# LLM Serving & Inference Systems / 大模型推理与服务系统

Systems research on optimizing the serving, inference, and deployment of large language models. Covers scheduling, KV cache management, autoscaling, workload characterization, agent serving, and quantization.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference** [NSDI 2026]
   Preemptive iteration-level scheduling for LLM inference that reduces tail latency under bursty workloads. / 迭代级抢占式LLM推理调度，降低突发负载下的尾部延迟。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang) | [PDF](https://www.usenix.org/system/files/nsdi26-wu-bingyang.pdf)

2. **DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants** [NSDI 2026]
   Enables KV cache reuse across different fine-tuned variants of the same base model, reducing memory footprint and serving cost. / 跨微调模型变体共享KV缓存，降低内存占用和服务成本。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan) | [PDF](https://www.usenix.org/system/files/nsdi26-liu-yuhan.pdf)

3. **HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds** [NSDI 2026]
   Addresses cold start latency in serverless LLM deployments using model-aware pre-warming and adaptive scaling. / 通过模型感知预热和自适应扩缩解决无服务器LLM部署的冷启动延迟。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/lou) | [PDF](https://www.usenix.org/system/files/nsdi26-lou.pdf)

4. **JITServe: SLO-aware LLM Serving with Imprecise Request Information** [NSDI 2026]
   Handles LLM serving under imprecise SLO information, providing robust quality-of-service even with incomplete request metadata. / 在不精确SLO信息下提供鲁棒的LLM服务质量保证。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhang-wei) | [PDF](https://www.usenix.org/system/files/nsdi26-zhang-wei.pdf)

5. **FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees** [NSDI 2026]
   Co-schedules LLM inference and fine-tuning at token granularity while meeting SLOs for both workloads. / 以token粒度协同调度LLM推理与微调，同时满足两类负载的SLO。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/oliaro) | [PDF](https://www.usenix.org/system/files/nsdi26-oliaro.pdf)

6. **PlanetServe: A Decentralized, Scalable, and Privacy-Preserving Overlay for Democratizing Large Language Model Serving** [NSDI 2026]
   Decentralized P2P overlay network for LLM serving, enabling scalable and privacy-preserving inference without centralized infrastructure. / 去中心化P2P覆盖网络实现规模化隐私保护LLM推理。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/fang) | [PDF](https://www.usenix.org/system/files/nsdi26-fang.pdf)

7. **ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production** [NSDI 2026]
   Characterizes real-world LLM serving workloads and generates representative traces for evaluating serving systems. / 表征真实LLM服务负载并生成代表性trace用于系统评估。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | [PDF](https://www.usenix.org/system/files/nsdi26-xiang-servegen.pdf)

8. **Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads** [NSDI 2026]
   Adaptive request partitioning and scheduling that handles unbalanced, dynamic LLM workloads across heterogeneous serving nodes. / 自适应请求分区与调度，处理异构节点上的非均衡动态LLM负载。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra) | [PDF](https://www.usenix.org/system/files/nsdi26-ruan-libra.pdf)

9. **Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access For LLM via Semantic-Aware Knowledge Caching** [NSDI 2026]
   Semantic-aware caching system that reduces remote data access latency and cost for LLM-based agents by caching knowledge based on semantic similarity. / 基于语义相似度的知识缓存，降低LLM代理的远程数据访问延迟和成本。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/ruan-cortex) | [PDF](https://www.usenix.org/system/files/nsdi26-ruan-cortex.pdf)

10. **Agentix: An Efficient Serving Engine for LLM Agents as General Programs** [NSDI 2026]
    Serving engine optimized for LLM agents that execute as general programs with complex control flows, tool calls, and multi-turn interactions. / 优化LLM智能体通用程序执行的推理引擎，处理复杂控制流、工具调用和多轮交互。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/luo) | [PDF](https://www.usenix.org/system/files/nsdi26-luo.pdf)

11. **WaferLLM: Large Language Model Inference at Wafer Scale** [OSDI 2025]
    Wafer-scale LLM inference system that maps the entire model onto a single wafer for extreme throughput and energy efficiency. / 晶圆级LLM推理系统，将完整模型映射到单个晶圆上实现极致吞吐和能效。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/he) | [PDF](https://www.usenix.org/system/files/osdi25-he.pdf)

12. **BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching** [OSDI 2025]
    O(1) complexity host-level caching for live autoscaling of large model serving, enabling fast scale-up/down without performance degradation. / O(1)主机级缓存实现大模型服务的实时自动扩缩，无性能退化。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan) | [PDF](https://www.usenix.org/system/files/osdi25-zhang-dingyan.pdf)

13. **NanoFlow: Towards Optimal Large Language Model Serving Throughput** [OSDI 2025]
    Achieves near-optimal LLM serving throughput through fine-grained request scheduling and execution pipelining at the nano-batch level. / 通过纳级微批次细粒度请求调度和执行流水线实现接近最优的LLM服务吞吐。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/zhu-kan) | [PDF](https://www.usenix.org/system/files/osdi25-zhu-kan.pdf)

14. **DecDEC: A Systems Approach to Advancing Low-Bit LLM Quantization** [OSDI 2025]
    Systems-level framework that advances low-bit LLM quantization by jointly optimizing the quantization-dequantization pipeline with hardware-aware kernel design. / 系统级框架通过量化-反量化流水线与硬件感知kernel设计联动，推进低比特LLM量化。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/park-yeonhong) | [PDF](https://www.usenix.org/system/files/osdi25-park-yeonhong.pdf)

## 实验指导 / Experiment Guide

When running LLM serving experiments, the papers above use common patterns you can adopt:

### 典型实验配置 / Typical Setup
- **Hardware**: 8×NVIDIA H100/Hopper GPUs per node with NVLink + NVSwitch (intra-node 200GB/s), ConnectX-7 400Gbps NICs for inter-node (InfiniBand/RoCE), Intel Xeon CPUs
- **Models**: OPT (6.7B-30B), LLaMA-3 (8B-70B), Mixtral 8×7B/8×22B, GPT-3 family
- **Frameworks**: vLLM, SGLang, PyTorch with custom NCCL plugins

### 常用指标 / Common Metrics
| Metric | 用途 | Papers using it |
|--------|------|----------------|
| **TTFT** (Time-To-First-Token) | 首token延迟, 用户体感 | FastServe, BlitzScale, NanoFlow |
| **TPOT** (Time-Per-Output-Token) | 逐token生成延迟 | FastServe, NanoFlow |
| **Throughput** (tokens/s 或 requests/s) | 系统吞吐上限 | NanoFlow, Libra, FastServe |
| **SLO Attainment** (P50/P99) | 服务质量达标率 | JITServe, Libra, BlitzScale |
| **Cold Start Latency** | 冷启动开销 | HydraServe |

### 常用Baseline / Common Baselines
- **vLLM**: 最广泛使用的开源LLM推理引擎
- **Default NCCL with PXN**: GPU通信默认配置
- **Vanilla PyTorch**: 无优化的原生推理
- **TensorRT-LLM**: NVIDIA官方优化推理引擎

### 负载选择 / Workload Selection
- **Public trace sources**: Azure LLM traces, ShareGPT, LMSYS-Chat-1M
- **Synthetic patterns**: Poisson arrival with variable rates, bursty patterns
- **Mixed workloads**: 混合不同长度prompt, 混合prefill/decode比例

### 实验常见坑 / Common Pitfalls
- **预热不足**: LLM推理前几个iteration需要warmup, 忽略会导致数据偏差
- **KV cache 碎片化**: 长期运行后内存碎片化严重影响性能, 需长时间实验(>1h)
- **GPU-NIC拓扑不对称**: 不同节点的GPU-NIC连接方式不同, 影响跨节点通信(Burst/FuseLink论文重点讨论)
- **忽略SLO多样性和请求到达模式**: 仅用固定QPS测不出调度系统优劣

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

LLM serving research in 2025-2026 shows a clear shift from single-resource optimization (memory-bound assumption) to multi-resource orchestration and system-level throughput maximization. Key trends:

- **From memory-bound to compute-bound understanding**: NanoFlow demonstrated that modern LLM serving with GQA and large batches is actually compute-bound, contradicting the prevailing memory-bound assumption. This matters because it changes optimization targets.
- **Fine-grained scheduling**: FastServe (iteration-level preemption), NanoFlow (nano-batch pipelining), and Libra (adaptive partitioning) all push toward finer scheduling granularity to reduce resource waste.
- **Disaggregation for LLM serving**: SYMPHONY separates compute from KV cache storage, showing 2.4× latency reduction. This architectural pattern challenges monolithic serving designs.
- **Cold start and autoscaling**: HydraServe and BlitzScale address deployment elasticity—an under-explored but critical aspect of production serving.

### 论文亮点与局限 / Paper Highlights & Limitations

**NanoFlow** — 1.91× throughput boost (50-72% of theoretical optimum on LLaMA-2/3 70B, Qwen2-72B, Mixtral 8×7B, DeepSeek-67B). Key insight: intra-device parallelism via nano-batching overlaps compute/memory/network operations. Two-stage MILP auto-search finds optimal pipelines in ~10 minutes. **Limitation**: Assumes abundant requests; pipeline auto-search needs re-execution for significant model/workload changes. GPU interference modeling uses pairwise profiling with simplifications that may not fully capture 3-way contention.

**FastServe** — Iteration-level preemptive scheduling with skip-join MLFQ, reducing tail latency under bursty workloads. Proactive KV cache offload/upload for preemption support. **Limitation**: The semi-information-agnostic setting relies on input length heuristics that may not hold for all workloads. Preemption overhead increases with context length.

**SYMPHONY** — Disaggregated KV cache management with advisory prefetching (2.4× latency reduction, 4× request capacity increase on LLaMA models with ShareGPT/BurstGPT). Cooperative GPU-memory pool coordination. **Limitation**: Advisory request accuracy depends on workload predictability; overhead of remote KV cache access is bounded by network latency.

**DroidSpeak** — KV cache sharing across fine-tuned model variants. **Limitation**: Only applies when serving multiple LoRA/FT variants of the same base model; benefit diminishes with model diversity.

### 实用建议 / Practical Guidance

- **Production throughput**: NanoFlow for maximum throughput (2×+ over vLLM); expect 10 min auto-search overhead per deployment
- **Latency-sensitive apps**: FastServe for interactive workloads with strict latency requirements; pair with DroidSpeak if running multiple model variants
- **Cost optimization**: SYMPHONY if KV cache memory is the dominant cost; HydraServe + BlitzScale for serverless/elastic deployments
- **Workload understanding**: ServeGen for characterizing your specific production traffic before committing to a serving system
- **Agent workloads**: Agentix and Cortex specifically target LLM agent serving patterns (multi-turn, tool calls), which general serving systems handle suboptimally

## 写作指导 / Writing Guide

LLM serving 论文的写作要点（详细通用指南见 `references/paper-writing-guide.md`）：

- **Abstract关键数字**: 必须包含TTFT/TPOT/Throughput的提升百分比, P50/P99 SLO达成率
- **Motivation**: 用真实trace（ShareGPT/LMSYS）数据展示现有系统的不足, 不要用synthetic workload
- **Design section核心**: 清晰区分"调度策略"和"内存管理"两个子问题, 各自独立成节
- **Evaluation必含**: (1) End-to-end vs baselines (2) Latency CDF分布 (3) Ablation study (4) 不同模型/硬件的泛化性
- **常见审稿Challenge**: "你的improvement来自更好的tuning而非更好的算法" → 必须在ablation中证明每个设计决策的独立贡献

## 实现指导 / Implementation Guide

基于现有论文的实现模式（详细见 `references/implementation-guide.md`）：

- **入口点**: 几乎所有LLM serving论文都是基于vLLM/SGLang扩展, 修改Scheduler + BlockManager + Worker三个核心组件
- **通信层**: 通信优化 (NCCL plugin) 放在单独的C++模块, 约1000-3000 LOC
- **Kernel层**: GEMM/GEMV/Attention的CUDA优化单独打包, 约5000-15000 LOC
- **配置管理**: 所有参数集中在一个config类, 便于实验复现
- **Profiling**: 必须包含warmup (50+ iterations) + measurement (200+ iterations) 两个阶段

## 实验流程 / Experiment Pipeline

完整的LLM serving实验流程：

```
1. 环境准备
   ├── 8×H100/A100 DGX节点
   ├── CUDA ≥12.0 + PyTorch 2.x + vLLM 0.5+
   ├── 固定随机种子
   └── 记录所有版本号 (commit hash)

2. 模型下载 & 预热
   ├── 下载LLaMA-2/3 70B, Mixtral 8×7B, Qwen2-72B
   ├── 转换到目标精度 (FP16/BF16)
   └── Warmup 100 iterations (忽略前100次测量)

3. Baseline测试
   ├── vLLM (默认配置)
   ├── TensorRT-LLM
   ├── 你的系统 (默认配置)
   └── 每种配置: 3种workload × 3次重复

4. 负载测试
   ├── ShareGPT trace (真实对话)
   ├── LMSYS-Chat-1M (多轮对话)
   ├── Synthetic: Poisson(λ=10/20/50/100) 请求/秒
   └── 每种: 运行30分钟以上

5. 指标收集
   ├── TTFT: P50/P95/P99 + 平均值
   ├── TPOT: P50/P95/P99 + 平均值
   ├── Throughput: tokens/s/GPU
   ├── SLO Attainment: P99 TTFT < 2s
   └── GPU利用率: SM occupancy, memory BW

6. Ablation Study
   ├── 逐个关闭系统特性, 测量性能下降
   ├── 证明每个组件的独立贡献
   └── 展示在哪些场景下你的系统最有效

7. 泛化测试
   ├── 在不同模型大小上测试 (8B/13B/70B)
   ├── 在不同GPU上测试 (A100/H100)
   └── 在不同请求长度上测试

8. 结果分析
   ├── 生成对比柱状图 (Figure 7 style)
   ├── 生成延迟CDF图
   └── 生成Ablation breakdown图
```

## 注意事项 / Notes

- LLM serving research is fast-moving; check for follow-up work from the same groups.
- Most systems assume NVIDIA GPU clusters; evaluate applicability to your hardware.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
