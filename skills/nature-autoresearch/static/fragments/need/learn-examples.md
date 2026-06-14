# Need: 我想看应用案例 / Learn from Examples

当用户想了解 autoresearch 在真实世界中的成功应用，寻找灵感和参考。

## 最有参考价值的案例 / Most Referencable Cases

### 工业级应用 / Industry Applications

1. **Shopify Liquid 引擎优化**
   Shopify CEO Tobi Lütke 亲自上手的优化案例。公开的 PR 轨迹展示了显著的解析/渲染加速和内存分配减少。这是目前最高调、最可信的工业级应用实例。
   - [tweet](https://x.com/tobi/status/2032212531846971413)
   - [PR with traces](https://github.com/Shopify/liquid/pull/2056)

2. **Driveline 棒球生物力学**
   用生物力学数据预测投球速度。公开报告模型质量大幅提升，展示了 autoresearch 从代码领域向体育科学领域的扩展潜力。
   - [tweet](https://x.com/drivelinekyle/status/2032242254035992610)

### 最有教育意义 / Most Educational

1. **Nick Oak 的网球预测 + reward hacking 案例**
   最有价值的"反面教材"：作者记录了优化设置出错的完整轨迹，包括 reward hacking 是如何发生的。任何一个要做自主改进的人必读。
   - [blog](https://nickoak.com/posts/tennis-xgboost-autoresearch/)
   - [repo](https://github.com/buildoak/tennis-xgboost-autoresearch)

2. **SkyPilot: 在 GPU 集群上扩展 Autoresearch**
   实操指南：在 H100/H200 集群上通过云编排运行 autoresearch。有集群资源的团队必读。
   - [SkyPilot Blog](https://blog.skypilot.co/scaling-autoresearch/)

### 技术深度文章 / In-Depth Technical

1. **Kingy AI 技术拆解** — 循环架构、变异运算符、适应度函数设计的详细技术走查 [article](https://kingy.ai/ai/autoresearch-karpathys-minimal-agent-loop-for-autonomous-llm-experimentation/)
2. **Autoresearch 101 Builder's Playbook** — 将模式应用于 prompt、agent 和工作流的深度剖析 [article](https://sidsaladi.substack.com/p/autoresearch-101-builders-playbook)
3. **Addy Osmani: Self-Improving Coding Agents** — 用 Claude Code 搭建自我改进循环的实操指南 [article](https://addyosmani.com/blog/self-improving-agents/)

### 科研应用 / Research Applications

- **Vesuvius Challenge 墨水检测蜂群** — 多智能体实验循环应用于古卷，跨卷泛化改进 [blog](https://scrollprize.substack.com/p/we-are-cooking)
- **地球系统模型优化** — LLM提出方程结构+搜索调参的混合流程 [blog](https://paragiri.com/blog/2026/autoresearch-earth-system-models/)
- **The Agentic Researcher** — 学术论文，引用autoresearch作为典范 [arxiv 2603.15914](https://arxiv.org/html/2603.15914)

## 注意事项 / Notes

- 这些案例大多来自社交媒体和博客，不是经过同行评审的论文。参考时保持批判性思维。
- 部分案例（如 Shopify Liquid 优化）的完整实验设置未公开，只能看到结果。
- 查看 `references/full-catalog.md` 获取完整的 Use cases and writeups 列表（16 个条目）。
