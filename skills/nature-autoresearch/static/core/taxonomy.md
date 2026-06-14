# Taxonomy: nature-autoresearch

## 工具类别定义 / Tool Category Definitions

本技能将 awesome-autoresearch 目录中的 85+ 个工具按以下 6 个类别组织：

The 85+ tools in the awesome-autoresearch catalog are organized into 6 categories:

### 1. general-purpose (通用自主改进循环 / General-Purpose Descendants)
直接基于 `karpathy/autoresearch` 模式推广的通用自主改进循环工具。核心特征是 "propose → evaluate → keep-or-revert" 循环，可应用于任何可量化的优化目标。

Direct descendants of `karpathy/autoresearch` that generalize the autonomous improvement loop. Core pattern: propose → evaluate → keep-or-revert, applicable to any measurable optimization goal.

**典型场景**：代码优化、模型调参、prompt 进化、自动化测试
**Typical use**: code optimization, model tuning, prompt evolution, automated testing

### 2. research-agent (科研智能体系统 / Research-Agent Systems)
全流程科研自动化系统，覆盖 idea 生成 → 文献综述 → 实验 → 论文写作 → 审稿 的完整科研生命周期。

End-to-end research automation systems covering the full research lifecycle: idea generation → literature review → experimentation → paper writing → peer review.

**典型场景**：AI自动写论文、自动做ML研究、自动文献综述
**Typical use**: AI paper writing, automated ML research, automated literature review

### 3. platform-port (平台移植和硬件分支 / Platform Ports & Hardware Forks)
将 autoresearch 适配到不同硬件/平台的移植版本。

Ports that adapt autoresearch to different hardware/platforms.

**典型场景**：在 Mac/Windows/WebGPU/Jetson 上运行自主实验
**Typical use**: running autonomous experiments on Mac/Windows/WebGPU/Jetson

### 4. domain-specific (领域定制适配 / Domain-Specific Adaptations)
将自主改进循环应用于特定领域（非ML研究）的定制版本。

Custom adaptations applying the autonomous improvement loop to specific non-ML domains.

**典型场景**：语音AI优化、交易策略、GPU kernel调优、家谱研究
**Typical use**: voice AI optimization, trading strategies, GPU kernel tuning, genealogy

### 5. benchmark (评估和基准测试 / Evaluation & Benchmarks)
评估 AI 智能体在科研任务上表现的基准测试套件。

Benchmark suites for evaluating AI agent performance on research tasks.

**典型场景**：评估你的智能体能做多好的ML研究
**Typical use**: evaluating how well your agent performs ML research

### 6. use-case (知名应用案例和文章 / Notable Use Cases & Writeups)
autoresearch 在真实世界中的成功应用案例和相关深度文章。

Real-world success cases and in-depth writeups of autoresearch in action.

**典型场景**：了解其他人用autoresearch做了什么
**Typical use**: learning what others have done with autoresearch

## 概念定义 / Concept Definitions

### Autoresearch Loop (自主改进循环)
由 Andrej Karpathy 提出的一种 AI 自我改进模式：
1. AI 提出改进方案（propose）
2. 自动运行评估（evaluate）
3. 保留好结果，回退坏结果（keep-or-revert）
4. 将经验和结果写入实验日志（log）
5. 在下一轮迭代中参考之前的经验（learn）

### MoltFounders (AI 智能体协作维护)
一种开源工作模式，通过 `.moltfounders/` 目录中的规则文件定义 AI 智能体如何自动维护 GitHub 仓库，包括：
- Issue 分类和打标签
- PR 审查和批准
- 新资源发现和添加
- 过期条目清理

## 研究方向定义 / Research Topic Definitions

本技能将 68 篇顶会论文（NSDI 2026: 44篇, OSDI 2025: 18篇, RDMA相关: 6篇）按以下 9 个研究方向组织：

68 papers from top conferences (NSDI 2026: 44, OSDI 2025: 18, RDMA-related: 6) are organized into 9 research topics:

### 1. llm-serving (LLM推理与服务 / LLM Serving & Inference)
LLM推理系统优化，包括调度（FastServe, NanoFlow）、KV缓存管理（DroidSpeak）、自动扩缩（BlitzScale, HydraServe）、服务质量（JITServe, Libra）、智能体服务（Agentix, Cortex）和量化（DecDEC）。

LLM inference system optimization covering scheduling, KV cache management, autoscaling, SLO guarantees, agent serving, and quantization.

### 2. llm-training (大模型训练 / LLM Training)
LLM分布式训练系统，包括检查点（Checkmate）、跨集群训练（Di-PS）、训练诊断（FLARE, EROICA）、流水线并行（Attack of the Bubbles）、微调复用（MuxTune）、存储优化（ZipLLM）、仿真（Supercharging, Phantora）和4D并行（WLB-LLM）。

Distributed LLM training systems covering checkpointing, cross-cluster training, diagnosis, pipeline parallelism, fine-tuning, storage optimization, simulation, and 4D parallelism.

### 3. gpu-communication (GPU通信 / GPU Communication)
GPU间通信与集合操作优化，包括MoE通信（SwiftEP, FAST）、异构网络（ForestColl, HeteCCL）和多NIC（FuseLink）。

GPU-to-GPU communication and collective operation optimization covering MoE communication, heterogeneous networks, and multi-NIC transport.

### 4. tensor-compiler (张量编译器 / Tensor Compiler)
张量程序编译器与优化框架，包括超级优化（Mirage）、跨框架编译（QiMeng-Xpiler）、自动调优（Bayesian Code Diffusion）、profiling工具（KPerfIR, Neutrino）和流水线执行（PipeThreader）。

Tensor program compiler and optimization frameworks covering superoptimization, cross-framework compilation, auto-tuning, profiling tooling, and pipelined execution.

### 5. vector-search (向量搜索 / Vector Search)
向量搜索引擎与RAG基础设施，包括资源分离（DistVS）、自适应索引（Quake）、SSD对齐（Achieving Low-Latency）和加密搜索（Compass）。

Vector search engines and RAG infrastructure covering resource disaggregation, adaptive indexing, SSD-aligned search, and encrypted search.

### 6. network-ml (网络ML / Network ML)
面向网络系统的ML应用和面向AI的网络基础设施，包括网络控制（UNUM）、拥塞控制（PolicyCache）、流量工程（Geminet）、生成式ML网络（Making Logic）、集群设计（Matryoshka）、仿真（Arcadia）和遥测（PrvTel）。

ML applications for networking and AI-optimized network infrastructure covering network control, congestion control, traffic engineering, generative ML, cluster design, simulation, and telemetry.

### 7. edge-ml (边缘ML / Edge ML)
边缘推理与网络内ML，包括交换机内推理（SPLIDT, FENIX）、视频分析（AVA, Remembrall）和视频流（Morphe）。

Edge inference and in-network ML covering in-switch inference, video analytics, and generative video streaming.

### 8. rl-training (RL训练 / RL Training)
LLM强化学习训练基础设施（RLHF/RLVR），包括rollout管理（RollPacker）、资源利用（RLBoost）和奖励服务分离（DistRS）。

RL training infrastructure for LLM post-training (RLHF/RLVR) covering rollout management, resource harvesting, and reward service disaggregation.

### 9. memory-disaggregation (内存分离 / Memory Disaggregation)
数据中心内存分离与RDMA系统，包括软件RDMA（BURST）、LLM服务内存分离（SYMPHONY）、RNIC卸载（OneSidedMW）、DPU预取（PD3）和RDMA拥塞控制（HPCC, TIMELY, Swift, SwCC）。

Datacenter memory disaggregation and RDMA systems covering soft-RDMA, LLM memory disaggregation, RNIC offloading, DPU prefetching, and RDMA congestion control.
