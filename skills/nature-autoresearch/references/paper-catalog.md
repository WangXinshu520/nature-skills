# Paper Catalog: Systems Research for AI / AI系统研究论文目录

Complete catalog of 68 systems research papers from top conferences covering LLM serving, training, GPU communication, tensor compilers, vector search, and more. Each entry includes title, authors, conference, year, contribution summary (English + Chinese), and links.

For paper evaluations (strengths, limitations, practical impact, comparison context) and experiment design guidance (metrics, baselines, common pitfalls), see the corresponding `static/fragments/research_topic/*.md` files.

论文评价（优势、局限、实际影响、对比分析）和实验设计指导（指标选择、baseline设置、常见坑）请参见对应的 `static/fragments/research_topic/*.md` 文件。

---

## NSDI 2026 (44 papers)

### LLM Serving & Inference

1. **FastServe: Iteration-Level Preemptive Scheduling for Large Language Model Inference**
   Authors: Bingyang Wu et al. | Conference: NSDI 2026 | Tags: llm-serving
   Preemptive iteration-level scheduling for LLM inference that reduces tail latency under bursty workloads. / 迭代级抢占式LLM推理调度，降低突发负载下的尾部延迟。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wu-bingyang) | [PDF](https://www.usenix.org/system/files/nsdi26-wu-bingyang.pdf)

2. **DroidSpeak: KV Cache Sharing Across Fine-tuned Model Variants**
   Authors: Yuhan Liu et al. | Conference: NSDI 2026 | Tags: llm-serving, kv-cache
   Enables KV cache reuse across different fine-tuned variants of the same base model. / 跨微调模型变体共享KV缓存，降低内存占用和服务成本。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/liu-yuhan) | [PDF](https://www.usenix.org/system/files/nsdi26-liu-yuhan.pdf)

3. **HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds**
   Authors: Authors et al. | Conference: NSDI 2026 | Tags: llm-serving, serverless
   Addresses cold start latency in serverless LLM deployments using model-aware pre-warming. / 通过模型感知预热解决无服务器LLM部署的冷启动延迟。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/lou) | [PDF](https://www.usenix.org/system/files/nsdi26-lou.pdf)

4. **JITServe: SLO-aware LLM Serving with Imprecise Request Information**
   Authors: Wei Zhang et al. | Conference: NSDI 2026 | Tags: llm-serving, slo
   Handles LLM serving under imprecise SLO information with robust quality-of-service. / 在不精确SLO信息下提供鲁棒的LLM服务质量保证。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhang-wei) | [PDF](https://www.usenix.org/system/files/nsdi26-zhang-wei.pdf)

5. **FlexLLM: Token-Level Co-Serving of LLM Inference and Finetuning with SLO Guarantees**
   Authors: Oliaro et al. | Conference: NSDI 2026 | Tags: llm-serving, fine-tuning
   Co-schedules LLM inference and fine-tuning at token granularity while meeting SLOs. / 以token粒度协同调度LLM推理与微调，同时满足两类负载的SLO。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/oliaro) | [PDF](https://www.usenix.org/system/files/nsdi26-oliaro.pdf)

6. **PlanetServe: A Decentralized, Scalable, and Privacy-Preserving Overlay for Democratizing Large Language Model Serving**
   Authors: Fang et al. | Conference: NSDI 2026 | Tags: llm-serving, decentralized
   Decentralized P2P overlay network for scalable and privacy-preserving LLM serving. / 去中心化P2P覆盖网络实现规模化隐私保护LLM推理。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/fang) | [PDF](https://www.usenix.org/system/files/nsdi26-fang.pdf)

7. **ServeGen: Workload Characterization and Generation of Large Language Model Serving in Production**
   Authors: Xiang et al. | Conference: NSDI 2026 | Tags: llm-serving, workload
   Characterizes real-world LLM serving workloads and generates representative traces. / 表征真实LLM服务负载并生成代表性trace用于系统评估。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen) | [PDF](https://www.usenix.org/system/files/nsdi26-xiang-servegen.pdf)

8. **Libra: Flexible Request Partitioning and Scheduling for Serving Unbalanced and Dynamic LLM Workloads**
   Authors: Ruan et al. | Conference: NSDI 2026 | Tags: llm-serving, scheduling
   Adaptive request partitioning and scheduling for unbalanced, dynamic LLM workloads. / 自适应请求分区与调度，处理异构节点上的非均衡动态LLM负载。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/ruan-libra) | [PDF](https://www.usenix.org/system/files/nsdi26-ruan-libra.pdf)

9. **Cortex: Achieving Low-Latency, Cost-Efficient Remote Data Access For LLM via Semantic-Aware Knowledge Caching**
   Authors: Ruan et al. | Conference: NSDI 2026 | Tags: llm-serving, caching, agents
   Semantic-aware caching that reduces remote data access latency for LLM-based agents. / 基于语义相似度的知识缓存，降低LLM代理的远程数据访问延迟和成本。
   [Presentation](https://www.usenix.org/conference/nsdi26/presentation/ruan-cortex) | [PDF](https://www.usenix.org/system/files/nsdi26-ruan-cortex.pdf)

10. **Agentix: An Efficient Serving Engine for LLM Agents as General Programs**
    Authors: Luo et al. | Conference: NSDI 2026 | Tags: llm-serving, agents
    Serving engine optimized for LLM agents executing as general programs. / 优化LLM智能体通用程序执行的推理引擎。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/luo) | [PDF](https://www.usenix.org/system/files/nsdi26-luo.pdf)

### LLM Training & Diagnosis

11. **Checkmate: Zero Performance Overhead Model Checkpointing via Network Gradient Replication**
    Authors: Bhardwaj et al. | Conference: NSDI 2026 | Tags: llm-training, checkpointing
    Zero-overhead distributed checkpointing via network gradient replication. / 通过网络梯度复制实现零开销分布式检查点。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/bhardwaj) | [PDF](https://www.usenix.org/system/files/nsdi26-bhardwaj.pdf)

12. **Di-PS: System-Algorithm Co-Design for Asynchronous and Heterogeneous Cross-cluster LLM Training at Scale**
    Authors: Shengwei Li et al. | Conference: NSDI 2026 | Tags: llm-training, distributed
    Cross-cluster asynchronous training with system-algorithm co-design. / 系统-算法协同设计的跨集群异步训练。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/li-shengwei) | [PDF](https://www.usenix.org/system/files/nsdi26-li-shengwei.pdf)

13. **FLARE: Anomaly Diagnostics for Divergent LLM Training in GPU Clusters of Thousand-Plus Scale**
    Authors: Cui et al. | Conference: NSDI 2026 | Tags: llm-training, diagnosis
    Anomaly detection and root-cause analysis for LLM training at thousand-GPU scale. / 千卡规模LLM训练异常的自动化检测与根因分析。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/cui) | [PDF](https://www.usenix.org/system/files/nsdi26-cui.pdf)

14. **EROICA: Online Performance Troubleshooting for Large-scale Model Training**
    Authors: Yu Guan et al. | Conference: NSDI 2026 | Tags: llm-training, diagnosis
    Online performance diagnosis for large-scale model training. / 在线性能诊断系统，无需离线profiling即可识别大规模模型训练瓶颈。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/guan-yu) | [PDF](https://www.usenix.org/system/files/nsdi26-guan-yu.pdf)

15. **Supercharging Packet-level Network Simulation of Large Model Training via Memoization and Fast-Forwarding**
    Authors: Long et al. | Conference: NSDI 2026 | Tags: llm-training, simulation
    Accelerates packet-level simulation of distributed training via memoization. / 通过记忆化技术加速分布式训练的包级仿真。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/long) | [PDF](https://www.usenix.org/system/files/nsdi26-long.pdf)

16. **MuxTune: Efficient Multi-Task LLM Fine-Tuning in Multi-Tenant Datacenters via Spatial-Temporal Backbone Multiplexing**
    Authors: Chunyu Xue et al. | Conference: NSDI 2026 | Tags: llm-training, fine-tuning
    Shares backbone model across multiple fine-tuning tasks through spatial-temporal multiplexing. / 通过模型参数的空时复用跨多个微调任务共享骨干模型。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/xue-chunyu) | [PDF](https://www.usenix.org/system/files/nsdi26-xue-chunyu.pdf)

17. **Attack of the Bubbles: Straggler-Resilient Pipeline Parallelism for Large Model Training**
    Authors: Tianyuan Wu et al. | Conference: NSDI 2026 | Tags: llm-training, pipeline-parallelism
    Straggler-resilient pipeline parallelism addressing the pipeline bubble problem. / 解决流水线并行训练中的pipeline bubble问题，提供落后者容忍。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wu-tianyuan) | [PDF](https://www.usenix.org/system/files/nsdi26-wu-tianyuan.pdf)

18. **ZipLLM: Efficient LLM Storage via Model-Aware Synergistic Data Deduplication and Compression**
    Authors: Zirui Wang et al. | Conference: NSDI 2026 | Tags: llm-training, storage
    Model-aware deduplication and compression for efficient LLM storage. / 模型感知的去重与压缩协同优化LLM存储。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wang-zirui) | [PDF](https://www.usenix.org/system/files/nsdi26-wang-zirui.pdf)

19. **Phantora: Maximizing Code Reuse in Simulation-based Machine Learning System Performance Estimation**
    Authors: Qin et al. | Conference: NSDI 2026 | Tags: llm-training, simulation
    Simulation framework maximizing code reuse for ML training performance estimation. / 最大化代码复用的仿真框架，估计ML训练系统性能。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/qin) | [PDF](https://www.usenix.org/system/files/nsdi26-qin.pdf)

### GPU Communication & Collective Ops

20. **SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading**
    Authors: Xingyi Li et al. | Conference: NSDI 2026 | Tags: gpu-communication, moe
    Accelerates MoE inference via buffer fusion and TMA offloading. / 通过融合通信缓冲区和卸载TMA操作加速MoE推理。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/li-xingyi) | [PDF](https://www.usenix.org/system/files/nsdi26-li-xingyi.pdf)

21. **ForestColl: Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics**
    Authors: Liangyu Zhao et al. | Conference: NSDI 2026 | Tags: gpu-communication, collective
    Throughput-optimal collective communication on heterogeneous network fabrics. / 吞吐最优的异构网络结构集合通信算法。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhao-liangyu) | [PDF](https://www.usenix.org/system/files/nsdi26-zhao-liangyu.pdf)

22. **FAST: An Efficient Scheduler for All-to-All GPU Communication**
    Authors: Yiran Lei et al. | Conference: NSDI 2026 | Tags: gpu-communication, all-to-all
    Efficient all-to-all GPU communication scheduling for MoE workloads. / 高效的all-to-all GPU通信调度算法，最小化竞争并最大化带宽利用率。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/lei-yiran) | [PDF](https://www.usenix.org/system/files/nsdi26-lei-yiran.pdf)

23. **HeteCCL: Synthesizing Near-Optimal Collective Communication Schedules for Heterogeneous GPU Clusters**
    Authors: Hei et al. | Conference: NSDI 2026 | Tags: gpu-communication, collective
    Near-optimal collective communication schedules for heterogeneous GPU clusters. / 为异构GPU集群合成接近最优的集合通信调度方案。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/hei) | [PDF](https://www.usenix.org/system/files/nsdi26-hei.pdf)

### RL Training Infrastructure

24. **RollPacker: Taming Long-Tail Rollouts for RL Post-Training with Tail Batching**
    Authors: Wei Gao et al. | Conference: NSDI 2026 | Tags: rl-training, rlhf
    Dynamic batching of long-tail rollouts for RLHF training efficiency. / 动态批处理长尾rollout解决RLHF训练中的长尾问题。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/gao-wei) | [PDF](https://www.usenix.org/system/files/nsdi26-gao-wei.pdf)

25. **RLBoost: Harvesting Preemptible Cloud Resources for Cost-Efficient Reinforcement Learning on LLMs**
    Authors: Yongji Wu et al. | Conference: NSDI 2026 | Tags: rl-training, cost
    Cost-efficient RL training on LLMs using preemptible cloud instances. / 利用可抢占云实例进行成本高效的LLM RL训练。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wu-yongji) | [PDF](https://www.usenix.org/system/files/nsdi26-wu-yongji.pdf)

26. **DistRS: Disaggregated Reward Service for RLVR with Batch-Level Constraint**
    Authors: Ruidong Zhu et al. | Conference: NSDI 2026 | Tags: rl-training, rlvr
    Disaggregated reward computation for RL with verifiable rewards (RLVR). / 可验证奖励RL的奖励计算服务分离。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhu-ruidong) | [PDF](https://www.usenix.org/system/files/nsdi26-zhu-ruidong.pdf)

### Vector Search

27. **DistVS: Large-scale Vector Search with Compute-Memory Disaggregation**
    Authors: Yin et al. | Conference: NSDI 2026 | Tags: vector-search, rag
    Compute-memory disaggregation for large-scale vector search. / 计算与内存分离的大规模向量搜索，独立扩展索引和查询服务组件。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/yin) | [PDF](https://www.usenix.org/system/files/nsdi26-yin.pdf)

### Memory Disaggregation & RDMA

28. **BURST: Seeking High-performance, Interoperability and Scalability in Soft-RDMA**
    Authors: Shen et al. | Conference: NSDI 2026 | Tags: memory-disaggregation, rdma
    High-performance software-based RDMA with cross-implementation interoperability. / 基于软件的高性能RDMA实现，跨不同RDMA实现保持互操作性。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/shen) | [PDF](https://www.usenix.org/system/files/nsdi26-shen.pdf)

29. **SYMPHONY: Enabling Compute-Memory Disaggregation in LLM Serving Systems**
    Authors: Agarwal et al. | Conference: NSDI 2026 | Tags: llm-serving, memory-disaggregation
    Compute-memory disaggregation for LLM serving via RDMA. / 实现LLM服务的计算-内存分离，通过RDMA访问远程内存池。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/agarwal) | [PDF](https://www.usenix.org/system/files/nsdi26-agarwal.pdf)

30. **OneSidedMW: Managing Disaggregated Memory Efficiently, Flexibly, and Securely with RNIC Offloading**
    Authors: Zixuan Wang et al. | Conference: NSDI 2026 | Tags: memory-disaggregation, rdma
    RNIC-offloaded disaggregated memory management for one-sided access. / 将分离内存管理卸载到RNIC，实现无CPU参与的单侧内存访问。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wang-zixuan) | [PDF](https://www.usenix.org/system/files/nsdi26-wang-zixuan.pdf)

31. **PD3: Prefetching Data with DPUs for Disaggregated Memory**
    Authors: Sankhe et al. | Conference: NSDI 2026 | Tags: memory-disaggregation, dpu
    DPU-accelerated intelligent prefetching from disaggregated memory pools. / 使用DPU智能预取分离内存池数据，隐藏远程访问延迟。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/sankhe) | [PDF](https://www.usenix.org/system/files/nsdi26-sankhe.pdf)

### Network ML & AI Networking

32. **UNUM: A New Framework for Network Control**
    Authors: Jiayi Chen et al. | Conference: NSDI 2026 | Tags: network-ml
    Unified ML-driven network control framework replacing fragmented control-plane. / 统一的ML驱动网络控制框架，替代碎片化的控制面组件。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/chen-jiayi) | [PDF](https://www.usenix.org/system/files/nsdi26-chen-jiayi.pdf)

33. **PolicyCache: Intra-flow Learning in Congestion Control**
    Authors: Tian et al. | Conference: NSDI 2026 | Tags: network-ml, congestion-control
    Learns optimal congestion control policies within individual flows in real time. / 在单个流内实时学习最优拥塞控制策略。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/tian) | [PDF](https://www.usenix.org/system/files/nsdi26-tian.pdf)

34. **Making Logic a First-Class Citizen in Generative ML for Networking**
    Authors: He et al. | Conference: NSDI 2026 | Tags: network-ml, generative
    Incorporates logical constraints into generative ML models for networking. / 将逻辑约束和领域知识融入网络任务的生成式ML模型。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/he) | [PDF](https://www.usenix.org/system/files/nsdi26-he.pdf)

35. **Geminet: Learning the Duality-based Topology-Agnostic Update Operator for Lightweight Traffic Engineering in Changing Topologies**
    Authors: Ximeng Liu et al. | Conference: NSDI 2026 | Tags: network-ml, traffic-engineering
    Learns topology-agnostic traffic engineering using duality theory. / 基于对偶理论学习拓扑无关的流量工程算子。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/liu-ximeng) | [PDF](https://www.usenix.org/system/files/nsdi26-liu-ximeng.pdf)

36. **Matryoshka: Realizing Hyperscale Data Center Network Design for the AI Era**
    Authors: Cai et al. | Conference: NSDI 2026 | Tags: network-ml, datacenter
    Nested topology design for hyperscale AI data center networks. / 为AI训练和推理流量优化的超大规模数据中心嵌套拓扑设计。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/cai) | [PDF](https://www.usenix.org/system/files/nsdi26-cai.pdf)

37. **Arcadia: Enabling AI Network Cross-Layer Design and Operations with A Simulation Platform at Scale**
    Authors: Zhaodong Wang et al. | Conference: NSDI 2026 | Tags: network-ml, simulation
    Large-scale simulation platform for cross-layer AI network design. / 大规模仿真平台支持跨层AI网络设计。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/wang-zhaodong) | [PDF](https://www.usenix.org/system/files/nsdi26-wang-zhaodong.pdf)

38. **PrvTel: Lightweight Models for Private and Accurate Telemetry Data Retention**
    Authors: Yajie Zhou et al. | Conference: NSDI 2026 | Tags: network-ml, telemetry
    Lightweight ML models for private, accurate network telemetry. / 使用轻量ML模型实现隐私保护的网络遥测。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/zhou-yajie) | [PDF](https://www.usenix.org/system/files/nsdi26-zhou-yajie.pdf)

39. **Defeating Slow-and-Low Threats via Diffusion Model-based Generative Inference**
    Authors: Mirnajafizadeh et al. | Conference: NSDI 2026 | Tags: network-ml, security
    Diffusion model-based detection of slow-and-low network attacks. / 使用扩散模型检测低频慢速网络攻击。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/mirnajafizadeh) | [PDF](https://www.usenix.org/system/files/nsdi26-mirnajafizadeh.pdf)

### Edge ML & In-Network Inference

40. **SPLIDT: Partitioned Decision Trees for Scalable Stateful Inference at Line Rate**
    Authors: Parvez et al. | Conference: NSDI 2026 | Tags: edge-ml, in-network
    Stateful decision tree inference at line rate on programmable switches. / 在可编程交换机上实现线速状态决��树推理。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/parvez) | [PDF](https://www.usenix.org/system/files/nsdi26-parvez.pdf)

41. **FENIX: Enabling In-Network DNN Inference with FPGA-Enhanced Programmable Switches**
    Authors: Gao et al. | Conference: NSDI 2026 | Tags: edge-ml, in-network
    FPGA-enhanced programmable switches for in-network DNN inference. / 结合FPGA加速与可编程交换机的网络内DNN推理。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/gao) | [PDF](https://www.usenix.org/system/files/nsdi26-gao.pdf)

42. **Morphe: High-Fidelity Generative Video Streaming with Vision Foundation Model**
    Authors: Gong et al. | Conference: NSDI 2026 | Tags: edge-ml, video
    Vision foundation model-powered generative video streaming at the edge. / 在边缘使用视觉基础模型进行高保真生成式视频流传输。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/gong) | [PDF](https://www.usenix.org/system/files/nsdi26-gong.pdf)

43. **AVA: Towards Agentic Video Analytics with Vision Language Models**
    Authors: Yan et al. | Conference: NSDI 2026 | Tags: edge-ml, video, vlm
    Vision language model-powered agentic video analytics framework. / 视觉语言模型驱动的智能视频分析框架。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/yan) | [PDF](https://www.usenix.org/system/files/nsdi26-yan.pdf)

44. **Remembrall: Leaning into Memory for Accurate Video Analytics on System-on-Chip GPUs**
    Authors: Ramanujam et al. | Conference: NSDI 2026 | Tags: edge-ml, video
    Temporal memory leverage for accurate video analytics on power-constrained SoC GPUs. / 利用帧间时序记忆在SoC GPU上进行精确视频分析。
    [Presentation](https://www.usenix.org/conference/nsdi26/presentation/ramanujam) | [PDF](https://www.usenix.org/system/files/nsdi26-ramanujam.pdf)

---

## OSDI 2025 (18 papers)

45. **FuseLink: Enabling Efficient GPU Communication over Multiple NICs**
    Authors: Ren et al. | Conference: OSDI 2025 | Tags: gpu-communication
    Efficient GPU communication over multiple NICs with near-linear bandwidth scaling. / 在多NIC间高效复用GPU通信，实现接近线性的带宽扩展。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/ren) | [PDF](https://www.usenix.org/system/files/osdi25-ren.pdf)

46. **Quake: Adaptive Indexing for Vector Search**
    Authors: Mohoney et al. | Conference: OSDI 2025 | Tags: vector-search
    Adaptive indexing that dynamically adjusts to query patterns for faster vector search. / 自适应索引系统，根据查询模式动态调整索引结构。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/mohoney) | [PDF](https://www.usenix.org/system/files/osdi25-mohoney.pdf)

47. **Achieving Low-Latency Graph-Based Vector Search via Aligning Best-First Search Algorithm with SSD**
    Authors: Guo et al. | Conference: OSDI 2025 | Tags: vector-search, storage
    Aligns graph search with SSD access patterns for low-latency disk-based vector search. / 将图搜索算法与SSD访问模式对齐，实现基于磁盘的低延迟向量搜索。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/guo) | [PDF](https://www.usenix.org/system/files/osdi25-guo.pdf)

48. **KPerfIR: Towards an Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads**
    Authors: Guan et al. | Conference: OSDI 2025 | Tags: tensor-compiler, profiling
    Open compiler-centric GPU kernel performance profiling infrastructure. / 开放的编译器中心化GPU kernel性能分析基础设施。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/guan) | [PDF](https://www.usenix.org/system/files/osdi25-guan.pdf)

49. **Mirage: A Multi-Level Superoptimizer for Tensor Programs**
    Authors: Mengdi Wu et al. | Conference: OSDI 2025 | Tags: tensor-compiler
    Multi-level superoptimizer searching across operator, graph, and kernel levels. / 多级超级优化器，跨算子、图、kernel三级同时搜索最优张量程序实现。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/wu-mengdi) | [PDF](https://www.usenix.org/system/files/osdi25-wu-mengdi.pdf)

50. **QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach**
    Authors: Dong et al. | Conference: OSDI 2025 | Tags: tensor-compiler
    Neural-symbolic transcompilation of tensor programs between DL frameworks. / 神经-符号编译器，在不同DL框架间转换张量程序。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/dong) | [PDF](https://www.usenix.org/system/files/osdi25-dong.pdf)

51. **WaferLLM: Large Language Model Inference at Wafer Scale**
    Authors: He et al. | Conference: OSDI 2025 | Tags: llm-serving
    Wafer-scale LLM inference mapping entire model onto a single wafer. / 晶圆级LLM推理系统，将完整模型映射到单个晶圆上。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/he) | [PDF](https://www.usenix.org/system/files/osdi25-he.pdf)

52. **BlitzScale: Fast and Live Large Model Autoscaling with O(1) Host Caching**
    Authors: Dingyan Zhang et al. | Conference: OSDI 2025 | Tags: llm-serving, autoscaling
    O(1) host-level caching for live autoscaling of large model serving. / O(1)主机级缓存实现大模型服务的实时自动扩缩。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan) | [PDF](https://www.usenix.org/system/files/osdi25-zhang-dingyan.pdf)

53. **Bayesian Code Diffusion for Efficient Automatic Deep Learning Program Optimization**
    Authors: Jeong et al. | Conference: OSDI 2025 | Tags: tensor-compiler, auto-tuning
    Bayesian optimization guided by code diffusion models for DL program optimization. / 使用贝叶斯优化引导的代码扩散模型自动发现高效DL程序实现。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/jeong) | [PDF](https://www.usenix.org/system/files/osdi25-jeong.pdf)

54. **Training with Confidence: Catching Silent Errors in Deep Learning Training with Automated Proactive Checks**
    Authors: Jiang et al. | Conference: OSDI 2025 | Tags: llm-training, reliability
    Proactive error detection catching silent data corruption during DL training. / 主动错误检测系统，在DL训练中捕获静默数据损坏。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/jiang) | [PDF](https://www.usenix.org/system/files/osdi25-jiang.pdf)

55. **Neutrino: Fine-grained GPU Kernel Profiling via Programmable Probing**
    Authors: Songlin Huang et al. | Conference: OSDI 2025 | Tags: tensor-compiler, profiling
    Fine-grained GPU kernel profiler using programmable hardware probes. / 细粒度GPU kernel profiler，通过可编程硬件探针捕获逐指令性能数据。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/huang-songlin) | [PDF](https://www.usenix.org/system/files/osdi25-huang-songlin.pdf)

56. **Principles and Methodologies for Serial Performance Optimization**
    Authors: Sujin Park et al. | Conference: OSDI 2025 | Tags: tensor-compiler, optimization
    Systematic principles and methodologies for serial (single-thread) performance optimization. / 建立串行性能优化的原则和系统方法论。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/park-sujin) | [PDF](https://www.usenix.org/system/files/osdi25-park-sujin.pdf)

57. **Understanding Stragglers in Large Model Training Using What-if Analysis**
    Authors: Jinkun Lin et al. | Conference: OSDI 2025 | Tags: llm-training, analysis
    Systematic what-if analysis of straggler causes and impacts in large model training. / 系统分析大模型训练中的落后者成因和影响。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/lin-jinkun) | [PDF](https://www.usenix.org/system/files/osdi25-lin-jinkun.pdf)

58. **NanoFlow: Towards Optimal Large Language Model Serving Throughput**
    Authors: Kan Zhu et al. | Conference: OSDI 2025 | Tags: llm-serving
    Near-optimal LLM serving throughput via nano-batch level scheduling. / 通过纳级微批次细粒度请求调度实现接近最优的LLM服务吞吐。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/zhu-kan) | [PDF](https://www.usenix.org/system/files/osdi25-zhu-kan.pdf)

59. **PipeThreader: Software-Defined Pipelining for Efficient DNN Execution**
    Authors: Cheng et al. | Conference: OSDI 2025 | Tags: tensor-compiler, gpu
    Software-defined pipeline execution overlapping computation and communication. / 软件定义流水线执行框架，自动重叠DNN负载的计算与通信。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/cheng) | [PDF](https://www.usenix.org/system/files/osdi25-cheng.pdf)

60. **WLB-LLM: Workload-Balanced 4D Parallelism for Large Language Model Training**
    Authors: Zheng Wang et al. | Conference: OSDI 2025 | Tags: llm-training, parallelism
    Workload-balanced 4D parallelism for LLM training with dynamic rebalancing. / 负载均衡的4D并行训练策略，动态重均衡。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/wang-zheng) | [PDF](https://www.usenix.org/system/files/osdi25-wang-zheng.pdf)

61. **DecDEC: A Systems Approach to Advancing Low-Bit LLM Quantization**
    Authors: Yeonhong Park et al. | Conference: OSDI 2025 | Tags: llm-serving, quantization
    Systems-level framework for low-bit LLM quantization with hardware-aware kernel design. / 系统级框架通过量化-反量化流水线与硬件感知kernel设计联动，推进低比特LLM量化。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/park-yeonhong) | [PDF](https://www.usenix.org/system/files/osdi25-park-yeonhong.pdf)

62. **Compass: Encrypted Semantic Search with High Accuracy**
    Authors: Jinhao Zhu et al. | Conference: OSDI 2025 | Tags: vector-search, privacy
    Encrypted semantic search achieving high accuracy while preserving data privacy. / 加密语义搜索系统，在保护数据隐私的同时实现高精度向量搜索。
    [Presentation](https://www.usenix.org/conference/osdi25/presentation/zhu-jinhao) | [PDF](https://www.usenix.org/system/files/osdi25-zhu-jinhao.pdf)

---

## RDMA & Datacenter Networking (6 papers)

63. **HPCC: High Precision Congestion Control**
    Authors: Li et al. | Conference: SIGCOMM | Tags: memory-disaggregation, congestion-control, rdma
    High-precision congestion control using in-network telemetry for RDMA networks. / 利用网内遥测实现RDMA网络高精度拥塞控制。
    [PDF](https://dl.acm.org/doi/10.1145/3387514.3405895)

64. **TIMELY: RTT-based Congestion Control for the Datacenter**
    Authors: Mittal et al. | Conference: SIGCOMM | Tags: memory-disaggregation, congestion-control, rdma
    RTT-based congestion control using round-trip time for faster congestion signals. / 基于RTT的RDMA数据中心拥塞控制，使用往返时间测量替代ECN标记。
    [PDF](https://dl.acm.org/doi/10.1145/2785956.2787510)

65. **Swift: Delay is Simple and Effective for Congestion Control in the Datacenter**
    Authors: Kumar et al. | Conference: SIGCOMM | Tags: memory-disaggregation, congestion-control, rdma
    Simple delay-based congestion control achieving high throughput and low latency. / 简单的延迟拥塞控制在RDMA网络中高效易实现。
    [PDF](https://dl.acm.org/doi/10.1145/3387514.3406591)

66. **SwCC: Software-Programmable and Per-Packet Congestion Control in RDMA Engine**
    Authors: Authors et al. | Conference: APNet | Tags: memory-disaggregation, congestion-control, rdma
    Software-programmable per-packet congestion control for RDMA NICs. / RDMA网卡上的软件可编程拥塞控制框架。
    [PDF](https://www.usenix.org/system/files/nsdi26-sankhe.pdf)

67. **APNet: Application-Centric Networking**
    Authors: Authors et al. | Conference: APNet 2026 | Tags: network-ml
    Application-centric networking approach for better network-application co-design. / 应用为中心的网络方法，实现更好的网络-应用协同设计。

68. **RDMA Performance and Optimization**
    Authors: Authors et al. | Tags: memory-disaggregation, rdma
    Advances in RDMA performance optimization and congestion management. / RDMA性能优化与拥塞管理的最新进展。
    [PDF](https://dl.acm.org/doi/10.1145/2829988.2787484)

---

## Category Index / 分类索引

| Category | Papers | Key Conferences |
|---|---|---|
| llm-serving | 15 | NSDI 2026, OSDI 2025 |
| llm-training | 12 | NSDI 2026, OSDI 2025 |
| gpu-communication | 5 | NSDI 2026, OSDI 2025 |
| tensor-compiler | 7 | OSDI 2025 |
| vector-search | 4 | NSDI 2026, OSDI 2025 |
| network-ml | 9 | NSDI 2026 |
| edge-ml | 5 | NSDI 2026 |
| rl-training | 3 | NSDI 2026 |
| memory-disaggregation | 10 | NSDI 2026, SIGCOMM, APNet |
