"""Paper Retrieval Module — automated paper search, download, and manifest generation.

Usage::

    from paper_retrieval import retrieve_papers

    result = retrieve_papers(
        venue="NSDI",
        year=2026,
        category="ai_sys",
        keywords=["LLM serving", "GPU"],
        dry_run=True,
    )
"""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from .archive import archive_result
from .config import get_venue_info, resolve_venue
from .downloader import download_papers
from .filters import filter_papers
from .manifest import generate_all_manifests
from .models import (
    DownloadStatus,
    Paper,
    RetrievalConfig,
    RetrievalResult,
    SourceName,
)
from .sources import UsenixSource, DblpSource, ArxivSource, SemanticScholarSource

__all__ = [
    "retrieve_papers",
    "DownloadStatus",
    "Paper",
    "RetrievalConfig",
    "RetrievalResult",
    "SourceName",
    "get_venue_info",
    "resolve_venue",
]

logger = logging.getLogger(__name__)


def _fetch_papers(config: RetrievalConfig) -> list[Paper]:
    """Fetch papers from sources in priority order."""
    venue_info = get_venue_info(config.venue)
    if venue_info is None:
        raise ValueError(f"Unknown venue: {config.venue}")

    all_papers: list[Paper] = []
    seen_titles: set[str] = set()

    for source_name in config.source_priority:
        if source_name not in venue_info.sources:
            continue

        try:
            if source_name == SourceName.USENIX and venue_info.usenix_short:
                source = UsenixSource(timeout=config.timeout, retries=config.retries)
                papers = source.fetch(venue_info, config.year)
            elif source_name == SourceName.DBLP and venue_info.dblp_venue_id:
                source = DblpSource(timeout=config.timeout, retries=config.retries)
                papers = source.papers_from_search(venue_info, config.year)
            elif source_name == SourceName.ARXIV:
                source = ArxivSource(timeout=config.timeout, retries=config.retries)
                papers = []
                # arXiv is used for enrichment, not primary fetch
                continue
            elif source_name == SourceName.SEMANTIC_SCHOLAR:
                source = SemanticScholarSource(timeout=config.timeout, retries=config.retries)
                raw = source.search_venue(venue_info, config.year, limit=200)
                papers = []
                for i, r in enumerate(raw):
                    title = r.get("title", "")
                    if not title or title in seen_titles:
                        continue
                    papers.append(Paper(
                        index=i + 1,
                        title=title,
                        authors=r.get("authors", []),
                        venue=venue_info.name,
                        year=r.get("year", config.year),
                        abstract=r.get("abstract", ""),
                        pdf_url=r.get("pdf_url", ""),
                        arxiv_url=f"https://arxiv.org/abs/{r.get('arxiv_id', '')}" if r.get("arxiv_id") else "",
                        official_page_url=r.get("url", ""),
                        source=SourceName.SEMANTIC_SCHOLAR,
                    ))
            else:
                continue

            # Deduplicate and add
            new_count = 0
            for p in papers:
                title_key = p.title.lower().strip()
                if title_key and title_key not in seen_titles:
                    seen_titles.add(title_key)
                    all_papers.append(p)
                    new_count += 1

            logger.info(f"  {source_name.value}: {new_count} papers")

        except Exception as e:
            logger.warning(f"  {source_name.value}: failed — {e}")

    # Re-index
    for i, p in enumerate(all_papers):
        p.index = i + 1

    logger.info(f"Total unique papers: {len(all_papers)}")
    return all_papers


def _enrich_papers(papers: list[Paper], config: RetrievalConfig) -> list[Paper]:
    """Enrich papers with arXiv metadata (abstract, PDF URL)."""
    try:
        arxiv = ArxivSource(timeout=config.timeout, retries=config.retries)
    except Exception:
        return papers

    for p in papers:
        if p.abstract and p.pdf_url:
            continue
        try:
            match = arxiv.match_paper(p)
            if match:
                if not p.abstract:
                    p.abstract = match.get("abstract", "")
                if not p.pdf_url:
                    p.pdf_url = match.get("pdf_url", "")
                if not p.arxiv_url:
                    p.arxiv_url = match.get("arxiv_url", "")
        except Exception:
            pass

    return papers


def retrieve_papers(
    venue: str,
    year: int,
    category: str = "",
    keywords: Optional[list[str]] = None,
    output_root: str = "/mnt/disk1/wangxinshu/wxs/docs/paper",
    max_papers: int = 0,
    download_pdf: bool = True,
    make_zip: bool = True,
    force: bool = False,
    dry_run: bool = False,
    source_priority: Optional[list[SourceName]] = None,
    retries: int = 3,
    timeout: int = 60,
) -> RetrievalResult:
    """Retrieve, filter, download, and archive papers from a venue.

    Args:
        venue: Conference/journal name (e.g., "NSDI", "OSDI").
        year: Publication year.
        category: Category for keyword expansion.
        keywords: User-provided keywords for filtering.
        output_root: Base output directory.
        max_papers: Maximum number of papers (0 = unlimited).
        download_pdf: Whether to download PDFs.
        make_zip: Whether to create a ZIP archive.
        force: Force re-download even if files exist.
        dry_run: Fetch and filter without downloading.
        source_priority: Override source priority order.
        retries: Number of download retries.
        timeout: HTTP timeout in seconds.

    Returns:
        RetrievalResult with papers, manifest paths, and statistics.
    """
    resolved_venue = resolve_venue(venue)

    if source_priority is None:
        vi = get_venue_info(resolved_venue)
        if vi:
            source_priority = vi.sources
        else:
            source_priority = [
                SourceName.USENIX, SourceName.DBLP,
                SourceName.ARXIV, SourceName.SEMANTIC_SCHOLAR,
            ]

    config = RetrievalConfig(
        venue=resolved_venue,
        year=year,
        category=category,
        keywords=keywords or [],
        output_root=output_root,
        max_papers=max_papers,
        download_pdf=download_pdf,
        make_zip=make_zip,
        force=force,
        dry_run=dry_run,
        source_priority=source_priority,
        retries=retries,
        timeout=timeout,
    )

    output_dir = config.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    result = RetrievalResult(
        config=config,
        output_dir=output_dir,
        started_at=datetime.now(timezone.utc).isoformat(),
    )

    # Step 1: Fetch
    logger.info(f"=== Fetching papers: {resolved_venue} {year} ===")
    papers = _fetch_papers(config)

    if not papers:
        logger.warning("No papers found from any source")
        result.finished_at = datetime.now(timezone.utc).isoformat()
        return result

    # Step 2: Filter
    logger.info(f"=== Filtering papers ===")
    if config.keywords or config.category:
        matches = filter_papers(
            papers,
            keywords=config.keywords,
            category=config.category,
        )
        papers = []
        for mr in matches:
            p = mr.paper
            p.match_keywords = mr.matched_keywords
            p.match_reason = "; ".join(mr.match_details)
            p.category = config.category
            papers.append(p)

        if config.max_papers > 0:
            papers = papers[:config.max_papers]

        logger.info(f"Filtered: {len(papers)} papers match criteria")
    else:
        # No filtering: take all
        for p in papers:
            p.category = config.category
        if config.max_papers > 0:
            papers = papers[:config.max_papers]

    # Step 3: Enrich
    logger.info(f"=== Enriching papers (arXiv) ===")
    papers = _enrich_papers(papers, config)

    # Step 4: Download
    if config.download_pdf and not config.dry_run:
        logger.info(f"=== Downloading PDFs ===")
        papers = download_papers(papers, config, output_dir)
    elif config.dry_run:
        for p in papers:
            if p.pdf_url:
                p.download_status = DownloadStatus.NO_PDF
                p.notes = "Dry run — not downloaded"
            else:
                p.download_status = DownloadStatus.NO_PDF
                p.notes = "No PDF URL (dry run)"

    result.papers = papers
    result.total = len(papers)
    result.success = sum(1 for p in papers if p.download_status == DownloadStatus.SUCCESS)
    result.failed = sum(1 for p in papers if p.download_status == DownloadStatus.FAILED)
    result.no_pdf = sum(1 for p in papers if p.download_status == DownloadStatus.NO_PDF)

    # Step 5: Generate manifests
    logger.info(f"=== Generating manifests ===")
    generate_all_manifests(result, output_dir)

    # Step 6: Archive
    if config.make_zip and not config.dry_run:
        logger.info(f"=== Creating archive ===")
        archive_result(result)

    result.finished_at = datetime.now(timezone.utc).isoformat()

    # Summary
    logger.info(f"=== Done: {config.normalized_venue} {config.year} {config.normalized_category} ===")
    logger.info(f"  Total: {result.total}")
    logger.info(f"  Success: {result.success}")
    logger.info(f"  Failed: {result.failed}")
    logger.info(f"  No PDF: {result.no_pdf}")
    logger.info(f"  Skipped: {result.skipped_existing}")
    logger.info(f"  Output: {output_dir}")

    return result
