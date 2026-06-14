# 系统论文写作指南 / Systems Paper Writing Guide

基于 NSDI 2026 和 OSDI 2025 68篇系统论文的结构分析，总结系统论文的写作方法论和常见模式。

Writing methodology and common patterns extracted from 68 systems papers at NSDI 2026 and OSDI 2025.

---

## 1. 论文整体结构 / Overall Paper Structure

标准系统论文（NSDI/OSDI）的典型结构（12-14页）：

```
1. Abstract                        (~200 words)
2. Introduction                     (1-1.5 pages)
3. Background / Motivation          (1-2 pages)
4. Design                           (3-4 pages)
5. Implementation                   (1-1.5 pages)
6. Evaluation                       (3-5 pages)
7. Related Work                     (1 page)
8. Discussion / Limitations         (0.5 page)
9. Conclusion                       (0.5 page)
Acknowledgments
References
```

**关键原则**: Evaluation是系统论文的灵魂。没有扎实的Evaluation，再好的Design也无法被接收。

---

## 2. Abstract 写作 / Abstract Writing

### 标准模板（6句法）

| 句子 | 功能 | 示例来源 |
|------|------|---------|
| S1 | 问题背景 + 为什么重要 | "LLMs result in surging demand for planet-scale serving systems" (NanoFlow) |
| S2 | 现有方案的不足 | "Existing serving engines fall short from optimal compute utilization" (NanoFlow) |
| S3 | 你的核心洞察/发现 | "We show that despite memory-intensive components, end-to-end LLM serving is compute bound" (NanoFlow) |
| S4 | 你的方案（带系统名） | "We propose NanoFlow, a novel serving framework that exploits intra-device parallelism" (NanoFlow) |
| S5 | 关键结果（具体数字） | "1.91× throughput boost, 50-72% of optimal throughput" (NanoFlow) |
| S6 | 实现规模（可选） | "~10K lines CUDA + ~6K lines Python" (NanoFlow) |

### 常见模式

**Pattern A: 推翻假设型** (NanoFlow, FLARE)
- S1: 现有假设 → S2: 我们证明假设不成立 → S3: 基于新认识提出方案
- 示例: "LLM serving is commonly assumed to be memory-bound. We show it's actually compute-bound."

**Pattern B: 新硬件/新场景型** (FuseLink, ForestColl)
- S1: 新硬件/场景出现 → S2: 现有方案不适配 → S3: 我们的适配方案
- 示例: "Multi-NIC GPUs become standard. Existing NCCL only uses one NIC."

**Pattern C: 新问题型** (FLARE, Training with Confidence)
- S1: 出现一个新问题 → S2: 现有工具无法解决 → S3: 我们的诊断/检测方案
- 示例: "LLM training at 1000+ GPU scale has divergent failures. No tool exists to diagnose them."

---

## 3. Introduction 写作 / Introduction Writing

### 标准流程（5段法）

**段1: 宏观背景 + 问题陈述** (0.5页)

用1-2句建立大背景，然后快速收敛到具体问题。

示例（NanoFlow）:
- 段1-2: "LLMs power chatbots, search engines, office software... 200M+ weekly ChatGPT users" → 建立重要性
- 段3: 引用具体数字证明规模: "API usage doubling after GPT-4o Mini release" → 量化问题

**段2: 现有方案的不足** (0.3页)

- 指出gap: "However, in practice, we find LLM serving engines are far from optimal"
- 解释gap的root cause: "because heterogeneous operations are executed sequentially"

**段3: 你的核心洞察** (0.3页)

- 这是Introduction中最关键的部分
- 要展示你发现了什么别人没发现的事
- 示例（NanoFlow）: "We show that despite memory-intensive attention, end-to-end LLM serving is compute-bound"
- 示例（SYMPHONY）: "We observe that KV cache consumption is the dominant factor limiting deployment density"

**段4: 你的方案** (0.4页)

- 系统名 + 核心机制
- 列出2-3个关键设计决策
- 模板: "We propose [SYSTEM], which [核心机制]. [SYSTEM] does X by doing Y. [SYSTEM] also does Z."

**段5: 贡献列表 + 关键结果** (0.3页)

- 使用"In summary, we contribute the following:" 或 "We make the following contributions:"
- 3-4个贡献点，每个用一句话
- 最后一定要嵌入关键数字

### 常见错误

| 错误 | 正确做法 |
|------|---------|
| Introduction太长（>2页） | 控制在1.5页以内，详细分析放在Background |
| 贡献点写成feature list | 贡献 = 新知识，不是 "we built a system" |
| 没有在Introduction里给关键数字 | 必须有1-2个关键结果数字（审稿人只看Abstract+Introduction） |
| 先描述自己的系统再描述问题 | 问题 → 洞察 → 方案 的顺序不能乱 |

---

## 4. Background / Motivation 写作

### 写作目标
- 给审稿人建立必要的技术背景
- 用数据和分析建立问题的严重性和紧迫性
- 最好包含一个 **cost model** 或 **分析框架**

### 常见模式

**Pattern A: 数据驱动的动机分析** (NanoFlow风格)
- 建立cost model ($3.2: Cost Model of LLM Serving)
- 用model对实际workload分类 ($3.3: Classification)
- 用实验验证model ($3.4: Validation)
- 用分析解释gap ($3.6: Gap to Optimal)

**Pattern B: 问题驱动的诊断** (FLARE风格)
- 描述生产环境的真实问题
- 展示现有工具为什么不work
- 用真实failure case说明

**Pattern C: 硬件特征驱动** (FuseLink风格)
- 描述新硬件的特征（多NIC、异构GPU）
- 分析为什么现有软件无法利用新特征
- 建立性能模型

### 关键技巧
- Background里最好有一个 **Figure 2/3** 级别的分析图
- 用表格展示硬件特征（参见NanoFlow的Table 1: accelerator characteristics）
- 如果可能，给出一个简洁的数学模型

---

## 5. Design 写作 / Design Writing

### 结构模板

```
4. Design
  4.1 Overview (0.5页) — 系统全景图 + 设计原则
  4.2 核心机制1 (1-1.5页)
  4.3 核心机制2 (1-1.5页)
  4.4 核心机制3 (0.5-1页)
```

### 核心原则

1. **先画架构图**: Design section的第一件事是放一张architecture diagram (Figure 3/4级别)
2. **一个设计决策 = 一个子节**: 每个关键设计决策单独成节
3. **Each decision has a justification**: 不要只说"我们用了X"，要说"我们用了X因为Y"
4. **Complexity is in the algorithm, not the description**: 用伪代码或MILP公式表示复杂逻辑

### 常见设计决策类型

| 类型 | 示例 | Paper |
|------|------|-------|
| 资源分配优化 | GPU资源分配 (R) | NanoFlow (MILP) |
| 调度算法 | Skip-Join MLFQ | FastServe |
| 数据结构设计 | µGraph representation | Mirage |
| 通信模式 | P2P flow scheduling | FuseLink |
| 缓存策略 | Advisory prefetching | SYMPHONY |

### 示例：优秀Design section结构 (NanoFlow)

```
4. Design
  4.1 Automated Pipeline Search
    4.1.1 Kernel Profiling and Interference Modeling
    4.1.2 Auto-search Stage I: Pipeline Structure Search
    4.1.3 Auto-search Stage II: Refining the Pipeline
    4.1.4 Example Pipelines (展示生成结果)
  4.2 NanoFlow Runtime
    4.2.1 Request Scheduling
    4.2.2 KV-cache Management
```

**为什么这个结构好**:
- 4.1讲"如何生成最优pipeline" (offline/compile-time)
- 4.2讲"如何执行pipeline" (online/runtime)
- 两者有清晰的boundary
- 4.1.4用具体例子让抽象算法变得具体

---

## 6. Implementation 写作 / Implementation Writing

### 标准模板

```
[System] consists of ~X lines of [language1] and ~Y lines of [language2].
Key implementation choices:
- [Infrastructure choice and why]
- [Library/framework dependency]
- [Hardware-specific optimizations]
```

### 论文中的实现信息提取

| Paper | 代码量 | 语言 | 关键依赖 |
|-------|--------|------|---------|
| NanoFlow | ~10K CUDA + ~6K Python | CUDA, Python | CUTLASS, PyTorch |
| FuseLink | ~3000 LOC | C++ | NCCL plugin API |
| SYMPHONY | N/A | Python | vLLM, RDMA |
| Mirage | N/A | C++/Python | CUDA, PyTorch |

### 注要点
- Implementation节不需要太长（1-1.5页），但要足够具体让人能复现
- 必须列出系统对硬件的依赖和要求
- 如果修改了开源项目，要说明修改了多少、在哪一层

---

## 7. Evaluation 写作 / Evaluation Writing

这是系统论文最重要的部分，占3-5页，必须回答以下问题：

### 必须回答的问题

| 问题 | 对应小节 | 示例Paper |
|------|---------|----------|
| 相比现有方案提升了多少？ | Overall comparison | NanoFlow (6.2) |
| 在不同负载下表现如何？ | Diverse workloads | NanoFlow (6.2b) |
| 延迟分布是怎样的（不只是平均）？ | Latency distribution | NanoFlow (6.3) |
| 各组件各自贡献了多少？ | Ablation study | NanoFlow (6.4) |
| 资源使用率是多少？ | Resource utilization | NanoFlow (6.5) |
| 其他模型/硬件上也能work吗？ | Generalization | NanoFlow (6.6) |

### 标准Evaluation结构

```
6. Evaluation
  6.1 Experiment Setup
    - Hardware (GPU型号、网络、内存)
    - Models (模型名、参数规模)
    - Baselines (为什么选这些baseline)
    - Datasets/Workloads
    - Metrics
  6.2 Overall Performance (End-to-end throughput/latency)
  6.3 Latency Analysis / SLO Attainment
  6.4 Ablation Study / Micro-benchmarks
  6.5 Resource Utilization / Scalability
  6.6 Generalization (other models/hardware/workloads)
```

### Experiment Setup Checklist

- Hardware: GPU型号、NVLink版本、NIC型号和数量、CPU型号
- Software: CUDA版本、驱动版本、框架版本（记录commit hash）
- Models: 尺寸、精度（FP16/BF16/INT8）、并行策略(TP/PP)
- Baselines: 名称+版本+为什么选它（最广泛使用/最新/最强）
- Workloads: 来源(trace/dataset/synthetic)、分布特征(平均+标准差)
- Metrics: 定义清晰，区分primary metrics和secondary metrics

### 关键原则

1. **用实际负载测试**: 不要只用synthetic workload。好坏系统在真实负载下差距更大。
2. **报告分布，不只是average**: P50/P95/P99 + 平均值。Tail latency往往是最重要的。
3. **Ablation是信任的基础**: 审稿人从ablation判断你的claim是否站得住。
4. **展示limitations**: 最好在evaluation里包含negative results或limitation讨论。
5. **与理论最优对比**: 如果可能（如NanoFlow计算了optimal throughput），建立上限参考。

---

## 8. Related Work 写作

### 不要做的事
- 不要按时间顺序罗列论文
- 不要只是摘要每篇论文
- 不要在related work里批评别人

### 应该做的事
- 按主题分组 (by topic/cluster)
- 每组: 现有工作做了什么 → 与你的差异是什么
- 句式模板: "Unlike [existing work], which does X, our system does Y because Z."

---

## 9. 图表制作 / Figures and Tables

### 常见图表类型

| 图类型 | 用途 | 示例 |
|--------|------|------|
| Architecture Diagram | Design section开头 | NanoFlow Fig4, Fig6 |
| Problem Illustration | Motivation/Background | NanoFlow Fig1 (Transformer架构标注) |
| Analytical Figure | Cost model验证 | NanoFlow Fig2/Fig3 (热力图) |
| Performance Bar Chart | 方案对比 | NanoFlow Fig7 |
| Latency CDF | 延迟分布 | FastServe |
| Ablation Bar/Breakdown | 消融实验 | NanoFlow Fig8 |
| Scalability Line Chart | 扩展性 | FuseLink |
| Table: Experiment Setup | 配置参数 | NanoFlow Table1 |

### 图表原则
- 每个Figure必须在正文中被引用和解释
- 图表标题应该描述 "what you see" + "what it means"
- 颜色和标记要有明确图例
- 使用一致的视觉风格

---

## 10. 常见审稿意见及预防 / Common Reviewer Comments

| 常见负面评价 | 如何预防 |
|-------------|---------|
| "Evaluation不够全面" | 覆盖diverse workloads + multiple models + 多种hardware |
| "只是engineering，没有research contribution" | 明确定义insight是什么，design decisions背后的原理 |
| "Baseline选择不公平" | 选择最强的开源baseline，公平地tune它们 |
| "没有跟最新工作比较" | 引用并对比arxiv上最新的相关工作（即使是preprint） |
| "没有讨论limitations" | 专门有一节讨论limitations，诚实展示negative results |
| "没有开源代码" | 尽量开源（NSDI/OSDI越来越要求artifact evaluation） |
| "只在自己的硬件上work" | 展示generalization：不同GPU/不同云/不同模型 |
| "实验只跑了一次" | 报告error bar/standard deviation + 重复次数 |

---

## 11. 写作检查清单 / Writing Checklist

提交前自检：

**Introduction**
- [ ] 第一段就让人知道这篇论文要解决什么问题
- [ ] 明确陈述了核心洞察（insight）
- [ ] 贡献列表不超过4个
- [ ] 有具体的提升数字（不要只说"显著提升"）

**Design**
- [ ] 有architecture diagram
- [ ] 每个设计决策有justification（不只是一个选择）
- [ ] 复杂度高的部分有伪代码/公式
- [ ] 读者能理解系统是如何工作的

**Implementation**
- [ ] 列出了代码规模
- [ ] 列出了硬件/软件依赖
- [ ] 说明了修改了哪些开源组件

**Evaluation**
- [ ] 所有claim都有实验数据支撑
- [ ] 有end-to-end + micro-benchmark + ablation
- [ ] Baselines是被充分tuned的
- [ ] 有diverse workloads/models测试
- [ ] 报告了P50/P95/P99 + error bars

**整体**
- [ ] 没有未定义的简写
- [ ] 所有Figures在正文中引用了
- [ ] 所有表格在正文中讨论了
- [ ] 参考文献格式正确
