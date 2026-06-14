# LLM Training Systems / 大模型训练系统

Systems research on large language model training, including distributed training, fine-tuning, training diagnosis, reliability, checkpointing, and training simulation.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **Checkmate: Zero Performance Overhead Model Checkpointing via Network Gradient Replication** [NSDI 2026]
   Zero-overhead distributed checkpointing by replicating gradients over the network during training, eliminating checkpoint stalls. / 训练时通过网络梯度复制实现零开销分布式检查点，消除检查点停滞。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/bhardwaj) | [PDF](https://www.usenix.org/system/files/nsdi26-bhardwaj.pdf)

2. **Di-PS: System-Algorithm Co-Design for Asynchronous and Heterogeneous Cross-cluster LLM Training at Scale** [NSDI 2026]
   Cross-cluster asynchronous training with system-algorithm co-design that handles heterogeneous cluster resources and network conditions. / 系统-算法协同设计的跨集群异步训练，处理异构资源和网络条件。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/li-shengwei) | [PDF](https://www.usenix.org/system/files/nsdi26-li-shengwei.pdf)

3. **FLARE: Anomaly Diagnostics for Divergent LLM Training in GPU Clusters of Thousand-Plus Scale** [NSDI 2026]
   Automated anomaly detection and root-cause analysis for LLM training failures at thousand-GPU scale. / 千卡规模LLM训练异常的自动化检测与根因分析。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/cui) | [PDF](https://www.usenix.org/system/files/nsdi26-cui.pdf)

4. **EROICA: Online Performance Troubleshooting for Large-scale Model Training** [NSDI 2026]
   Online performance diagnosis system that identifies bottlenecks in large-scale model training without requiring offline profiling. / 在线性能诊断系统，无需离线profiling即可识别大规模模型训练瓶颈。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/guan-yu) | [PDF](https://www.usenix.org/system/files/nsdi26-guan-yu.pdf)

5. **Supercharging Packet-level Network Simulation of Large Model Training via Memoization and Fast-Forwarding** [NSDI 2026]
   Accelerates packet-level simulation of distributed training workloads using memoization and state fast-forwarding techniques. / 通过记忆化和状态快进技术加速分布式训练负载的包级仿真。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/long) | [PDF](https://www.usenix.org/system/files/nsdi26-long.pdf)

6. **MuxTune: Efficient Multi-Task LLM Fine-Tuning in Multi-Tenant Datacenters via Spatial-Temporal Backbone Multiplexing** [NSDI 2026]
   Shares backbone model across multiple fine-tuning tasks in multi-tenant datacenters through spatial-temporal multiplexing of model parameters. / 通过模型参数的空时复用，在多租户数据中心跨多个微调任务共享骨干模型。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/xue-chunyu) | [PDF](https://www.usenix.org/system/files/nsdi26-xue-chunyu.pdf)

7. **Attack of the Bubbles: Straggler-Resilient Pipeline Parallelism for Large Model Training** [NSDI 2026]
   Addresses the pipeline bubble problem in pipeline-parallel training, providing straggler resilience without sacrificing throughput. / 解决流水线并行训练中的pipeline bubble问题，提供落后者容忍而不牺牲吞吐。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wu-tianyuan) | [PDF](https://www.usenix.org/system/files/nsdi26-wu-tianyuan.pdf)

8. **ZipLLM: Efficient LLM Storage via Model-Aware Synergistic Data Deduplication and Compression** [NSDI 2026]
   Combines model-aware deduplication and compression for efficient LLM storage, reducing disk footprint without affecting serving performance. / 模型感知的去重与压缩协同优化LLM存储，减少磁盘占用不影响服务性能。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wang-zirui) | [PDF](https://www.usenix.org/system/files/nsdi26-wang-zirui.pdf)

9. **Phantora: Maximizing Code Reuse in Simulation-based Machine Learning System Performance Estimation** [NSDI 2026]
   Simulation framework maximizing code reuse for ML training system performance estimation across different hardware configurations. / 最大化代码复用的仿真框架，跨不同硬件配置估计ML训练系统性能。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/qin) | [PDF](https://www.usenix.org/system/files/nsdi26-qin.pdf)

10. **Training with Confidence: Catching Silent Errors in Deep Learning Training with Automated Proactive Checks** [OSDI 2025]
    Proactive error detection system that catches silent data corruption during DL training using statistical checks and invariants. / 主动错误检测系统，通过统计检查和不变性在DL训练中捕获静默数据损坏。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/jiang) | [PDF](https://www.usenix.org/system/files/osdi25-jiang.pdf)

11. **Understanding Stragglers in Large Model Training Using What-if Analysis** [OSDI 2025]
    Systematic analysis of straggler causes and impacts in large model training, providing insights for designing straggler-resilient training systems. / 系统分析大模型训练中的落后者成因和影响，为落后者容忍训练系统设计提供洞见。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/lin-jinkun) | [PDF](https://www.usenix.org/system/files/osdi25-lin-jinkun.pdf)

12. **WLB-LLM: Workload-Balanced 4D Parallelism for Large Language Model Training** [OSDI 2025]
    Workload-balanced 4D parallelism (data, tensor, pipeline, sequence) for LLM training that dynamically rebalances across dimensions. / 负载均衡的4D并行（数据、张量、流水线、序列）动态重均衡训练策略。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/wang-zheng) | [PDF](https://www.usenix.org/system/files/osdi25-wang-zheng.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Hardware**: 千卡级GPU集群 (H100/A100), NVLink intra-node + InfiniBand/RoCE inter-node (400Gbps)
- **Frameworks**: Megatron-LM, DeepSpeed, PyTorch FSDP, NCCL
- **Training configs**: 数据并行(DP) × 张量并行(TP) × 流水线并行(PP) × 序列并行(SP) 四维组合

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **MFU** (Model FLOPs Utilization) | 训练算力效率 | WLB-LLM, Attack of the Bubbles |
| **Iteration Time** | 单步训练耗时 | Di-PS, Checkmate, WLB-LLM |
| **Checkpoint Overhead** | 检查点占迭代比例 | Checkmate |
| **Straggler Ratio** | 落后者占比 | Understanding Stragglers, Attack of the Bubbles |
| **Anomaly Detection Recall** | 训练异常检测率 | FLARE, EROICA |
| **Silent Error Detection Rate** | 静默错误检出率 | Training with Confidence |

### 常用Baseline / Common Baselines
- **Megatron-LM**: NVIDIA官方分布式训练框架 (PP+TP)
- **DeepSpeed ZeRO-3**: 微软分布式训练框架
- **PyTorch FSDP**: PyTorch原生全分片数据并行
- **Default NCCL**: 通信层baseline
- **Periodic Checkpointing**: 传统定时检查点 (vs Checkmate)

### 实验常见坑 / Common Pitfalls
- **Scale matters**: 小规模(8卡)实验结论不能直接推广到大集群(千卡+)。Straggler、网络拥塞等在大规模才明显。
- **通信-计算overlap**: 简单的iteration time不足以评估系统，要同时测量通信等待时间和计算时间 (参考EROICA的在线诊断方法)。
- **多次运行取平均**: 训练实验噪声大 (网络波动、GPU温度 throttling)，至少3次重复实验。
- **检查点开销隐藏**: 检查点实验需要长时间(>1h)运行才能观察到真实开销模式。

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

LLM training systems research in 2025-2026 reflects the reality of training at 1000+ GPU scale. The key shift is from optimizing healthy-cluster performance to managing the inherent unreliability of large-scale training. Key themes:

- **Training diagnosis and reliability as first-class concerns**: FLARE and EROICA address real-world failures at thousand-GPU scale—a problem that is growing faster than the hardware. Training with Confidence catches silent errors that traditional monitoring misses.
- **Simulation-driven design**: Supercharging, Phantora, and Arcadia show that the complexity of large-scale training demands simulation before deployment, reducing costly trial-and-error on production clusters.
- **Pipeline efficiency**: Attack of the Bubbles and WLB-LLM address fundamental inefficiencies in parallelism—bubble overhead and load imbalance—that compound at scale.
- **Storage and checkpointing**: ZipLLM and Checkmate show that training I/O (storage and checkpointing) is as critical as compute, especially with increasingly large models.

### 论文亮点与局限 / Paper Highlights & Limitations

**FLARE** — Deployed across 6,000 GPUs in production. Full-stack tracing daemon with backend-extensible architecture, automatic root-cause analysis for performance regressions. **Limitation**: Diagnostic coverage limited to known anomaly patterns; novel failure modes require rule updates.

**Checkmate** — Zero-overhead checkpointing via network gradient replication, eliminating stalls that waste 10-30% of training time at scale. **Limitation**: Requires fast network interconnects; benefit diminishes on bandwidth-constrained links.

**EROICA** — Online performance troubleshooting without offline profiling—critical because offline profiling of 1000-GPU runs is impractical. **Limitation**: Online analysis accuracy depends on sampling granularity.

**WLB-LLM** — Workload-balanced 4D parallelism (data, tensor, pipeline, sequence) that dynamically rebalances—addresses the combinatorial complexity of choosing parallelism strategies. **Limitation**: Dynamic rebalancing adds control overhead; best for heterogeneous clusters.

**Di-PS** — Cross-cluster asynchronous training handling heterogeneous resources. **Limitation**: Asynchronous updates introduce staleness that may affect model quality; best for pre-training or tasks tolerant to staleness.

### 实用建议 / Practical Guidance

- **Training reliability**: Deploy FLARE or EROICA before scaling past 100 GPUs; the ROI increases with cluster size
- **Checkpointing efficiency**: Checkmate for frequent checkpointing with zero overhead; pair with ZipLLM for storage reduction
- **Parallelism strategy**: WLB-LLM for auto-selecting parallelism configurations; Attack of the Bubbles for reducing bubble overhead in pipeline-parallel setups
- **Simulation**: Use Supercharging/Phantora to estimate training performance before hardware purchase or cluster expansion
- **Multi-tenant training**: MuxTune for shared-backbone fine-tuning in multi-tenant environments

## 写作指导 / Writing Guide

- **Abstract核心数字**: MFU提升、iteration time降低%、checkpoint开销占比
- **Motivation关键**: 说明"在小规模(8卡)上表现好的方案在大规模(1000+卡)上为什么不行"
- **Design组织**: 按并行维度组织 (data/TP/PP/SP × diagnosis/reliability/storage)
- **Evaluation必须**: (1) 至少两种模型规模 (2) 大规模(>64 GPU)scaling测试 (3) 多次重复+error bar (4) GPU利用率breakdown (5) 故障注入实验（诊断论文必须）
- **Scale matters审稿要点**: 审稿人最常问"这个在1000+ GPU上还有效吗"

## 实现指导 / Implementation Guide

- **入口点**: 基于Megatron-LM或DeepSpeed扩展, 修改Parallelism策略层
- **训练框架修改**: Pipeline scheduler (1F1B) + Checkpoint manager + Communication backend
- **诊断系统**: 全栈tracing daemon (FLARE风格) + 在线profiling (EROICA风格)
- **配置文件**: 同时提供8卡/64卡/256卡/1024卡四种规模的配置文件
- **关键依赖**: NCCL版本 ≥2.18, CUDA ≥12.0, 特定拓扑文件

## 实验流程 / Experiment Pipeline

```
1. 集群准备
   ├── 至少256 GPU (推荐512+)
   ├── NVLink intra-node + InfiniBand/RoCE inter-node
   ├── NCCL ≥2.18, Megatron-LM最新版
   └── 验证所有GPU可用 + NVLink健康

2. 诊断实验 (FLARE/EROICA类)
   ├── 注入已知故障类型 (GPU掉线/NCCL超时/慢节点)
   ├── 测量检测延迟 (detection latency)
   ├── 测量根因定位准确率 (root cause accuracy)
   └── 至少1000+迭代, 测试误报率

3. 训练性能实验
   ├── 模型: LLaMA-2 7B/13B/70B
   ├── 并行配置: DP×TP×PP多组
   ├── 每种配置: 运行100+ iterations (排除warmup)
   ├── 指标: MFU, Iteration Time, Communication Time
   └── 重复3次, 报告mean±std

4. Checkpointing实验 (Checkmate类)
   ├── Baseline: periodic checkpoint (每N步)
   ├── Ours: network gradient replication
   ├── 测量: checkpoint overhead/iteration
   └── 测试场景: GPU故障/NCCL超时恢复

5. Fault Tolerance实验
   ├── 注入GPU故障 (模拟硬件故障)
   ├── 注入网络故障 (模拟NCCL超时)
   ├── 测量: 恢复时间 + 训练质量影响
   └── 与baseline checkpoint方案对比

6. Scaling实验
   ├── 8 GPU → 64 → 256 → 512 → 1024
   ├── 报告scaling efficiency (理想线性×实测)
   └── 分析scaling瓶颈(通信/计算/内存)

7. Generalization
   ├── 不同模型架构 (dense/MoE)
   ├── 不同硬件 (A100/H100/B200)
   └── 不同网络拓扑
```

## 注意事项 / Notes

- Training systems often have complex dependencies on specific hardware (NCCL, InfiniBand, CUDA version).
- Diagnosis tools (FLARE, EROICA) complement reliability tools (Checkmate, Training with Confidence).
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
