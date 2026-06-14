# GPU Communication & Collective Operations / GPU通信与集合操作

Systems research on GPU-to-GPU communication, collective operations, and multi-NIC transport for distributed AI workloads. Covers MoE all-to-all communication, heterogeneous cluster scheduling, and high-speed interconnects.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading** [NSDI 2026]
   Accelerates Mixture-of-Experts inference by fusing communication buffers and offloading tensor memory access (TMA) operations to hardware. / 通过融合通信缓冲区和卸载张量内存访问操作到硬件，加速MoE推理。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/li-xingyi) | [PDF](https://www.usenix.org/system/files/nsdi26-li-xingyi.pdf)

2. **ForestColl: Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics** [NSDI 2026]
   Throughput-optimal algorithm for collective communication operations (all-reduce, all-to-all) on heterogeneous network fabrics mixing different link speeds and topologies. / 吞吐最优的异构网络结构集合通信算法，混合不同链路速度和拓扑。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhao-liangyu) | [PDF](https://www.usenix.org/system/files/nsdi26-zhao-liangyu.pdf)

3. **FAST: An Efficient Scheduler for All-to-All GPU Communication** [NSDI 2026]
   Efficient scheduling algorithm for all-to-all GPU communication patterns in MoE and other distributed workloads, minimizing contention and maximizing bandwidth utilization. / 高效的all-to-all GPU通信调度算法，最小化竞争并最大化带宽利用率。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/lei-yiran) | [PDF](https://www.usenix.org/system/files/nsdi26-lei-yiran.pdf)

4. **HeteCCL: Synthesizing Near-Optimal Collective Communication Schedules for Heterogeneous GPU Clusters** [NSDI 2026]
   Synthesizes near-optimal collective communication schedules for clusters with heterogeneous GPU types and interconnects, generalizing across hardware generations. / 为异构GPU和互联的集群合成接近最优的集合通信调度方案。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/hei) | [PDF](https://www.usenix.org/system/files/nsdi26-hei.pdf)

5. **FuseLink: Enabling Efficient GPU Communication over Multiple NICs** [OSDI 2025]
   Efficiently multiplexes GPU communication across multiple NICs with intelligent flow scheduling, achieving near-linear bandwidth scaling with NIC count. / 通过智能流调度在多NIC间高效复用GPU通信，实现随NIC数量接近线性的带宽扩展。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/ren) | [PDF](https://www.usenix.org/system/files/osdi25-ren.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Hardware**: 8×H100 per node, NVLink intra-node (200GB/s), ConnectX-7 400Gbps NICs ×8 per node, GPU-NIC 1:1直连 or 1:N with NVSwitch relay
- **GPU-NIC拓扑**: 每个GPU直连一个NIC (PCIe bridge) 是最简单配置; 论文中FuseLink展示了利用NVLink relay让单GPU使用多NIC
- **NCCL版本**: ≥2.18 (支持PXN), 自定义NCCL plugin for FuseLink-style optimizations

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **Inter-server Bandwidth (GB/s)** | 跨节点GPU通信带宽 | FuseLink (基线50GB/s, FuseLink 212GB/s with 6 NICs) |
| **All-to-All Completion Time** | MoE通信延迟 | FAST, SwiftEP |
| **NIC Utilization** | 多NIC利用率均衡度 | FuseLink |
| **Scheduling Overhead (µs)** | 通信调度额外开销 | FuseLink (~0.8-5.6µs/op) |
| **Collective Communication Throughput** | 集合通信吞吐 | ForestColl, HeteCCL |

### 常用Baseline / Common Baselines
- **NCCL with PXN enabled**: 默认最优配置 (单NIC绑定)
- **Static NIC Binding**: 每个GPU固定绑定一个NIC
- **MP-RDMA / MPTCP**: 多路径传输协议baselines
- **NCCL without PXN**: 无优化的PCIe路径

### 实验常见坑 / Common Pitfalls
- **GPU-NIC拓扑影响巨大**: 不同节点的GPU和NIC物理连接方式可能不同，需要确认拓扑再下结论 (FuseLink论文重点讨论)
- **微基准与大模型差异**: 单GPU带宽micro-benchmark优秀的方案，在大模型训练/推理中不一定好(通信模式不同)
- **NIC负载均衡假设**: 负载均衡的通信 (如AllReduce) 各NIC利用率均衡，优化空间在非均衡的P2P通信 (MoE, 分散式推理)
- **NVLink vs PCIe瓶颈**: 多NIC聚合受NVLink带宽上限限制，不能无限扩展

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

GPU communication is the critical scaling bottleneck for distributed AI workloads, especially with MoE architectures driving all-to-all communication patterns. Key trends:

- **Heterogeneity-first design**: ForestColl and HeteCCL acknowledge that real GPU clusters have mixed hardware (A100+H100, different NVLink versions, varied topologies). Optimizing for heterogeneous fabrics delivers more practical gains than homogeneous assumptions.
- **MoE driving communication innovation**: SwiftEP and FAST specifically target MoE all-to-all communication—the communication pattern set to dominate as MoE models become standard.
- **Multi-NIC as a practical path**: FuseLink shows that efficient multi-NIC multiplexing (4.2× bandwidth improvement, 1.04-2.73× serving speedup) can close the gap to specialized interconnects without new hardware.

### 论文亮点与局限 / Paper Highlights & Limitations

**ForestColl** — Throughput-optimal collective communication schedules via spanning tree construction, proven optimal for any network topology. Polynomial-time schedule generation. Validated on AMD MI250 and NVIDIA DGX A100/H100 clusters, outperforming vendor communication libraries (NCCL, RCCL). **Limitation**: Generated schedules are topology-static; re-computation needed for topology changes. Does not dynamically adapt to transient contention.

**FuseLink** — Efficient multi-NIC GPU communication achieving near-linear bandwidth scaling (212GBps vs 50GBps single-NIC baseline). ~3000 LOC NCCL plugin—practical integration with existing distributed training frameworks. **Limitation**: Optimized for imbalanced P2P traffic patterns (MoE-style); less benefit for symmetric collective communications like all-reduce.

**SwiftEP** — Buffer fusion + TMA offloading for MoE inference communication. Hardware-aware optimization leveraging modern GPU DMA engines. **Limitation**: TMA features are H100/B100-specific; limited portability to older hardware or AMD GPUs.

**FAST** — Efficient all-to-all scheduling minimizing contention and maximizing bandwidth utilization. **Limitation**: Best for topologies where all-to-all dominates; less impact when point-to-point communication is the bottleneck.

### 实用建议 / Practical Guidance

- **NCCL replacement**: ForestColl for heterogeneous clusters where NCCL's built-in schedules are suboptimal; measure gains on your specific topology
- **Multi-NIC deployment**: FuseLink for clusters with multiple NICs per node (common in cloud deployments); the ~3000 LOC plugin makes integration straightforward
- **MoE inference**: SwiftEP for H100/B100 MoE deployments; FuseLink + FAST for all-to-all scheduling breadth
- **Heterogeneous clusters**: HeteCCL for clusters mixing GPU generations; ForestColl for heterogeneous network fabrics

## 写作指导 / Writing Guide

- **Motivation核心**: 用micro-benchmark展示现有方案的带宽利用率(e.g., "NCCL PXN only achieves 50GBps out of 400Gbps")
- **Evaluation必须**: (1) dot-to-dot micro-benchmark (2) end-to-end with 真实训练/推理负载 (3) scaling with NIC count (4) 不同消息大小的性能
- **审稿关键问题**: "你对NCCL的修改是否会引入正确性问题？" → 必须提供correctness验证 (randomized testing)

## 实现指导 / Implementation Guide

- **NCCL Plugin模式** (FuseLink): ~3000 LOC C++ plugin, 修改transport + topology层
- **集合通信调度** (ForestColl/HeteCCL): 图算法 + schedule注入, 侵入NCCL collective algo层
- **MoE通信** (SwiftEP/FAST): all-to-all scheduling + kernel fusion
- **测试**: `nccl-tests` (perf) + `nccl-validator` (correctness)

## 实验流程 / Experiment Pipeline

```
1. 基准测试 (每个通信模式独立测试):
   ├── nccl-tests: all_reduce, all_gather, all_to_all, sendrecv
   ├── 消息大小: 1KB→1GB, 对数间隔
   ├── NIC数: 1/2/4/6/8 (如果硬件支持)
   └── 重复100+次, 报告bus BW mean±std

2. 端到端测试:
   ├── AllReduce w/ GPT-3 175B (TP=8)
   ├── All-to-All w/ Mixtral 8×22B (MoE)
   ├── 测量: per-iteration communication time
   └── 测量: training throughput (samples/s)

3. 多拓扑测试:
   ├── 测试至少2种网络拓扑 (fat-tree, dragonfly)
   └── 测试异构GPU集群 (A100+H100混合)
```

## 注意事项 / Notes

- Most GPU communication research targets NVIDIA GPUs with NCCL and InfiniBand/RoCE.
- MoE all-to-all communication (SwiftEP, FAST) is a hot topic in 2025-2026.
- Collective communication optimizations (ForestColl, HeteCCL) are critical for training at 1000+ GPU scale.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
