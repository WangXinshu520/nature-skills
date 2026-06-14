# Full Catalog / 完整工具目录

This is the complete curated catalog from the awesome-autoresearch repository, organized by category. All tools are listed with their original descriptions for reference.

> 来源 / Source: [alvinunreal/awesome-autoresearch](https://github.com/alvinunreal/awesome-autoresearch)

---

## General-Purpose Descendants / 通用自主改进循环 (25 entries)

- [kayba-ai/recursive-improve](https://github.com/kayba-ai/recursive-improve) - Recursive self-improvement framework where agents capture execution traces, analyze failure patterns, and apply targeted fixes with keep-or-revert evaluation.
- [vukrosic/auto-research](https://github.com/vukrosic/auto-research) - Docs-only control plane for an open autonomous AI research lab — file-based operating model for human direction and agent execution.
- [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) - Claude Code skill that generalizes autoresearch into a reusable loop for software, docs, security, shipping, debugging, and other measurable goals.
- [leo-lilinxiao/codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) - Codex-native autoresearch skill with resume support, lessons across runs, optional parallel experiments, and mode-specific workflows.
- [SeeleAI/Thoth](https://github.com/SeeleAI/Thoth) - Dashboard-first Claude Code and Codex runtime for autoresearch, with durable runs, locked work items, visible ledgers, and reviewable verdicts.
- [supratikpm/gemini-autoresearch](https://github.com/supratikpm/gemini-autoresearch) - Gemini CLI skill that generalises autoresearch to any measurable goal. Gemini-native: uses Google Search grounding as a live verification source inside the loop, true headless overnight mode via `--yolo --prompt`, and 1M token context. Also works in Antigravity IDE via `.agents/skills/`.
- [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) - `pi` extension plus dashboard for persistent experiment loops, live metrics, confidence tracking, and resumable autoresearch sessions.
- [drivelineresearch/autoresearch-claude-code](https://github.com/drivelineresearch/autoresearch-claude-code) - Claude Code plugin/skill port of `pi-autoresearch`, with a clean experiment-loop workflow and a concrete biomechanics case study.
- [greyhaven-ai/autocontext](https://github.com/greyhaven-ai/autocontext) - Closed-loop control plane for repeated agent improvement, with evaluation, persistent knowledge, staged validation, and optional distillation into cheaper local runtimes.
- [jmilinovich/goal-md](https://github.com/jmilinovich/goal-md) - Generalizes autoresearch into a `GOAL.md` pattern for repos where the agent must first construct a measurable fitness function before it can optimize.
- [james-s-tayler/lazy-developer](https://github.com/james-s-tayler/lazy-developer) - Claude Code skill that orchestrates autoresearch across a prioritized sequence of optimization goals (coverage, test speed, build speed, complexity, LOC, performance) using GOAL.md as the engine. Supports standalone and Ralph Mode multi-instance execution.
- [mutable-state-inc/autoresearch-at-home](https://github.com/mutable-state-inc/autoresearch-at-home) - Collaborative fork of upstream autoresearch that adds experiment claiming, shared best-config syncing, hypothesis exchange, and swarm-style coordination across many single-GPU agents.
- [zkarimi22/autoresearch-anything](https://github.com/zkarimi22/autoresearch-anything) - Generalizes autoresearch to **any measurable metric** — system prompts, API performance, landing pages, test suites, config tuning, SQL queries. "If you can measure it, you can optimize it."
- [Entrpi/autoresearch-everywhere](https://github.com/Entrpi/autoresearch-everywhere) - Cross-platform expansion that auto-detects hardware config and starts the loop. The "glue and generalization" half of autoresearch.
- [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS) - **Automated Design of Agentic Systems** — ICLR 2025. Meta-agents that invent novel agent architectures by programming them in code.
- [MaximeRobeyns/self_improving_coding_agent](https://github.com/MaximeRobeyns/self_improving_coding_agent) - **SICA**: Self-Improving Coding Agent that edits its own codebase. ICLR 2025 Workshop paper demonstrating scaffold-level self-improvement on coding benchmarks.
- [peterskoett/self-improving-agent](https://github.com/peterskoett/self-improving-agent) - Alternative self-improving agent architecture with reflection and meta-learning cycles.
- [metauto-ai/HGM](https://github.com/metauto-ai/HGM) - **Huxley-Gödel Machine** for coding agents — applies self-improvement to SWE-bench performance via meta-level optimization.
- [gepa-ai/gepa](https://github.com/gepa-ai/gepa) - **GEPA (Genetic-Pareto)** — ICLR 2026 Oral. Reflective prompt evolution that outperforms RL (GRPO) on benchmarks. Optimizes any textual parameters against any metric using natural language reflection.
- [sentient-agi/EvoSkill](https://github.com/sentient-agi/EvoSkill) - Automated skill discovery for coding agents: evolves reusable skills and prompts from failed trajectories against benchmarks, with support for Claude Code, Codex CLI, OpenCode, OpenHands, and Goose.
- [MrTsepa/autoevolve](https://github.com/MrTsepa/autoevolve) - GEPA-inspired autoresearch for self-play: mutate code strategies, evaluate head-to-head, rate with Elo/Bradley-Terry, branch from the Pareto front. Agent reads match traces to target mutations. Works as a Claude Code skill.
- [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) - Agent swarm intelligence for autoresearch — spawns parallel GPU research directions, distributes work across agents, aggregates results.
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) - Comprehensive skill library including autoresearch orchestration with two-loop architecture (inner optimization + outer synthesis).
- [WecoAI/aideml](https://github.com/WecoAI/aideml) - **AIDE**: Tree-search ML engineering agent that autonomously improves model performance via iterative code generation and evaluation.
- [weco.ai](https://weco.ai) - **Weco**: Cloud platform for AIDE with observability, experiment tracking, and managed runs — brings the autoresearch loop into production.

---

## Research-Agent Systems / 科研智能体系统 (22 entries)

- [aiming-lab/AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) - End-to-end research pipeline that turns a topic into literature review, experiments, analysis, peer review, and paper drafts; broader than autoresearch, but clearly in the same lineage.
- [OpenRaiser/NanoResearch](https://github.com/OpenRaiser/NanoResearch) - End-to-end autonomous research engine that plans experiments, generates code, runs jobs locally or on SLURM, analyzes real results, and writes papers grounded in those outputs.
- [kaust-ark/ARK](https://github.com/kaust-ark/ARK) - **ARK (Automatic Research Kit)**: idea + venue → paper pipeline orchestrating 6 agents — proposal analysis, literature search, Slurm experiments, LaTeX drafting, iterative peer review. Controlled via CLI, web dashboard, or Telegram.
- [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - Markdown-first research workflows for Claude Code and other agents, centered on autonomous literature review, experiments, paper iteration, and cross-model critique.
- [skyllwt/AutoSci](https://github.com/skyllwt/AutoSci) - Wiki-centric full-lifecycle research platform built on Claude Code, realizing Karpathy's LLM-Wiki vision. 20+ skills cover the full loop: ingest → ideate → novelty check → experiment design / run / eval → paper writing. Research state lives in a structured knowledge wiki with an interactive graph.
- [Sibyl-Research-Team/AutoResearch-SibylSystem](https://github.com/Sibyl-Research-Team/AutoResearch-SibylSystem) - Fully autonomous AI scientist built on Claude Code, with explicit AutoResearch lineage, multi-agent research iteration, GPU experiment execution, and a self-evolving outer loop.
- [eimenhmdt/autoresearcher](https://github.com/eimenhmdt/autoresearcher) - Early open-source package for automating scientific workflows, currently centered on literature-review generation with an ambition toward broader autonomous research.
- [hyperspaceai/agi](https://github.com/hyperspaceai/agi) - Distributed, peer-to-peer research network where autonomous agents run experiments, gossip findings, maintain CRDT leaderboards, and archive results to GitHub across multiple research domains.
- [Human-Agent-Society/CORAL](https://github.com/Human-Agent-Society/CORAL) - **CORAL**: Autonomous multi-agent evolution for open-ended discovery ([arXiv:2604.01658](https://arxiv.org/abs/2604.01658)). Long-running agents with shared persistent memory, asynchronous execution, and heartbeat-based interventions; SOTA on 10 math/algorithmic/systems tasks.
- [SakanaAI/AI-Scientist](https://github.com/SakanaAI/AI-Scientist) - **The AI Scientist**: First comprehensive system for fully automatic scientific discovery. From idea generation to paper writing with minimal human supervision.
- [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) - Workshop-level automated scientific discovery via agentic tree search. Removes template dependency from v1, generalizes across research domains.
- [AweAI-Team/AiScientist](https://github.com/AweAI-Team/AiScientist) - **AiScientist**: long-horizon ML research lab with hierarchical orchestration and File-as-Bus coordination — workspace files act as the durable system of record. Drives autonomous paper-reproduction (PaperBench) and competition-style MLE-Bench iteration loops under fixed compute/time budgets. ([arXiv 2604.13018](https://arxiv.org/abs/2604.13018))
- [HKUDS/AI-Researcher](https://github.com/HKUDS/AI-Researcher) - NeurIPS 2025 paper. Full end-to-end research automation: hypothesis → experiments → manuscript → peer review. Production version at [novix.science](https://novix.science/chat).
- [openags/Auto-Research](https://github.com/openags/Auto-Research) - **OpenAGS**: Orchestrates a team of AI agents across the full research lifecycle — lit review, hypothesis generation, experiments, manuscript writing, and peer review.
- [SamuelSchmidgall/AgentLaboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) - End-to-end autonomous research workflow: idea → literature review → experiments → report. Supports both autonomous and co-pilot modes.
- [AgentRxiv](https://agentrxiv.github.io/) - Collaborative autonomous research framework where agent laboratories share a preprint server to build on each other's work iteratively.
- [JinheonBaek/ResearchAgent](https://github.com/JinheonBaek/ResearchAgent) - Iterative research idea generation over scientific literature with LLMs. Multi-agent review and feedback loops.
- [du-nlp-lab/MLR-Copilot](https://github.com/du-nlp-lab/MLR-Copilot) - Autonomous ML research framework — generates ideas, implements experiments, analyzes results.
- [MASWorks/ML-Agent](https://github.com/MASWorks/ML-Agent) - Reinforcing LLM agents for autonomous ML engineering. Learns from trial and error to improve model performance.
- [PouriaRouzrokh/LatteReview](https://github.com/PouriaRouzrokh/LatteReview) - Low-code Python package for **automated systematic literature reviews** via AI-powered agents.
- [LitLLM/LitLLM](https://github.com/LitLLM/LitLLM) - AI-powered literature review assistant using RAG for accurate, well-structured related-work sections in academic writing.
- [Agent Laboratory](https://agentlaboratory.github.io/) - Three-phase research pipeline: Literature Review → Experimentation → Report Writing, with specialized agents for each phase.

---

## Platform Ports & Hardware Forks / 平台移植和硬件分支 (9 entries)

- [gianfrancopiana/openclaw-autoresearch](https://github.com/gianfrancopiana/openclaw-autoresearch) - OpenClaw port of pi-autoresearch; autonomous experiment loop for any optimization target with statistical confidence scoring.
- [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos) - Widely adopted macOS fork that adapts upstream autoresearch for Apple Silicon / MPS while preserving the original loop shape.
- [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) - MLX-native Apple Silicon port that keeps the upstream fixed-budget `val_bpb` loop while removing the PyTorch/CUDA dependency entirely.
- [jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx) - Windows-native RTX fork focused on consumer NVIDIA GPUs, with explicit VRAM floors and a practical desktop setup path.
- [iii-hq/n-autoresearch](https://github.com/iii-hq/n-autoresearch) - Multi-GPU autoresearch infrastructure with structured experiment tracking, adaptive search strategy, crash recovery, and queryable orchestration around the classic `train.py` loop.
- [lucasgelfond/autoresearch-webgpu](https://github.com/lucasgelfond/autoresearch-webgpu) - Browser/WebGPU port that lets agents generate training code, run experiments in-browser, and feed results back into the loop without a Python setup.
- [tonitangpotato/autoresearch-engram](https://github.com/tonitangpotato/autoresearch-engram) - Fork with **persistent cognitive memory** — frequency-weighted retrieval of cross-session knowledge for improved experiment continuity.
- **Colab/Kaggle T4 port** - Adapts autoresearch for free T4 GPUs (Google Colab / Kaggle) with zero cost and zero local setup. Key changes: Flash Attention 3 → PyTorch SDPA, removes H100-only kernel dependency. ([upstream issue #208](https://github.com/karpathy/autoresearch/issues/208))
- [ArmanJR-Lab/autoautoresearch](https://github.com/ArmanJR-Lab/autoautoresearch) - Jetson AGX Orin port with a **director** — a Go binary that acts as a "creative director" injecting novelty (arxiv papers + DeepSeek Reasoner) into the loop to escape local minima. Includes multi-experiment comparison (baseline vs director-guided) with detailed stall analysis.

---

## Domain-Specific Adaptations / 领域定制适配 (7 entries)

- [mattprusak/autoresearch-genealogy](https://github.com/mattprusak/autoresearch-genealogy) - Applies the autoresearch pattern to genealogy, using structured prompts, archive guides, source checks, and vault workflows to iteratively expand and verify family-history research.
- [ArchishmanSengupta/autovoiceevals](https://github.com/ArchishmanSengupta/autovoiceevals) - Uses adversarial callers plus keep-or-revert prompt edits to harden voice AI agents across Vapi, Smallest AI, and ElevenLabs.
- [chrisworsey55/atlas-gic](https://github.com/chrisworsey55/atlas-gic) - Applies the autoresearch keep-or-revert loop to trading agents, optimizing prompts and portfolio orchestration against rolling Sharpe ratio instead of model loss.
- [RightNow-AI/autokernel](https://github.com/RightNow-AI/autokernel) - Applies the autoresearch loop to GPU kernel optimization: profile bottlenecks, edit one kernel, benchmark, keep or revert, repeat.
- [Agent-Analytics/autoresearch-growth](https://github.com/Agent-Analytics/autoresearch-growth) - Applies autoresearch to landing-page positioning and A/B test candidates, using analytics snapshots and measured experiment results to seed subsequent rounds.
- [Rkcr7/autoresearch-sudoku](https://github.com/Rkcr7/autoresearch-sudoku) - Enhanced autoresearch workflow where an AI agent iteratively rewrites and benchmarks a Rust sudoku solver, ultimately beating leading human-built solvers on hard benchmark sets.
- [jeongph/autospec](https://github.com/jeongph/autospec) - Reads natural-language business rules and autonomously builds a Spring Boot service with tests via the keep-or-revert loop. Evaluates with Gradle build + JUnit XML. 119-line skeleton to 950 lines in 5 cycles.

---

## Evaluation & Benchmarks / 评估和基准测试 (5 entries)

- [snap-stanford/MLAgentBench](https://github.com/snap-stanford/MLAgentBench) - Benchmark suite for evaluating AI agents on ML experimentation tasks. 13 tasks from CIFAR-10 to BabyLM.
- [openai/mle-bench](https://github.com/openai/mle-bench) - OpenAI's benchmark for measuring how well AI agents perform at ML engineering.
- [chchenhui/mlrbench](https://github.com/chchenhui/mlrbench) - MLR-Bench: Evaluating AI agents on open-ended ML research. 201 tasks from NeurIPS/ICLR/ICML workshops.
- [gersteinlab/ML-Bench](https://github.com/gersteinlab/ML-Bench) - Evaluates LLMs and agents for ML tasks on repository-level code.
- [THUDM/AgentBench](https://github.com/THUDM/AgentBench) - Comprehensive benchmark for LLM-as-Agent evaluation across 8 distinct environments. ICLR 2024.

---

## Notable Use Cases & Writeups / 知名应用案例和文章 (16 entries)

- **Shopify Liquid optimization** - Tobi Lütke shared an autoresearch-style optimization run on Shopify's Liquid engine, with public traces showing major parse/render speedups and allocation reductions. ([tweet](https://x.com/tobi/status/2032212531846971413), [PR with traces](https://github.com/Shopify/liquid/pull/2056))
- **Driveline baseball biomechanics** - Public autoresearch-style experiment loop for pitch-velocity prediction from biomechanics data, with large reported gains in model quality. ([tweet](https://x.com/drivelinekyle/status/2032242254035992610))
- **Tennis XGBoost prediction + reward hacking writeup** - Nick Oak documents an autoresearch-inspired loop for tennis match prediction, including where the optimization setup went wrong. ([blog](https://nickoak.com/posts/tennis-xgboost-autoresearch/) · [repo](https://github.com/buildoak/tennis-xgboost-autoresearch) · [gamed branch](https://github.com/buildoak/tennis-xgboost-autoresearch/tree/archived/gamed-iterations))
- **Vesuvius Challenge ink detection swarm** - Multi-agent experimental loop applied to ancient-scroll ink detection, with a strong writeup on cross-scroll generalization improvements. ([blog](https://scrollprize.substack.com/p/we-are-cooking))
- **Earth system model optimization** - Hybrid workflow where an LLM proposes equation structures and a search process tunes parameters, showing how the autoresearch pattern extends into scientific modeling. ([tweet](https://x.com/devparagiri/status/2035075626273739068), [blog](https://paragiri.com/blog/2026/autoresearch-earth-system-models/))
- **The Agentic Researcher** - Paper: "A Practical Guide to AI-Assisted Research in Mathematics and Machine Learning." Cites autoresearch as the canonical example of automated ML experiment pipelines. ([arxiv 2603.15914](https://arxiv.org/html/2603.15914))
- **Scaling Autoresearch to GPU Clusters** - SkyPilot blog on running autoresearch on H100/H200 clusters with cloud orchestration. ([SkyPilot Blog](https://blog.skypilot.co/scaling-autoresearch/))
- **Self-Improving Coding Agents** - Addy Osmani's practical guide to setting up self-improving agent loops with Claude Code. ([article](https://addyosmani.com/blog/self-improving-agents/))
- **autoresearch@home: Distributed AI Research** - SETI@home model applied to autoresearch — contribute GPU time to collective model optimization. ([Ensue Blog](https://ensue.dev/blog/autoresearch-at-home/))
- **Claude Code + AutoResearch for Self-Improving Skills** - MindStudio guide to building self-improving AI skills using Claude Code with autoresearch patterns. ([article](https://www.mindstudio.ai/blog/claude-code-autoresearch-self-improving-skills))
- **100 ML Experiments Overnight** - Particula technical breakdown with domain-agnostic fork applications. ([article](https://particula.tech/blog/karpathy-autoresearch-autonomous-ml-experiments))
- **PM's Guide to Autoresearch** - Product manager's guide covering setup, community forks, and real-world applications. ([article](https://www.news.aakashg.com/p/autoresearch-guide-for-pms))
- **Autoresearch 101 Builder's Playbook** - Substack deep-dive on applying autoresearch patterns to prompts, agents, and workflows with concrete examples. ([article](https://sidsaladi.substack.com/p/autoresearch-101-builders-playbook))
- **Kingy AI Technical Breakdown** - Detailed technical walkthrough of the autoresearch loop architecture, mutation operators, and fitness function design. ([article](https://kingy.ai/ai/autoresearch-karpathys-minimal-agent-loop-for-autonomous-llm-experimentation/))
- **Fortune Feature** - Business and industry context on why autoresearch matters for the future of autonomous AI agents. ([article](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/))
