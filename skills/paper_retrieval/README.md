# Paper Retrieval Module

Automated paper retrieval, download, and manifest generation for top systems venues (NSDI, OSDI, SOSP, SIGCOMM, etc.).

## Quick Start

### CLI Usage

```bash
# Dry-run (no downloads)
python -m paper_retrieval.cli retrieve --venue NSDI --year 2026 --category ai_sys --dry-run

# With keywords
python -m paper_retrieval.cli retrieve --venue NSDI --year 2026 --category ai_sys --keywords "LLM serving,GPU,inference"

# Real download
python -m paper_retrieval.cli retrieve --venue NSDI --year 2026 --category ai_sys

# Force re-download
python -m paper_retrieval.cli retrieve --venue OSDI --year 2025 --category llm_serving --force

# List available venues and categories
python -m paper_retrieval.cli list
python -m paper_retrieval.cli list --venues
python -m paper_retrieval.cli list --categories
```

### Python API

```python
from paper_retrieval import retrieve_papers

result = retrieve_papers(
    venue="NSDI",
    year=2026,
    category="ai_sys",
    keywords=["LLM serving", "GPU"],
    dry_run=True,
)
print(f"Found {result.total} papers")
for p in result.papers:
    print(f"  {p.index}. {p.title}")
```

## Directory Structure

After a successful retrieval run (`NSDI 2026 ai_sys`):

```
/mnt/disk1/wangxinshu/wxs/docs/paper/
└── NSDI/
    └── 2026/
        ├── ai_sys/
        │   ├── README.md
        │   ├── manifest.csv
        │   ├── manifest.json
        │   ├── failed_downloads.csv   (if any failures)
        │   ├── 01_Paper_Title_One.pdf
        │   ├── 02_Paper_Title_Two.pdf
        │   └── ...
        └── NSDI_2026_ai_sys_papers.zip
```

## Supported Venues

| Venue | Source | Open Access |
|-------|--------|-------------|
| NSDI | USENIX | Yes |
| OSDI | USENIX | Yes |
| ATC | USENIX | Yes |
| FAST | USENIX | Yes |
| SOSP | ACM DL (arXiv fallback) | No |
| SIGCOMM | ACM DL (arXiv fallback) | No |
| SIGMOD | ACM DL (arXiv fallback) | No |
| EuroSys | ACM DL (arXiv fallback) | No |
| ASPLOS | ACM DL (arXiv fallback) | No |
| MLSys | OpenReview | Yes |
| VLDB | DBLP | Yes |

## Keyword Categories

| Category | Description |
|----------|-------------|
| `ai_sys` | General AI systems (LLM, GPU, training, inference) |
| `ml_sys` | Machine learning systems |
| `rdma` | RDMA, RoCE, SmartNIC, CXL |
| `llm_serving` | LLM inference serving |
| `distributed_training` | Distributed model training |
| `networking_for_ai` | AI cluster networking |
| `tensor_compiler` | Tensor compilers and kernel optimization |
| `vector_search` | Vector similarity search / ANN |
| `edge_ml` | Edge/in-network ML |
| `memory_disaggregation` | Memory disaggregation |
| `rl_training` | RL training / RLHF / post-training |

## Manifest Fields

The `manifest.csv` contains 20+ fields per paper:

| Field | Description |
|-------|-------------|
| `index` | Sequential paper number |
| `title` | Paper title |
| `authors` | Semicolon-separated author list |
| `venue` | Conference/journal name |
| `year` | Publication year |
| `category` | Keyword category |
| `session` | Conference session |
| `abstract` | Abstract (first 500 chars) |
| `official_page_url` | Link to paper page |
| `pdf_url` | Direct PDF link |
| `arxiv_url` | arXiv link |
| `source` | Data source (usenix/dblp/arxiv/semantic_scholar) |
| `match_keywords` | Matched keywords |
| `match_reason` | Why the paper matched |
| `local_pdf_path` | Local PDF file path |
| `download_status` | success/failed/no_pdf/skipped_existing |
| `file_size_bytes` | PDF file size |
| `sha256` | SHA-256 hash of PDF |
| `downloaded_at` | Download timestamp |
| `notes` | Error messages or status notes |

## Options

| Flag | Description |
|------|-------------|
| `--venue` | Conference/journal name |
| `--year` | Publication year |
| `--category` | Category for keyword expansion |
| `--keywords` | Comma-separated filter keywords |
| `--output-root` | Base output directory |
| `--max-papers N` | Limit to N papers |
| `--no-download` | Skip PDF download |
| `--no-zip` | Skip ZIP archive |
| `--force` | Force re-download |
| `--dry-run` | Fetch + filter only, no downloads |
| `--sources` | Source priority (comma-separated) |
| `--retries N` | Download retry count (default: 3) |
| `--timeout N` | HTTP timeout seconds (default: 60) |
| `--verbose` | Debug logging |

## Dependencies

```
httpx
beautifulsoup4
pytest (for tests)
```
