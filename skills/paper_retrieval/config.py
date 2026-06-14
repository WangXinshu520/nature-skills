"""Venue mappings, default keywords, and category configurations."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .models import SourceName


@dataclass
class VenueInfo:
    """Metadata for a conference/journal venue."""
    name: str
    full_name: str
    sources: list[SourceName] = field(default_factory=list)
    usenix_short: str = ""          # e.g., "nsdi26"
    acm_venue_id: str = ""          # ACM DL venue identifier
    dblp_venue_id: str = ""         # DBLP venue key
    proceedings_url: str = ""       # URL to accepted papers / proceedings
    is_open_access: bool = True
    notes: str = ""


# Venue registry
VENUES: dict[str, VenueInfo] = {
    "NSDI": VenueInfo(
        name="NSDI",
        full_name="Symposium on Networked Systems Design and Implementation",
        sources=[SourceName.USENIX, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        usenix_short="nsdi",
        dblp_venue_id="conf/nsdi",
        proceedings_url="https://www.usenix.org/conference/nsdi{year_short}/technical-sessions",
        is_open_access=True,
    ),
    "OSDI": VenueInfo(
        name="OSDI",
        full_name="Operating Systems Design and Implementation",
        sources=[SourceName.USENIX, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        usenix_short="osdi",
        dblp_venue_id="conf/osdi",
        proceedings_url="https://www.usenix.org/conference/osdi{year_short}/technical-sessions",
        is_open_access=True,
    ),
    "ATC": VenueInfo(
        name="ATC",
        full_name="USENIX Annual Technical Conference",
        sources=[SourceName.USENIX, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        usenix_short="atc",
        dblp_venue_id="conf/usenix",
        proceedings_url="https://www.usenix.org/conference/atc{year_short}/technical-sessions",
        is_open_access=True,
    ),
    "FAST": VenueInfo(
        name="FAST",
        full_name="USENIX Conference on File and Storage Technologies",
        sources=[SourceName.USENIX, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        usenix_short="fast",
        dblp_venue_id="conf/fast",
        proceedings_url="https://www.usenix.org/conference/fast{year_short}/technical-sessions",
        is_open_access=True,
    ),
    "SOSP": VenueInfo(
        name="SOSP",
        full_name="Symposium on Operating Systems Principles",
        sources=[SourceName.ACM_DL, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="conf/sosp",
        acm_venue_id="SOSP",
        proceedings_url="https://dl.acm.org/doi/proceedings/10.1145/{acm_doi_prefix}",
        is_open_access=False,
        notes="ACM DL papers may require subscription; use arXiv fallback",
    ),
    "SIGCOMM": VenueInfo(
        name="SIGCOMM",
        full_name="ACM SIGCOMM Conference",
        sources=[SourceName.ACM_DL, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="conf/sigcomm",
        acm_venue_id="SIGCOMM",
        proceedings_url="https://dl.acm.org/doi/proceedings/10.1145/{acm_doi_prefix}",
        is_open_access=False,
        notes="ACM DL papers may require subscription",
    ),
    "SIGMOD": VenueInfo(
        name="SIGMOD",
        full_name="ACM SIGMOD International Conference on Management of Data",
        sources=[SourceName.ACM_DL, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="conf/sigmod",
        acm_venue_id="SIGMOD",
        proceedings_url="https://dl.acm.org/doi/proceedings/10.1145/{acm_doi_prefix}",
        is_open_access=False,
    ),
    "EuroSys": VenueInfo(
        name="EuroSys",
        full_name="European Conference on Computer Systems",
        sources=[SourceName.ACM_DL, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="conf/eurosys",
        proceedings_url="https://dl.acm.org/doi/proceedings/10.1145/{acm_doi_prefix}",
        is_open_access=False,
    ),
    "ASPLOS": VenueInfo(
        name="ASPLOS",
        full_name="Architectural Support for Programming Languages and Operating Systems",
        sources=[SourceName.ACM_DL, SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="conf/asplos",
        proceedings_url="https://dl.acm.org/doi/proceedings/10.1145/{acm_doi_prefix}",
        is_open_access=False,
    ),
    "MLSys": VenueInfo(
        name="MLSys",
        full_name="Machine Learning and Systems",
        sources=[SourceName.OPENREVIEW, SourceName.DBLP, SourceName.ARXIV],
        proceedings_url="https://proceedings.mlsys.org/",
        is_open_access=True,
    ),
    "VLDB": VenueInfo(
        name="VLDB",
        full_name="Very Large Data Bases",
        sources=[SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="journals/pvldb",
        proceedings_url="https://www.vldb.org/pvldb/",
        is_open_access=True,
    ),
    "INFOCOM": VenueInfo(
        name="INFOCOM",
        full_name="IEEE International Conference on Computer Communications",
        sources=[SourceName.DBLP, SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR],
        dblp_venue_id="conf/infocom",
        proceedings_url="https://infocom.info/",
        is_open_access=False,
        notes="IEEE Xplore — DBLP for metadata, arXiv for open-access PDFs",
    ),
}


# Category to default keywords mapping
CATEGORY_KEYWORDS: dict[str, list[str]] = {
    "ai_sys": [
        "LLM", "large language model", "serving", "inference", "training",
        "GPU", "accelerator", "tensor", "KV cache", "MoE",
        "reinforcement learning", "RL", "collective communication",
        "all-reduce", "all-to-all", "model parallelism", "pipeline parallelism",
        "disaggregated", "vector search", "agent", "video analytics",
        "AI network", "ML system", "deep learning", "transformer",
        "attention", "fine-tuning", "quantization", "distillation",
        "prompt", "RAG", "generation", "embedding",
    ],
    "ml_sys": [
        "machine learning", "deep learning", "training", "inference",
        "GPU", "accelerator", "tensor", "compiler", "kernel",
        "distributed", "parallel", "federated", "privacy", "quantization",
        "sparsity", "pipeline", "data loading", "profiling",
        "checkpoint", "memory", "auto-tuning", "AutoML",
    ],
    "rdma": [
        "RDMA", "RoCE", "RNIC", "Soft-RDMA", "DPU", "SmartNIC",
        "CXL", "memory disaggregation", "one-sided", "verbs",
        "InfiniBand", "collective communication", "congestion control",
        "remote memory", "NVM", "persistent memory",
    ],
    "llm_serving": [
        "LLM serving", "KV cache", "inference", "batching", "scheduling",
        "prefill", "decode", "disaggregated serving", "SLO",
        "throughput", "latency", "token", "generation",
        "autoscaling", "serverless", "model serving",
    ],
    "distributed_training": [
        "training", "distributed training", "data parallel", "tensor parallel",
        "pipeline parallel", "MoE", "RLHF", "RL",
        "checkpointing", "straggler", "all-reduce", "collective",
        "gradient", "synchronization", "fault tolerance",
    ],
    "networking_for_ai": [
        "AI network", "GPU cluster", "collective communication",
        "training network", "inference network", "scale-up network",
        "scale-out network", "congestion", "routing", "traffic engineering",
        "telemetry", "topology", "fabric", "interconnect", "network design",
    ],
    "tensor_compiler": [
        "tensor", "compiler", "kernel", "optimization", "code generation",
        "superoptimizer", "profiling", "auto-tuning", "TVM", "XLA",
        "CUDA", "GPU program", "IR", "lowering", "fusion",
        "schedule", "tiling", "vectorization",
    ],
    "vector_search": [
        "vector search", "ANN", "index", "RAG", "embedding",
        "similarity search", "nearest neighbor", "HNSW", "IVF",
        "quantization", "graph-based", "LSH", "approximate",
        "retrieval", "database",
    ],
    "edge_ml": [
        "edge", "in-network", "mobile", "embedded", "IoT",
        "video analytics", "smart camera", "real-time",
        "Jetson", "Raspberry Pi", "low-power", "bandwidth",
        "compression", "adaptive", "streaming",
    ],
    "memory_disaggregation": [
        "memory disaggregation", "remote memory", "RDMA",
        "CXL", "far memory", "swap", "paging", "prefetching",
        "memory pool", "memory tiering", "NVM", "DPU",
    ],
    "rl_training": [
        "reinforcement learning", "RLHF", "RLVR", "PPO",
        "reward model", "rollout", "policy", "value function",
        "GRPO", "REINFORCE", "post-training",
    ],
}

# Empty dict for undefined categories
_EMPTY_KEYWORDS: list[str] = []  # noqa: F811


def get_category_keywords(category: str) -> list[str]:
    """Get default keywords for a category."""
    return CATEGORY_KEYWORDS.get(category, _EMPTY_KEYWORDS)


def get_venue_info(venue: str) -> Optional[VenueInfo]:
    """Get venue info by normalized name."""
    return VENUES.get(venue.upper())


def resolve_venue(name: str) -> str:
    """Resolve a venue name to the canonical form."""
    name_upper = name.upper().strip()
    if name_upper in VENUES:
        return name_upper
    # Try fuzzy matching
    for key, vi in VENUES.items():
        if name_upper in vi.full_name.upper() or vi.full_name.upper().startswith(name_upper):
            return key
    raise ValueError(f"Unknown venue: {name}. Known venues: {list(VENUES.keys())}")
