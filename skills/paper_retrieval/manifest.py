"""Manifest generation: CSV, JSON, README, failed downloads."""
from __future__ import annotations

import csv
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .models import DownloadStatus, Paper, RetrievalConfig, RetrievalResult

logger = logging.getLogger(__name__)

MANIFEST_FIELDS = [
    "index", "title", "authors", "venue", "year", "category",
    "session", "abstract", "official_page_url", "pdf_url",
    "arxiv_url", "source", "match_keywords", "match_reason",
    "local_pdf_path", "download_status", "file_size_bytes",
    "sha256", "downloaded_at", "notes",
]


def generate_manifest_csv(papers: list[Paper], output_path: Path) -> Path:
    """Generate manifest.csv."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for p in papers:
            row = {
                "index": p.index,
                "title": p.title,
                "authors": "; ".join(p.authors),
                "venue": p.venue,
                "year": p.year,
                "category": p.category,
                "session": p.session,
                "abstract": p.abstract[:500] if p.abstract else "",
                "official_page_url": p.official_page_url,
                "pdf_url": p.pdf_url,
                "arxiv_url": p.arxiv_url,
                "source": p.source.value,
                "match_keywords": "; ".join(p.match_keywords),
                "match_reason": p.match_reason,
                "local_pdf_path": p.local_pdf_path,
                "download_status": p.download_status.value,
                "file_size_bytes": p.file_size_bytes,
                "sha256": p.sha256,
                "downloaded_at": p.downloaded_at,
                "notes": p.notes,
            }
            writer.writerow(row)
    logger.info(f"Manifest CSV: {output_path} ({len(papers)} entries)")
    return output_path


def generate_manifest_json(papers: list[Paper], output_path: Path) -> Path:
    """Generate manifest.json."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    papers_data = []
    for p in papers:
        papers_data.append({
            "index": p.index,
            "title": p.title,
            "authors": p.authors,
            "venue": p.venue,
            "year": p.year,
            "category": p.category,
            "session": p.session,
            "abstract": p.abstract,
            "official_page_url": p.official_page_url,
            "pdf_url": p.pdf_url,
            "arxiv_url": p.arxiv_url,
            "source": p.source.value,
            "match_keywords": p.match_keywords,
            "match_reason": p.match_reason,
            "local_pdf_path": p.local_pdf_path,
            "download_status": p.download_status.value,
            "file_size_bytes": p.file_size_bytes,
            "sha256": p.sha256,
            "downloaded_at": p.downloaded_at,
            "notes": p.notes,
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"papers": papers_data, "count": len(papers)}, f, ensure_ascii=False, indent=2)
    logger.info(f"Manifest JSON: {output_path}")
    return output_path


def generate_failed_csv(
    papers: list[Paper],
    output_path: Path,
) -> Optional[Path]:
    """Generate failed_downloads.csv if there are failures."""
    failed = [p for p in papers if p.download_status == DownloadStatus.FAILED]
    if not failed:
        return None

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "index", "title", "pdf_url", "error", "official_page_url",
        ])
        writer.writeheader()
        for p in failed:
            writer.writerow({
                "index": p.index,
                "title": p.title,
                "pdf_url": p.pdf_url,
                "error": p.notes,
                "official_page_url": p.official_page_url,
            })
    logger.info(f"Failed downloads: {output_path} ({len(failed)} entries)")
    return output_path


def generate_readme(
    result: RetrievalResult,
    output_path: Path,
) -> Path:
    """Generate README.md with retrieval summary and paper table."""
    config = result.config
    papers = result.papers
    success = sum(1 for p in papers if p.download_status == DownloadStatus.SUCCESS)
    failed = sum(1 for p in papers if p.download_status == DownloadStatus.FAILED)
    no_pdf = sum(1 for p in papers if p.download_status == DownloadStatus.NO_PDF)
    skipped = sum(1 for p in papers if p.download_status == DownloadStatus.SKIPPED_EXISTING)

    lines = [
        f"# {config.normalized_venue} {config.year} — {config.normalized_category} Papers",
        "",
        "## Retrieval Task / 检索任务",
        "",
        f"- **Venue**: {config.normalized_venue}",
        f"- **Year**: {config.year}",
        f"- **Category**: {config.normalized_category}",
        f"- **Keywords**: {', '.join(config.keywords) if config.keywords else 'default'}",
        f"- **Run Time**: {result.finished_at or 'N/A'}",
        "",
        "## Summary / 概况",
        "",
        f"- **Total Matched**: {len(papers)}",
        f"- **Downloaded**: {success}",
        f"- **Failed**: {failed}",
        f"- **No PDF Available**: {no_pdf}",
        f"- **Skipped (Existing)**: {skipped}",
        "",
        "## Paper List / 论文列表",
        "",
        "| # | Title | Official Page | PDF | Local File | Match Reason | Status |",
        "|---|-------|--------------|-----|------------|--------------|--------|",
    ]

    for p in papers:
        title_short = p.title[:80] + ("..." if len(p.title) > 80 else "")
        page_link = f"[link]({p.official_page_url})" if p.official_page_url else "-"
        pdf_link = f"[PDF]({p.pdf_url})" if p.pdf_url else "-"
        local = Path(p.local_pdf_path).name if p.local_pdf_path else "-"
        reason = (p.match_reason or "")[:60]
        status_emoji = {
            DownloadStatus.SUCCESS: "✅",
            DownloadStatus.FAILED: "❌",
            DownloadStatus.SKIPPED_EXISTING: "⏭️",
            DownloadStatus.NO_PDF: "📄",
        }.get(p.download_status, "❓")

        lines.append(
            f"| {p.index} | {title_short} | {page_link} | {pdf_link} | {local} | {reason} | {status_emoji} |"
        )

    lines.extend([
        "",
        "## Usage / 使用说明",
        "",
        "### Re-download / 重新下载",
        "```bash",
        f"python -m paper_tool retrieve --venue {config.normalized_venue} \\",
        f"  --year {config.year} --category {config.normalized_category} \\",
        f"  --output-root {config.output_root} --force",
        "```",
        "",
        "### Re-run with additional keywords / 追加关键词",
        "```bash",
        f"python -m paper_tool retrieve --venue {config.normalized_venue} \\",
        f"  --year {config.year} --category {config.normalized_category} \\",
        "  --keywords 'new_keyword1,new_keyword2'",
        "```",
        "",
        "### Package / 打包",
        "```bash",
        f"python -m paper_tool archive --input-dir '{output_path.parent}' --output '{config.zip_name}'",
        "```",
        "",
        "### Manifest Files / 清单文件",
        f"- `manifest.csv` — Full metadata in CSV format",
        f"- `manifest.json` — Full metadata in JSON format",
        "- `failed_downloads.csv` — Failed downloads (if any)",
        "- `download.log` — Download log",
    ])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    logger.info(f"README: {output_path}")
    return output_path


def generate_all_manifests(
    result: RetrievalResult,
    output_dir: Path,
) -> RetrievalResult:
    """Generate all manifest files for a retrieval result."""
    result.manifest_csv = generate_manifest_csv(result.papers, output_dir / "manifest.csv")
    result.manifest_json = generate_manifest_json(result.papers, output_dir / "manifest.json")
    generate_failed_csv(result.papers, output_dir / "failed_downloads.csv")
    generate_readme(result, output_dir / "README.md")
    return result
