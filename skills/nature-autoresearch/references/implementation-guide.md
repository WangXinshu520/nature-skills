# 系统论文实现指南 / Systems Paper Implementation Guide

基于 NSDI 2026 和 OSDI 2025 论文的实际实现模式，总结系统论文中常见的实现方法和工程实践。

Implementation patterns extracted from the actual codebases and implementation sections of NSDI 2026 and OSDI 2025 papers.

---

## 1. 实现模式概览 / Overview of Implementation Patterns

系统论文的实现通常遵循以下分层：

```
应用层 (Python)
├── 工作流编排、API、配置管理
│
中间层 (C++/CUDA)
├── 核心算法、数据流管理、资源分配
│
Kernel层 (CUDA/PTX)
├── GPU kernel、算子实现、硬件相关优化
│
通信层 (NCCL Plugin / RDMA)
└── 网络通信、多NIC管理、集合操作
```

| Layer | 典型语言 | 典型规模 | 示例 |
|-------|---------|---------|------|
| 应用层 | Python | 5K-15K LOC | NanoFlow runtime, vLLM |
| 中间层 | C++ | 2K-10K LOC | NanoFlow scheduling, FastServe |
| Kernel层 | CUDA | 2K-10K LOC | Mirage fused kernels, NanoFlow nano-ops |
| 通信层 | C++/NCCL | 1K-5K LOC | FuseLink NCCL plugin, ForestColl |

---

## 2. 通信层实现模式 / Communication Layer Patterns

### 2.1 NCCL Plugin 模式 (FuseLink风格)

FuseLink展示了一种成熟的GPU通信扩展模式：

```cpp
// 核心思路: 将GPU通信请求拆分为per-NIC的子流
// 通过NVLink relay实现单GPU利用多NIC

// 伪代码结构:
class MultiNICTransport {
  // 1. 物理拓扑探测
  TopologyMap discover_nvlink_to_nic_mapping();

  // 2. 流拆分策略
  struct FlowPlan {
    int src_gpu, dst_gpu;
    int nic_index;        // 分配到哪个NIC
    size_t offset, size;  // 数据分片
  };
  vector<FlowPlan> split_flow(Tensor data, int num_nics);

  // 3. NVLink relay: GPU A → NVSwitch → GPU B(接目标NIC)
  void relay_via_nvlink(FlowPlan plan);

  // 4. NCCL plugin接口
  ncclResult_t plugin_send(void* data, size_t count,
                           ncclDataType_t type, int peer);
};
```

**关键实现要点**:
- 拓扑发现需要在初始化时完成 (NVLink矩阵 + PCIe拓扑)
- 流拆分粒度: 按message size动态调整（小消息不拆分）
- NVLink relay的带宽上限: H100 NVLink 4.0 = 900 GB/s / GPU
- ~3000 LOC C++ NCCL plugin

### 2.2 集合通信调度模式 (ForestColl / HeteCCL风格)

```cpp
// 核心思路: 构造spanning tree计算吞吐最优schedule
// 输出: 每条链路的传输计划(什么时候发、发多少)

class CollectiveScheduler {
  // 1. 拓扑建模
  Graph build_topology_graph(vector<Node> nodes,
                              vector<Link> links);

  // 2. 生成最优schedule (线性规划/图算法)
  Schedule optimize_allreduce(Graph g, size_t msg_size);

  // 3. 注入到NCCL/RCCL
  void inject_schedule(Schedule s, ncclComm_t comm);
};
```

**支持的操作**: all-reduce, all-gather, reduce-scatter, all-to-all, broadcast
**算法复杂度**: ForestColl = O(|E|·log|V|) 多项式时间

---

## 3. CUDA Kernel 实现模式 / CUDA Kernel Patterns

### 3.1 超级优化模式 (Mirage风格)

Mirage的核心实现: 三级抽象搜索最优kernel

```cpp
// µGraph: 统一表示tensor program
struct muGraph {
  vector<muOP> operators;  // 最多11个操作
  // 对应: thread-block level → warp level → thread level
  vector<Tiling> tilings;  // 三级分块策略
};

// 核心组件:
// 1. µGraph builder: 从PyTorch计算图构建µGraph (Python)
// 2. Search engine: 在等价µGraph空间中搜索最优组合 (C++)
// 3. Kernel generator: 从最优µGraph生成CUDA kernel (CUDA)
// 4. Equivalence verifier: 概率性验证(< 10^-12 error) (C++)
```

**关键实现要点**:
- µGraph内的operator数量上限: 11 (受搜索空间限制)
- 等价性检查: 随机输入验证 + 代数化简
- 搜索时间: 11-28秒 per µGraph
- 生成kernel: 单文件CUDA kernel，与PyTorch通过torch.library集成

### 3.2 Nano-batch并行模式 (NanoFlow风格)

```cpp
// 核心思路: 将operation拆分为多个nano-operation
// 在多个CUDA stream上并发执行

class NanoOpScheduler {
  // 1. 批拆分
  vector<Batch> split_to_nano_batches(Batch full,
                                       int num_nano_ops);

  // 2. 资源分配 (每个nano-op占多少SM)
  struct ResourceAlloc {
    float compute_frac;    // 0.0-1.0，占多少SM
    int thread_blocks;     // 对应的thread block数
  };
  vector<ResourceAlloc> allocate_resources(Plan plan);

  // 3. 多stream执行
  void launch_on_streams(vector<NanoOp> ops,
                          vector<cudaStream_t> streams);

  // 4. 依赖管理 (CUDA events)
  void enforce_dependencies(vector<cudaEvent_t> events);
};
```

**关键实现要点**:
- CUDA stream数: 通常3-4个 (compute, memory, network)
- Interference profiling: 配对profiling (GEMM-GEMV, GEMM-Network)
- 资源利用率R (0.0-1.0) ↔ kernel选择映射: 预计算的查找表
- Auto-search: MILP solver (约10分钟)

### 3.3 内存Offloading模式 (SYMPHONY风格)

```cpp
// KV cache分层管理: GPU → CPU host → SSD
class HierarchicalKVCache {
  // 1. 优先级分配 (exploit NN structure)
  float compute_priority(int layer, int token_idx);

  // 2. Advisory prefetch
  void prefetch_on_access_pattern(vector<Request> upcoming);

  // 3. RDMA-based remote access
  void remote_read(KVCacheBlock block, int remote_node);
};
```

---

## 4. 应用层实现模式 / Application Layer Patterns

### 4.1 Serving Framework扩展模式

所有LLM serving论文几乎都是扩展现有框架：

```
vLLM / SGLang / DeepSpeed
├── 修改调度器 (Scheduler)
│   └── FastServe: 替换原有FCFS → Skip-Join MLFQ
│   └── NanoFlow: 替换batching → nano-batching
│   └── Libra: 替换partitioning → adaptive partitioning
├── 修改KV Cache管理器
│   └── SYMPHONY: GPU → remote memory pool
│   └── DroidSpeak: 跨变体共享
├── 修改批处理逻辑
│   └── NanoFlow: async batch formation
└── 添加Profiling/监控
    └── FLARE: tracing daemon
```

### 4.2 可复现性要点

所有系统论文实现应包含:

```python
# config.py - 所有可配置参数集中管理
class ExperimentConfig:
    # Hardware
    gpu_model: str = "A100-80GB-SXM"
    num_gpus: int = 2
    nvlink_version: int = 3
    nic_model: str = "ConnectX-6"
    nic_count: int = 2

    # Model
    model_name: str = "meta-llama/Llama-2-70b-hf"
    dtype: str = "fp16"
    tp_size: int = 2

    # Workload
    dataset: str = "sharegpt"
    request_rate: float = 10.0

    # Experiment
    warmup_iterations: int = 50
    measure_iterations: int = 200
    random_seed: int = 42

def run_experiment(config: ExperimentConfig) -> Results:
    """单一入口点的实验函数"""
    set_all_seeds(config.random_seed)
    model = load_model(config)
    warmup(model, config.warmup_iterations)
    results = measure(model, config.measure_iterations)
    save_results(results, config)
    return results
```

---

## 5. 实现检查清单 / Implementation Checklist

- [ ] 单一配置文件控制所有实验参数 (config.py / config.yaml)
- [ ] 固定随机种子 (Python + CUDA + NCCL)
- [ ] Warmup流程完善 (忽略前50次iteration)
- [ ] 测量足够的iteration (>200) 并报告统计信息
- [ ] 导出结果为结构化格式 (JSON/CSV)
- [ ] 提供绘图脚本 (matplotlib/plotly)
- [ ] Docker镜像或conda environment文件 (environment.yml)
- [ ] 记录commit hash和版本号
- [ ] 如果修改了开源框架，提供patch文件

---

## 6. 常见框架修改点 / Common Modification Points

### Serving框架 (vLLM/SGLang)
| 组件 | 修改点 | 相关论文 |
|------|--------|---------|
| Scheduler | 调度算法替换 | FastServe, Libra |
| Block Manager | KV cache管理 | SYMPHONY, DroidSpeak |
| Worker | 批处理逻辑 | NanoFlow |
| Model Runner | 推理引擎替换 | FlexLLM |

### 训练框架 (Megatron-LM/DeepSpeed)
| 组件 | 修改点 | 相关论文 |
|------|--------|---------|
| Pipeline Scheduler | 1F1B调度 | Attack of the Bubbles |
| Checkpointing | 梯度复制 | Checkmate |
| Communication | 集合通信 | HeteCCL |

### NCCL/RCCL
| 组件 | 修改点 | 相关论文 |
|------|--------|---------|
| Transport | 多NIC管理 | FuseLink |
| Topology | 拓扑感知调度 | ForestColl, HeteCCL |
| Collective algo | All-to-All | FAST |
