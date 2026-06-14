# Tensor Compilers & Program Optimization / 张量编译器与程序优化

Systems research on compiler frameworks for tensor programs, GPU kernel optimization, and automated deep learning program tuning. Covers superoptimization, neural-symbolic compilation, profiling tooling, and automatic code generation.

For full paper details, see `references/paper-catalog.md`.

## 论文列表 / Paper List

1. **KPerfIR: Towards an Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads** [OSDI 2025]
   Open compiler-centric infrastructure for GPU kernel performance profiling and analysis, providing unified tooling across different GPU hardware and AI frameworks. / 开放的编译器中心化GPU kernel性能分析与profiling基础设施，跨GPU硬件和AI框架统一工具。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/guan) | [PDF](https://www.usenix.org/system/files/osdi25-guan.pdf)

2. **Mirage: A Multi-Level Superoptimizer for Tensor Programs** [OSDI 2025]
   Multi-level superoptimizer that automatically discovers optimal tensor program implementations by searching across operator, graph, and kernel levels simultaneously. / 多级超级优化器，跨算子、图、kernel三级同时搜索最优张量程序实现。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/wu-mengdi) | [PDF](https://www.usenix.org/system/files/osdi25-wu-mengdi.pdf)

3. **QiMeng-Xpiler: Transcompiling Tensor Programs for Deep Learning Systems with a Neural-Symbolic Approach** [OSDI 2025]
   Neural-symbolic compiler that transcompiles tensor programs between different DL frameworks (PyTorch, JAX, TensorFlow), combining learned patterns with symbolic reasoning. / 神经-符号编译器，结合学习模式与符号推理，在不同DL框架间转换张量程序。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/dong) | [PDF](https://www.usenix.org/system/files/osdi25-dong.pdf)

4. **Bayesian Code Diffusion for Efficient Automatic Deep Learning Program Optimization** [OSDI 2025]
   Uses Bayesian optimization guided by code diffusion models to automatically discover efficient DL program implementations, reducing search cost vs. exhaustive auto-tuning. / 使用贝叶斯优化引导的代码扩散模型自动发现高效DL程序实现，降低搜索成本。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/jeong) | [PDF](https://www.usenix.org/system/files/osdi25-jeong.pdf)

5. **Neutrino: Fine-grained GPU Kernel Profiling via Programmable Probing** [OSDI 2025]
   Fine-grained GPU kernel profiler that uses programmable hardware probes to capture per-instruction performance data without modifying kernel source code. / 细粒度GPU kernel profiler，通过可编程硬件探针捕获逐指令性能数据，无需修改kernel源码。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/huang-songlin) | [PDF](https://www.usenix.org/system/files/osdi25-huang-songlin.pdf)

6. **PipeThreader: Software-Defined Pipelining for Efficient DNN Execution** [OSDI 2025]
   Software-defined pipeline execution framework for DNN workloads that automatically overlaps computation and communication across GPU streams for maximal utilization. / 软件定义流水线执行框架，自动重叠DNN负载的计算与通信以最大化GPU利用率。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/cheng) | [PDF](https://www.usenix.org/system/files/osdi25-cheng.pdf)

7. **Principles and Methodologies for Serial Performance Optimization** [OSDI 2025]
   Establishes principles and systematic methodologies for optimizing serial (single-thread) performance, applicable to compiler backends and kernel implementations. / 建立串行性能优化的原则和系统方法论，适用于编译器后端和kernel实现。
   [Presentation](https://www.usenix.org/conference/osdi25/presentation/park-sujin) | [PDF](https://www.usenix.org/system/files/osdi25-park-sujin.pdf)

## 实验指导 / Experiment Guide

### 典型实验配置 / Typical Setup
- **Hardware**: NVIDIA H100/A100 GPU, CUDA ≥12.0
- **Models**: LLaMA-3-8B, GPT-3-7B, Chameleon-7B, nGPT-1B (Tranformer变体越多越好)
- **Frameworks**: PyTorch 2.x, TensorRT, XLA
- **Search time budget**: Mirage paper: 11-28 sec for RMSNorm (10 ops) on single GPU

### 常用指标 / Common Metrics
| Metric | 用途 | Papers |
|--------|------|--------|
| **Per-iteration Latency (ms)** | 单次kernel执行延迟 | Mirage (LLaMA-3: 1.4x vs PyTorch) |
| **Search/Compilation Time (s)** | 优化搜索耗时 | Mirage (11-28 sec for RMSNorm), Bayesian Code Diffusion |
| **Speedup over Baselines** | 相对加速比 | All papers |
| **Kernel-level Metrics** (occupancy, bandwidth util.) | GPU微架构级profiling | Neutrino, KPerfIR |
| **Cross-framework Accuracy** | 跨框架转换正确性 | QiMeng-Xpiler |

### 常用Baseline / Common Baselines
- **PyTorch eager mode**: 最基础的baseline
- **PyTorch compile (torch.compile)**: PyTorch 2.x 内置编译器
- **TensorRT**: NVIDIA 官方推理优化引擎
- **XLA**: Google/OpenXLA 编译器
- **TVM / Halide**: 传统张量编译器

### 实验常见坑 / Common Pitfalls
- **Warmup很重要**: GPU kernel首次启动有JIT编译开销，需先warmup多次再测量。Mirage和PyTorch编译器的warmup行为不同，公平对比需要统一warmup策略。
- **batch size敏感性**: 小batch (BS=1)和大batch (BS=16)的kernel优化策略完全不同; 好的实验应覆盖多个BS。
- **搜索时间 vs 执行收益**: 编译器优化论文需要同时报告搜索时间和执行加速。仅报告加速而忽略搜索开销不公平。
- **Shared memory overhead**: GPU shared memory读写对小计算量kernel反而是负担 (Mirage论文明确指出的limitation), 对lightweight ops可能不如原版快。

## 评估与洞察 / Evaluation & Insights

### 类别级评价 / Category-Level Assessment

Tensor compiler research in 2025 reflects a convergence of compilers and ML: search-based superoptimization (Mirage), neural-symbolic compilation (QiMeng-Xpiler), and ML-guided search (Bayesian Code Diffusion). Key trends:

- **Superoptimization over pattern-matching**: Mirage challenges the template-matching paradigm (TensorRT, XLA) by searching for optimal fused kernels across multiple abstraction levels simultaneously—discovering optimizations human compiler writers miss.
- **Profiling infrastructure as research**: KPerfIR and Neutrino address the fundamental problem that GPU kernel optimization is bottlenecked by profiling tooling, not compilation technique. Better profiling enables better compilation.
- **From auto-tuning to auto-generation**: Bayesian Code Diffusion and QiMeng-Xpiler use generative models (diffusion, neural-symbolic) to produce optimized code, moving beyond parameter search to code synthesis.

### 论文亮点与局限 / Paper Highlights & Limitations

**Mirage** — First multi-level superoptimizer for tensor programs. µGraph representation unifies kernel/thread-block/thread levels. 1.4× speedup on LLaMA-3-8B, GPT-3, Chameleon vs heavily-optimized baselines. Auto-discovers fused kernels of up to 11 operations (µGraphs). Probabilistic equivalence verification (Pr(error) < 10^-12). Search time: 11-28 seconds. **Limitation**: Shared memory contention limits gains for lightweight compute kernels. Search space heavily pruned; certain novel optimizations may be missed by the abstraction-based pruning. Currently targets single-GPU optimizations.

**KPerfIR** — Open compiler-centric GPU kernel profiling ecosystem. Addresses vendor tooling fragmentation (Nsight, ROCProf, etc.) with a unified IR-level approach. **Limitation**: Requires compiler IR instrumentation; profiling fidelity depends on IR-to-binary mapping accuracy.

**Neutrino** — Hardware-level programmable probing for per-instruction GPU kernel profiling without source modification. **Limitation**: Probing overhead may distort very short kernel measurements; hardware dependency limits portability.

**Bayesian Code Diffusion** — Code diffusion models guided by Bayesian optimization reduce auto-tuning cost vs exhaustive search. **Limitation**: Diffusion model training cost amortizes only when optimizing many similar programs. Generated code quality depends on training data diversity.

**QiMeng-Xpiler** — Neural-symbolic transcompilation between PyTorch/JAX/TensorFlow. Combines learned patterns with symbolic reasoning for correctness guarantees. **Limitation**: Framework-specific semantics can cause edge cases; accuracy degrades for framework-specific features with no cross-framework equivalent.

### 实用建议 / Practical Guidance

- **DNN inference optimization**: Mirage for production DNN deployments—the 1.4× speedup and 11-28 sec search time make it practical per-deployment
- **GPU kernel debugging**: KPerfIR for understanding which kernels are bottlenecked; Neutrino for diagnosing why specific kernels are slow
- **Auto-tuning**: Bayesian Code Diffusion when optimizing many similar tensor programs (model families); QiMeng-Xpiler for multi-framework codebases
- **Pipeline overlap**: PipeThreader for maximizing GPU utilization through automated computation-communication overlap

## 写作指导 / Writing Guide

- **贡献公式**: "A [方法] that [做什么] at the [什么粒度] level, achieving [X speedup] on [哪些模型]"
- **Motivation**: 展示"human-written kernel" vs "auto-generated kernel"的性能差距（用profiling tool数据）
- **Evaluation必须**: (1) end-to-end模型延迟 (2) single-operator micro-benchmark (3) 搜索/编译时间 (4) 与其他编译器的对比 (5) ablation on优化粒度

## 实现指导 / Implementation Guide

- **Mirage模式**: µGraph builder (Python) + Search engine (C++) + Kernel generator (CUDA), 约10K-15K LOC
- **Profiling集成** (KPerfIR/Neutrino): GPU硬件计数器读取 + IR插桩
- **Diffusion优化** (Bayesian Code Diffusion): pretrained code diffusion model + Bayesian search loop
- **关键**: 等价性验证 (randomized testing > 10^6 inputs)

## 实验流程 / Experiment Pipeline

```
1. Kernel Benchmark (single operator)
   ├── 操作: MatMul, Attention, LayerNorm, RMSNorm, GELU
   ├── Shape: (M=1..2048, N=K=4096), 实际模型shapes
   ├── 对比: PyTorch eager / torch.compile / TensorRT / 你的系统
   └── 指标: latency (µs), 搜索时间 (s), speedup ratio

2. End-to-End Benchmark
   ├── 模型: LLaMA-3-8B, GPT-3-7B, Chameleon-7B
   ├── Batch size: 1, 4, 8, 16
   ├── 指标: per-iteration latency (ms)
   └── 对比: 至少3个baselines

3. Ablation
   ├── 逐步关闭优化 (每级abstraction一个)
   ├── 分析每个优化的独立贡献
   └── 报告搜索overhead vs 执行收益
```

## 写作指导 / Writing Guide
- **贡献公式**: "A [方法] that [做什么] at the [什么粒度] level, achieving [X speedup] on [哪些模型]"
- **Evaluation必须**: (1) end-to-end模型延迟 (2) single-operator micro-benchmark (3) 搜索/编译时间 (4) 与其他编译器对比 (5) ablation on优化粒度

## 实现指导 / Implementation Guide
- **Mirage模式**: µGraph builder (Python) + Search engine (C++) + Kernel generator (CUDA), ~10-15K LOC
- **Profiling**: GPU硬件计数器读取 + IR插桩 (KPerfIR/Neutrino)
- **关键**: 等价性验证 (randomized testing > 10^6 inputs)

## 实验流程 / Experiment Pipeline
```
1. 单算子bench → 多种shape (M=1..2048, N=K=4096)
2. 端到端bench → LLaMA-3/GPT-3/Chameleon, BS=1/4/8/16
3. Ablation → 逐级关闭优化, 分析独立贡献
```

## 注意事项 / Notes

- Tensor compiler research is converging with ML-for-compilers approaches (QiMeng-Xpiler, Bayesian Code Diffusion).
- Profiling tooling (KPerfIR, Neutrino) is essential for understanding GPU kernel bottlenecks before applying compiler optimizations.
- Mirage and PipeThreader represent the cutting edge of automated tensor program optimization.
- 查看 `references/paper-catalog.md` 获取完整论文目录，包括作者和详细标签。
