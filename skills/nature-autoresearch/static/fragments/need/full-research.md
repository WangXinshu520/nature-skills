# Need: 我想做全自动科研 / Full Automated Research

当用户想实现从 idea 到 paper 的全流程科研自动化。

## 起步推荐 / Starter Picks

1. **[SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist)**
   首个全面自动化科学发现系统。从 idea 生成到论文写作，需要最少的人工监督。这是全自动科研方向的里程碑式工作，社区活跃、文档完善。

2. **[SamuelSchmidgall/AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory)**
   端到端自主研究流程：idea → 文献综述 → 实验 → 报告。支持**自主模式**（完全自动）和**副驾模式**（人机协作），适合渐进式采用。

## 进阶选项 / Advanced Options

- **[SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2)** — v2 版本，移除模板依赖，通过 agentic tree search 推广到多个研究领域。Workshop 级自动科学发现。

- **[HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher)** — NeurIPS 2025 论文。完整端到端：假设 → 实验 → 稿件 → 审稿。生产版本在 [novix.science](https://novix.science/chat) 可用。

- **[AweAI-Team/AiScientist](https://github.com/AweAI-Team/AiScientist)** — 长时域 ML 研究实验室，层级编排 + File-as-Bus 协调。驱动 PaperBench 和 MLE-Bench 迭代循环。适合有固定计算/时间预算的竞赛式研究。

- **[kaust-ark/ARK](https://github.com/kaust-ark/ARK)** — 6 个智能体编排，支持 CLI、Web 仪表盘和 Telegram 三种控制方式。idea + venue → paper 的完整管线。

## 如果你需要文献综述 / If You Need Literature Review

- **[PouriaRouzrokh/LatteReview](https://github.com/PouriaRouzrokh/LatteReview)** — 低代码 Python 包，自动化系统文献综述
- **[LitLLM/LitLLM](https://github.com/LitLLM/LitLLM)** — RAG 驱动的文献综述，生成准确的相关工作章节

## 注意事项 / Notes

- 全自动科研仍在快速发展中，当前工具更适合辅助科研而非替代科学家的判断。
- 生成的论文需要人工验证实验可复现性和论点的正确性。
- 查看 `references/full-catalog.md` 获取完整的 Research-agent systems 列表（20+ 系统）。
