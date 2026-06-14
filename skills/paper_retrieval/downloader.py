"""PDF downloader with retry, validation, and error handling."""
from __future__ import annotations

import hashlib
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import httpx

from .models import DownloadStatus, Paper, RetrievalConfig

logger = logging.getLogger(__name__)

# PDF magic bytes
PDF_MAGIC = b"%PDF"
MAX_PDF_SIZE = 500 * 1024 * 1024  # 500 MB max


def validate_pdf(filepath: Path) -> bool:
    """Check if a file is a valid PDF by reading its header."""
    try:
        with open(filepath, "rb") as f:
            header = f.read(10)
        return header[:4] == PDF_MAGIC
    except Exception:
        return False


def compute_sha256(filepath: Path) -> str:
    """Compute SHA-256 hash of a file."""
    sha = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha.update(chunk)
        return sha.hexdigest()
    except Exception:
        return ""


def download_paper(
    paper: Paper,
    config: RetrievalConfig,
    output_dir: Path,
) -> Paper:
    """Download a single paper's PDF.

    Returns the paper with download status updated.
    """
    pdf_url = paper.pdf_url

    if not pdf_url:
        paper.download_status = DownloadStatus.NO_PDF
        paper.notes = "No PDF URL available"
        logger.info(f"[{paper.index}] No PDF URL: {paper.title[:60]}")
        return paper

    # Determine local file path
    filename = paper.filename
    filepath = output_dir / filename

    # Check if already exists
    if filepath.exists() and not config.force:
        if validate_pdf(filepath):
            paper.local_pdf_path = str(filepath)
            paper.download_status = DownloadStatus.SKIPPED_EXISTING
            paper.file_size_bytes = filepath.stat().st_size
            paper.sha256 = compute_sha256(filepath)
            paper.notes = "File already exists"
            logger.info(f"[{paper.index}] Skipped (exists): {filename}")
            return paper
        else:
            logger.warning(f"[{paper.index}] Invalid existing file, re-downloading: {filename}")

    if config.dry_run:
        paper.download_status = DownloadStatus.NO_PDF
        paper.notes = "Dry run - not downloaded"
        return paper

    # Download with retries
    client = httpx.Client(
        timeout=config.timeout,
        follow_redirects=True,
        headers={
            "User-Agent": "PaperRetrieval/1.0 (research tool; academic use)",
            "Accept": "application/pdf,*/*",
        },
    )

    success = False
    last_error = ""

    for attempt in range(config.retries):
        try:
            response = client.get(pdf_url)
            response.raise_for_status()

            # Check content
            content = response.content

            # Validate it's a PDF
            content_type = response.headers.get("content-type", "")
            if len(content) < 1000:
                last_error = f"Response too small: {len(content)} bytes"
                logger.warning(f"[{paper.index}] Attempt {attempt + 1}: {last_error}")
                continue

            if content[:4] != PDF_MAGIC and "application/pdf" not in content_type:
                # Could be HTML error page
                if b"<html" in content[:200].lower() or b"<!doctype" in content[:200].lower():
                    last_error = "Response is HTML, not PDF"
                    logger.warning(f"[{paper.index}] Attempt {attempt + 1}: {last_error}")
                    # Don't retry HTML responses - the URL is wrong
                    break
                last_error = f"Content-Type: {content_type}, not PDF magic"
                logger.warning(f"[{paper.index}] Attempt {attempt + 1}: {last_error}")
                continue

            if len(content) > MAX_PDF_SIZE:
                last_error = f"PDF too large: {len(content)} bytes"
                logger.warning(f"[{paper.index}] {last_error}")
                break

            # Save file
            filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(filepath, "wb") as f:
                f.write(content)

            # Validate saved file
            if not validate_pdf(filepath):
                last_error = "Saved file is not a valid PDF"
                logger.warning(f"[{paper.index}] {last_error}")
                filepath.unlink(missing_ok=True)
                continue

            success = True
            break

        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            last_error = f"HTTP {status}"
            if status in (403, 404):
                logger.warning(f"[{paper.index}] {last_error} - not retrying")
                break
            logger.warning(f"[{paper.index}] Attempt {attempt + 1}: {last_error}")
        except httpx.TimeoutException:
            last_error = f"Timeout after {config.timeout}s"
            logger.warning(f"[{paper.index}] Attempt {attempt + 1}: {last_error}")
        except Exception as e:
            last_error = str(e)[:200]
            logger.warning(f"[{paper.index}] Attempt {attempt + 1}: {last_error}")

        if attempt < config.retries - 1:
            time.sleep(2 ** attempt)

    if success:
        paper.local_pdf_path = str(filepath)
        paper.download_status = DownloadStatus.SUCCESS
        paper.file_size_bytes = filepath.stat().st_size
        paper.sha256 = compute_sha256(filepath)
        paper.downloaded_at = datetime.now(timezone.utc).isoformat()
        logger.info(f"[{paper.index}] Downloaded: {filename} ({paper.file_size_bytes} bytes)")
    else:
        paper.download_status = DownloadStatus.FAILED
        paper.notes = f"Download failed: {last_error}"
        logger.error(f"[{paper.index}] Failed: {paper.title[:60]} - {last_error}")

    return paper


def download_papers(
    papers: list[Paper],
    config: RetrievalConfig,
    output_dir: Path,
) -> list[Paper]:
    """Download PDFs for a list of papers."""
    results = []
    for paper in papers:
        try:
            updated = download_paper(paper, config, output_dir)
            results.append(updated)
        except Exception as e:
            logger.error(f"[{paper.index}] Unexpected error: {e}")
            paper.download_status = DownloadStatus.FAILED
            paper.notes = f"Unexpected error: {str(e)[:200]}"
            results.append(paper)
    return results
