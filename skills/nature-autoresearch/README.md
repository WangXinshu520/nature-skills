# `nature-autoresearch` skill

An AI autonomous research tool recommendation and navigation skill. Recommends tools from the awesome-autoresearch catalog of 85+ projects, guides users on AI agent-based repo maintenance via MoltFounders rules, recommends and evaluates systems research papers from top conferences (NSDI 2026, OSDI 2025), provides experiment design guidance, and supports the full paper pipeline (writing, implementation, experiments).

Catalog source: [alvinunreal/awesome-autoresearch](https://github.com/alvinunreal/awesome-autoresearch)
Paper sources: NSDI 2026 (44 papers), OSDI 2025 (18 papers), RDMA (6 papers)

## File structure

```text
nature-autoresearch/
├── SKILL.md
├── README.md
├── manifest.yaml
├── static/
│   ├── core/
│   │   ├── stance.md
│   │   ├── workflow.md
│   │   └── taxonomy.md
│   └── fragments/
│       ├── category/
│       │   ├── general-purpose.md
│       │   ├── research-agent.md
│       │   ├── platform-port.md
│       │   ├── domain-specific.md
│       │   ├── benchmark.md
│       │   └── use-case.md
│       ├── need/
│       │   ├── start-loop.md
│       │   ├── full-research.md
│       │   ├── specific-hardware.md
│       │   ├── evaluate-agent.md
│       │   └── learn-examples.md
│       └── research_topic/
│           ├── llm-serving.md
│           ├── llm-training.md
│           ├── gpu-communication.md
│           ├── tensor-compiler.md
│           ├── vector-search.md
│           ├── network-ml.md
│           ├── edge-ml.md
│           ├── rl-training.md
│           └── memory-disaggregation.md
└── references/
    ├── full-catalog.md
    ├── moltfouders-guide.md
    ├── related-resources.md
    ├── paper-catalog.md
    ├── paper-writing-guide.md
    └── implementation-guide.md
```

## When to use

- Research automation needs: running autonomous experiments, auto-tuning, generating papers
- Tool discovery: browsing the catalog by category, platform, or domain
- Getting started with karpathy/autoresearch-style autonomous improvement loops
- Setting up AI agents to auto-maintain a GitHub repository via MoltFounders rules
- Evaluating AI agents on ML research benchmarks
- Learning from real-world autoresearch use cases (Shopify Liquid, biomechanics, trading, etc.)
- **Paper discovery**: finding systems research papers on LLM serving, training, GPU communication, tensor compilers, vector search, and more from top conferences
- **Paper evaluation**: getting evidence-based assessments of paper strengths, limitations, and practical impact with concrete experimental data
- **Experiment guidance**: getting experiment design recommendations (metrics, baselines, pitfalls) based on paper methodologies from top systems conferences
- **Paper writing**: getting systems paper writing methodology (abstract patterns, introduction flow, evaluation structure, reviewer expectations)
- **Paper implementation**: getting implementation pattern guidance (NCCL plugins, CUDA kernels, framework modifications, code organization)
- **Full experiment pipeline**: getting step-by-step experiment recipes from hardware setup to result analysis for all 9 research topics

## Design intent

The skill should:

- Recommend tools objectively without marketing superlatives
- Guide users to actual project repositories rather than reproducing usage from memory
- Cross-reference tools between user needs and tool categories for precise recommendations
- Teach MoltFounders agent maintenance as a practical, step-by-step process
- Recommend systems research papers with academic neutrality, linking to presentation and PDF
- Evaluate papers with evidence-based analysis (strengths, limitations, practical impact) citing specific experimental data
- Cross-reference relevant papers when recommending tools (e.g., GPU tools → GPU communication papers)
- Provide experiment design guidance (metrics, baselines, pitfalls) based on actual paper methodologies
- Guide paper writing with systems paper methodology (structure patterns, section templates, reviewer expectations)
- Guide system implementation with code-level patterns (NCCL plugins, CUDA kernels, framework extensions)
- Provide complete experiment pipelines with step-by-step instructions for all 9 research topics
- Keep Chinese and English content balanced throughout

## Routing (7 paths)

- **Path A (Smart Recommendation)**: User describes a concrete research automation need → detect `need` axis → load matching need fragment → cross-recommend tools from category fragments + papers from research_topic fragments
- **Path B (Catalog Browsing)**: User wants to browse → detect `category` axis → load matching category fragment → present tool list
- **Path C (MoltFounders Guide)**: User asks about AI agent repo maintenance → load `references/moltfounders-guide.md` directly
- **Path D (Paper Recommendation + Evaluation + Experiment Design)**: User asks about systems research papers → detect `research_topic` axis → load matching research_topic fragment → present curated papers + evidence-based evaluation + experiment guidance
- **Path E (Paper Writing)**: User asks about paper writing methodology → load `references/paper-writing-guide.md` + topic-specific writing tips
- **Path F (Paper Implementation)**: User asks about system implementation → load `references/implementation-guide.md` + topic-specific code patterns
- **Path G (Full Experiment Pipeline)**: User needs complete experiment recipes → load topic-specific experiment pipeline with step-by-step instructions

## Reference map

- `references/full-catalog.md`: Complete 85+ tool catalog with original descriptions, organized by 6 categories
- `references/moltfounders-guide.md`: 6-step guide for setting up AI agents to maintain GitHub repos, condensed from `.moltfounders/` rules
- `references/related-resources.md`: Curated awesome lists, surveys, and paper collections in the AI agent space
- `references/paper-catalog.md`: Full catalog of 68 systems research papers (NSDI 2026, OSDI 2025, RDMA) with titles, authors, contribution summaries, and links
- `references/paper-writing-guide.md`: Comprehensive systems paper writing methodology based on 68-paper structure analysis
- `references/implementation-guide.md`: System implementation patterns (NCCL plugins, CUDA kernels, framework modifications) from actual paper codebases

## Notes

- This skill is a recommendation and navigation system, not a replacement for the tools themselves
- The routing logic lives in `SKILL.md` and `manifest.yaml`; never apply recommendations from memory
- The fragments and manifest are designed to make adding new categories or need types a one-file + one-manifest-line operation
