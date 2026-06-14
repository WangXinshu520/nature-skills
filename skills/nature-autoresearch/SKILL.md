---
name: nature-autoresearch
description: >-
  Recommend AI autonomous research tools from the awesome-autoresearch catalog of 85+ projects. Covers autonomous improvement loops (autoresearch, self-improving agents), full research-agent systems (AI Scientist, end-to-end research automation), hardware/platform ports, domain-specific adaptations, and ML agent benchmarks. Also guides users on setting up AI agents to auto-maintain GitHub repos via MoltFounders rules (issue triage, PR review, research discovery, staleness management). Now also recommends systems research papers from top conferences (NSDI 2026, OSDI 2025) covering LLM serving, training, GPU communication, tensor compilers, vector search, and more, with evidence-based evaluation (strengths, limitations, practical impact) and experiment design guidance (metrics, baselines, pitfalls). Trigger when users describe research automation needs, ask about karpathy/autoresearch, AI scientist tools, autonomous experiments, systems/AI papers, experiment design, or MoltFounders agent maintenance workflows. Chinese trigger phrases: 自主科研、自动化实验、自动调参、AI科学实验、自动写论文、科研agent、自动化研究、自主改进循环、AI科学家工具推荐、MoltFounders搭建、系统论文推荐、大模型推理论文、GPU通信论文、实验设计、实验指标、baseline, and general queries about AI research tooling and self-improving AI systems.
version: 1.2.0
author: Community contribution, refactored from awesome-autoresearch into static/dynamic layers
---

# Nature-Autoresearch — Router

This skill recommends AI autonomous research tools from the awesome-autoresearch catalog, guides users on AI agent-based repo maintenance, recommends systems research papers from top conferences (NSDI 2026, OSDI 2025), and provides experiment design guidance (metrics, baselines, pitfalls).

This skill is split into two layers:

- A **static layer** under `static/` that holds versioned, reusable content fragments (stance, workflow, taxonomy, category catalogs, need-based recommendations).
- A **dynamic layer** (this file plus `manifest.yaml`) that detects the request's axes and loads only the fragments needed for the current job.

Do not try to apply the recommendation logic from memory or from this router. Always load fragments from disk as described below.

## Routing protocol

Follow these five steps every time the skill is invoked.

### 1. Load the manifest and the core layer

Read [manifest.yaml](manifest.yaml). It declares the axes (`category`, `need`), the allowed values, and the file paths each value maps to.

Also read every file listed under `always_load`. These hold the stance, workflow, and taxonomy that apply to every request.

### 2. Determine which path to take

Based on the user's intent, choose one of four paths:

**Path A: Smart Recommendation** — User describes a concrete research automation need.
- Proceed to step 3A (detect `need` axis).
- Also check if the need maps to a `research_topic` for cross-referencing papers (see step 5).

**Path B: Catalog Browsing** — User wants to browse tools by category, platform, or domain.
- Proceed to step 3B (detect `category` axis).

**Path C: MoltFounders Guide** — User asks how to set up AI agents to maintain a GitHub repo.
- Skip axis detection. Load `references/moltfounders-guide.md` directly and guide the user through the setup steps.

**Path D: Paper Recommendation + Evaluation + Experiment** — User asks about systems research papers on specific topics.
- Proceed to step 3D (detect `research_topic` axis).

**Path E: Paper Writing** — User asks about paper writing methodology.
- Skip axis detection. Load `references/paper-writing-guide.md` and use the "写作指导" section from the relevant `research_topic` fragment.

**Path F: Paper Implementation** — User asks about system implementation patterns.
- Skip axis detection. Load `references/implementation-guide.md` and use the "实现指导" section from the relevant `research_topic` fragment.

**Path G: Full Experiment Pipeline** — User wants complete experiment recipes.
- Skip axis detection. Use the "实验流程" section from the relevant `research_topic` fragment.

If the intent is ambiguous, present a brief summary and ask which path the user wants.

### 3A. Path A: Detect need and recommend

1. Analyze the user's research automation need and map it to one or more `need` axis values:
   - `start-loop` — wants to run an autonomous improvement loop
   - `full-research` — wants full end-to-end automated research
   - `specific-hardware` — has specific hardware to run on
   - `evaluate-agent` — wants to evaluate/benchmark an agent
   - `learn-examples` — wants to see real-world use cases

2. Load the matching `fragments/need/*.md` file(s).

3. Use the loaded fragment(s) to make 1-3 concrete tool recommendations. Each recommendation should include:
   - Tool name and GitHub link
   - One-sentence description (English, with Chinese summary)
   - Why it fits the user's specific need

4. If the user wants more detail on a specific tool or category, load `references/full-catalog.md`.

### 3B. Path B: Browse catalog by category

1. If the user didn't specify a category, present the 6-category overview:
   - **General-Purpose Descendants** (通用自主改进循环) — 25 projects
   - **Research-Agent Systems** (科研智能体系统) — 22 projects
   - **Platform Ports & Hardware Forks** (平台移植) — 9 projects
   - **Domain-Specific Adaptations** (领域定制) — 7 projects
   - **Evaluation & Benchmarks** (评估基准) — 5 projects
   - **Notable Use Cases & Writeups** (应用案例) — 16 projects

2. Detect the `category` axis value(s) from the user's selection.

3. Load the matching `fragments/category/*.md` file(s).

4. Present the tool list from the loaded fragment(s) — name, one-sentence description, and link for each entry.

5. If the user wants full descriptions, load `references/full-catalog.md`.

### 3D. Path D: Paper recommendation

1. Analyze the user's research interest and map it to one or more `research_topic` axis values:
   - `llm-serving` — LLM inference, serving systems, scheduling, KV cache, autoscaling
   - `llm-training` — distributed training, fine-tuning, diagnosis, checkpointing
   - `gpu-communication` — GPU-to-GPU collective ops, all-to-all, multi-NIC
   - `tensor-compiler` — tensor program optimization, GPU kernel compilation, auto-tuning
   - `vector-search` — vector databases, ANN search, RAG infrastructure
   - `network-ml` — ML for networking, congestion control, AI cluster design
   - `edge-ml` — edge inference, in-network ML, video analytics
   - `rl-training` — RL training infrastructure, RLHF, RLVR
   - `memory-disaggregation` — disaggregated memory, RDMA, DPU offloading

2. Load the matching `fragments/research_topic/*.md` file(s).

3. Use the loaded fragment(s) to present 3-10 curated paper recommendations. Each recommendation should include:
   - Paper title
   - One-sentence contribution summary (Chinese + English)
   - Conference and year
   - Links to presentation and PDF

4. If the user needs experiment design guidance (metrics, baselines, pitfalls), use the "实验指导 / Experiment Guide" section from the loaded fragment to provide:
   - Recommended metrics for the topic (with which papers use which metrics)
   - Standard baselines for fair comparison
   - Common experimental pitfalls to avoid
   - Typical hardware configurations

5. If the user wants more detail on a specific paper or the full paper list, load `references/paper-catalog.md`.

### 4. Reach for references only when needed

The files under `references/` are deep references, not defaults. Open them on demand per the `references.on_demand` table in the manifest:
- `references/full-catalog.md` — when the user wants complete tool descriptions
- `references/moltfounders-guide.md` — when the user asks about AI agent repo maintenance (Path C)
- `references/related-resources.md` — when the user wants related awesome lists and papers
- `references/paper-catalog.md` — when the user wants detailed paper metadata, full paper list, or asks about specific papers on systems topics
- `references/paper-writing-guide.md` — when the user asks about paper writing methodology, section structure, or reviewer expectations (Path E)
- `references/implementation-guide.md` — when the user asks about system implementation patterns, code organization, or framework modifications (Path F)

### 5. Cross-reference when useful

When recommending tools from a need fragment, you may also load the relevant category fragment to provide additional options. For example:
- `start-loop` need → also check `general-purpose` category
- `full-research` need → also check `research-agent` category
- `specific-hardware` need → also check `platform-port` category
- `evaluate-agent` need → also check `benchmark` category
- `learn-examples` need → also check `use-case` category

When the user's Path A need suggests deeper systems knowledge, cross-reference relevant papers:
- Autonomous experiment loops on GPU → suggest papers on `tensor-compiler`, `gpu-communication`
- LLM-related research automation → suggest papers on `llm-serving`, `llm-training`
- Distributed training tools → suggest papers on `gpu-communication`, `llm-training`
- Network/systems optimization → suggest papers on `network-ml`, `memory-disaggregation`
- RL-based agent training → suggest papers on `rl-training`
- Vector search / RAG → suggest papers on `vector-search`
- Hardware/GPU platform needs → suggest papers on `gpu-communication`, `tensor-compiler`

When the user asks about experiment design (how to set up benchmarks, what metrics to use, what baselines), load the relevant research_topic fragment and use the "实验指导 / Experiment Guide" section to recommend:
- Metrics: which metrics are standard for this topic and which papers use which metrics
- Baselines: standard systems/frameworks to compare against
- Pitfalls: common mistakes in experimental design for this topic

### 6. Paper pipeline: writing, implementation, and experiment planning

The skill now supports the full paper lifecycle via three additional capabilities:

**Path E — Paper Writing (论文写作指导)**:
When the user asks about paper writing ("怎么写Introduction"、"Evaluation section结构"、"系统论文写作模板"):
- Load `references/paper-writing-guide.md` for comprehensive writing methodology
- Load the relevant research_topic fragment and use the "写作指导 / Writing Guide" section for topic-specific tips
- Guide on: abstract patterns, introduction flow, design section organization, evaluation structure, related work, figure/table design, and reviewer expectation management

**Path F — Paper Implementation (论文实现指导)**:
When the user asks about implementation ("NCCL plugin怎么写"、"怎么修改vLLM"、"代码结构"):
- Load `references/implementation-guide.md` for general implementation patterns
- Load the relevant research_topic fragment and use the "实现指导 / Implementation Guide" section for topic-specific code patterns
- Cover: codebase organization, NCCL plugin patterns, CUDA kernel patterns, framework modification points, reproducibility

**Path G — Full Experiment Pipeline (完整实验流程)**:
When the user asks for complete experiment recipes ("LLM serving完整实验怎么做"、"需要跑哪些实验"、"实验checklist"):
- Load the relevant research_topic fragment and use the "实验流程 / Experiment Pipeline" section
- Provide step-by-step pipeline: hardware setup → model config → baseline testing → workload testing → metrics → ablation → generalization → analysis
- Each topic has a complete, numbered pipeline with concrete parameters

## Why this split

- The static layer is versioned and reviewable. Adding a new tool or category is one new file plus one manifest line.
- The dynamic layer keeps each invocation cheap: only the fragments relevant to the user's need enter context.
- The router itself is short on purpose. Update fragments, not this file, when adding scope.
