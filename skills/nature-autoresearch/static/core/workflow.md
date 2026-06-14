# Workflow: nature-autoresearch

## 主工作流 / Main Workflow

技能触发后，根据用户意图选择以下 7 条路径之一执行。

After skill is triggered, execute one of the following 7 paths based on user intent.

---

## Path A: 智能推荐 / Smart Recommendation

用户描述了具体的科研自动化需求时走此路径。

When the user describes a concrete research automation need:

### A1. 分析需求 / Analyze the need
从用户描述中提取关键信息：
- 目标任务类型（跑实验/调参数/写论文/文献综述/代码优化等）
- 硬件环境（有无 GPU、什么平台、多少卡）
- 技术栈偏好（Python/PyTorch、Claude Code 等）
- 是否需要评估对比

### A2. 匹配 need axis
将需求映射到以下场景之一，加载对应的 `fragments/need/*.md`：
- `start-loop` — 想跑一个自主改进循环（最常见）
- `full-research` — 想做全自动科研（从idea到paper）
- `specific-hardware` — 有特定硬件平台（MacOS/Windows/WebGPU等）
- `evaluate-agent` — 想评估智能体的研究能力
- `learn-examples` — 想看实际应用案例

### A3. 交叉推荐 / Cross-recommend
根据匹配的 need，交叉引用 `fragments/category/*.md` 中的具体工具，给出 1-3 个推荐：
- 起步推荐（1-2 个最推荐的入门项目）
- 进阶选项（1-2 个更高阶/更专业的选项）
- 每个推荐包含：名称、一句话描述、GitHub 链接、为什么适合

### A4. 需要详细信息时 / When more detail is needed
如果用户要求更多信息，加载 `references/full-catalog.md` 获取完整工具描述。

---

## Path B: 目录浏览 / Catalog Browsing

用户想按类别、平台或领域浏览整个工具库时走此路径。

When the user wants to browse the catalog by category:

### B1. 确认浏览维度
用户可能想按以下维度浏览：
- 按工具类别（category axis）
- 按硬件平台
- 按应用领域

如果用户没有明确指定，展示 6 个类别概览让用户选择。

### B2. 检测 category axis
将用户意图映射到以下类别之一，加载对应的 `fragments/category/*.md`：
- `general-purpose` — 通用自主改进循环
- `research-agent` — 科研智能体系统
- `platform-port` — 平台移植和硬件分支
- `domain-specific` — 领域定制适配
- `benchmark` — 评估和基准测试
- `use-case` — 知名应用案例

### B3. 展示工具列表
展示匹配类别下的工具列表（名称 + 一句话描述 + 链接），建议一次性展示该类别下的全部条目。

---

## Path C: MoltFounders 引导 / MoltFounders Guide

用户询问如何用 AI 智能体自动维护 GitHub 仓库时走此路径。

When the user asks how to set up AI agents to auto-maintain a GitHub repo:

### C1. 加载核心
加载 `static/core/stance.md`。

### C2. 直接加载指南
加载 `references/moltfounders-guide.md`，这是一份自包含的实战指南。

### C3. 交互式引导
根据用户的具体场景（维护 awesome list / 维护项目文档 / 管理 issue 和 PR），从指南中选择最相关的部分进行解释。

---

---

## Path D: 论文推荐 / Paper Recommendation

用户询问系统研究论文或特定研究方向的顶会论文时走此路径。

When the user asks about systems research papers or papers on specific topics:

### D1. 检测研究主题 / Detect research topic
从用户描述中提取关键信息：
- 具体研究领域（LLM推理训练、GPU通信、张量编译器等）
- 偏好的会议（NSDI、OSDI 等，如未指定则不限）
- 是想了解概览还是深入特定子方向

### D2. 匹配 research_topic axis
将需求映射到以下主题之一，加载对应的 `fragments/research_topic/*.md`：
- `llm-serving` — LLM推理与服务系统
- `llm-training` — 大模型训练系统
- `gpu-communication` — GPU通信与集合操作
- `tensor-compiler` — 张量编译器与程序优化
- `vector-search` — 向量搜索与RAG基础设施
- `network-ml` — 网络机器学习与AI网络
- `edge-ml` — 边缘ML与网络内推理
- `rl-training` — 强化学习训练基础设施
- `memory-disaggregation` — 内存分离与RDMA系统

### D3. 展示推荐论文 / Present paper recommendations
根据加载的fragment内容，为每篇论文提供：
- 论文标题
- 一句话贡献总结（中英双语）
- 会议和年份
- 演示和PDF链接

### D4. 需要详细信息时 / When more detail is needed
如果用户要求更多信息或查看完整论文列表，加载 `references/paper-catalog.md`。

### D5. 实验指导 / Experiment guidance
如果用户的提问涉及实验设计 ("怎么测"、"用什么baseline"、"实验要注意什么")，使用fragment中的"实验指导"section：
- 推荐合适的指标（如LLM推理测TTFT/TPOT/吞吐，训练测MFU/iteration time）
- 推荐常用的baseline（如vLLM、Megatron-LM、默认NCCL配置）
- 提醒常见实验坑（如warmup问题、scale effect、拓扑敏感性）
- 如果用户需要详细的实验参数（硬件配置、数据集选择、workload pattern），加载 `references/paper-catalog.md` 获取具体论文的实验细节

### D6. 跨主题交叉引用 / Cross-topic reference
论文可能跨多个研究主题（例如SYMPHONY同时属于llm-serving和memory-disaggregation），根据需要加载额外的fragment文件提供更全面的推荐。

### D7. 论文评价 / Paper evaluation
如果用户询问论文评价（"这个方向哪些论文比较强"、"XX论文有什么局限"、"对比一下"），使用fragment中的"评估与洞察"section：
- 提供类别级的趋势评价（Category-Level Assessment），总结该方向的整体研究趋势
- 对具体论文提供亮点与局限分析（Paper Highlights & Limitations），引用论文中的具体实验数据
- 给出实用建议（Practical Guidance），帮助用户根据具体场景选择合适的方案
- 评价必须基于证据（具体实验数字、benchmark结果），不添加主观颂词

---

## 注意事项 / Notes

- 路径可以组合：用户可能先浏览目录（Path B）再深入推荐（Path A）
- Path A 的工具推荐可以交叉引用 Path D 的论文（例如推荐GPU自主实验工具时顺便推荐GPU通信论文）
- MoltFounders 引导（Path C）与工具推荐（Path A/B）完全独立，通常不会在同一次对话中触发
- Path D 可以独立触发，也可以通过 Path A 的交叉引用逻辑自动触发
- Path D 的 D7（论文评价）提供基于证据的分析，与 D5（实验指导）互补——D5 关注"如何做实验"，D7 关注"论文质量如何"

---

## Path E: 论文写作指导 / Paper Writing Guidance

用户询问论文写作方法时走此路径。

When the user asks about paper writing methodology:

### E1. 加载写作指南
加载 `references/paper-writing-guide.md`，这是一份基于68篇系统论文结构分析的完整写作指南。

### E2. 确定研究主题
如果用户指定了具体研究方向（如"LLM serving论文的Introduction怎么写"），同时加载对应的 `fragments/research_topic/*.md` 中的"写作指导"section。

### E3. 提供具体指导
根据用户需要覆盖：Abstract模板选择、Introduction结构、Design组织方式、Evaluation checklist、图表设计、常见审稿意见预防。

---

## Path F: 论文实现指导 / Paper Implementation Guidance

用户询问系统实现方法时走此路径。

When the user asks about system implementation patterns:

### F1. 加载实现指南
加载 `references/implementation-guide.md`，这是一份基于实际论文代码的通用实现模式指南。

### F2. 确定研究主题
如果用户指定了具体方向，同时加载对应 fragment 的"实现指导"section。

### F3. 提供代码级指导
覆盖：NCCL plugin模式、CUDA kernel优化、框架修改点 (vLLM/Megatron-LM/DeepSpeed)、代码组织、可复现性实践。

---

## Path G: 完整实验流程 / Full Experiment Pipeline

用户需要完整的实验设计方案时走此路径。

When the user needs complete experiment recipes:

### G1. 确定研究主题
根据用户描述匹配 `research_topic` axis。

### G2. 加载实验流程
加载对应 fragment 的"实验流程 / Experiment Pipeline" section。

### G3. 提供逐步指导
提供从环境准备到结果分析的完整分步实验流程，包括：
- 硬件/软件配置
- 模型和数据集选择
- Baseline配置
- 各实验阶段的指标和测量方法
- Ablation和泛化测试
- 结果分析和可视化建议

---

## 注意事项 / Notes

- 路径可以组合：用户可能先浏览目录（Path B）再深入推荐（Path A）
- Path A 的工具推荐可以交叉引用 Path D 的论文（例如推荐GPU自主实验工具时顺便推荐GPU通信论文）
- MoltFounders 引导（Path C）与工具推荐（Path A/B）完全独立，通常不会在同一次对话中触发
- Path D 可以独立触发，也可以通过 Path A 的交叉引用逻辑自动触发
- Path D 的 D7（论文评价）提供基于证据的分析，与 D5（实验指导）互补——D5 关注"如何做实验"，D7 关注"论文质量如何"
- Path E（写作指导）和 Path F（实现指导）可以独立触发，也可以与 Path D 组合
- Path G（实验流程）通常与 Path D 的 D5 组合使用
- 如果用户需求无法匹配任何路径，回退到展示全部概览
