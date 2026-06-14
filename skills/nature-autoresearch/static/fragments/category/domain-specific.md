# Domain-Specific Adaptations / 领域定制适配

将自主改进循环应用于非ML研究场景的定制版本。展示了 "keep-or-revert" 模式在多领域的通用性。

For full descriptions, see `references/full-catalog.md`.

## 工具列表 / Tool List

- [mattprusak/autoresearch-genealogy](https://github.com/mattprusak/autoresearch-genealogy) — 家谱研究：结构化prompt、档案指南、源检查、vault流程迭代扩展家族史 (Genealogy research with structured prompts, archive guides, source checks)
- [ArchishmanSengupta/autovoiceevals](https://github.com/ArchishmanSengupta/autovoiceevals) — 语音AI：对抗性caller+keep-or-revert prompt编辑硬化Vapi/Smallest AI/ElevenLabs (Adversarial callers hardening voice AI agents)
- [chrisworsey55/atlas-gic](https://github.com/chrisworsey55/atlas-gic) — 交易：对滚动Sharpe ratio优化prompt和投资组合编排 (Trading agents optimizing against rolling Sharpe ratio)
- [RightNow-AI/autokernel](https://github.com/RightNow-AI/autokernel) — GPU kernel优化：profiling瓶颈→编辑kernel→benchmark→keep-or-revert (GPU kernel optimization via bottleneck profiling)
- [Agent-Analytics/autoresearch-growth](https://github.com/Agent-Analytics/autoresearch-growth) — 落地页A/B测试：分析快照+测量结果种子下一轮 (Landing-page A/B testing with analytics snapshots)
- [Rkcr7/autoresearch-sudoku](https://github.com/Rkcr7/autoresearch-sudoku) — Rust Sudoku求解器：AI迭代改写和benchmark，击败顶尖人写求解器 (AI rewriting Rust solver that beats human-built leaders)
- [jeongph/autospec](https://github.com/jeongph/autospec) — Spring Boot服务生成：从自然语言业务规则自主构建服务+测试 (Natural-language to Spring Boot service with JUnit tests, 119→950 lines in 5 cycles)

## 领域速查 / Quick Domain Lookup

| 应用领域 / Domain | 推荐项目 / Recommended |
|---|---|
| 家谱研究 / Genealogy | `mattprusak/autoresearch-genealogy` |
| 语音AI / Voice AI | `ArchishmanSengupta/autovoiceevals` |
| 交易策略 / Trading | `chrisworsey55/atlas-gic` |
| GPU Kernel优化 | `RightNow-AI/autokernel` |
| A/B测试优化 | `Agent-Analytics/autoresearch-growth` |
| 代码竞赛/Solver | `Rkcr7/autoresearch-sudoku` |
| 代码生成 | `jeongph/autospec` |
