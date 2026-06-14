"""ZIP archiver for retrieval output directory."""

from __future__ import annotations

import logging
import zipfile
from pathlib import Path
from typing import Optional

from .models import DownloadStatus, RetrievalResult

logger = logging.getLogger(__name__)

MAX_ZIP_SIZE = 2 * 1024 * 1024 * 1024  # 2 GB warning threshold


def archive_result(
    result: RetrievalResult,
    output_path: Optional[Path] = None,
) -> Optional[Path]:
    """Package a retrieval result directory into a ZIP archive.

    Skips archiving if no PDFs were successfully downloaded.
    """
    papers = result.papers
    success_pdfs = [
        p for p in papers
        if p.download_status in (DownloadStatus.SUCCESS, DownloadStatus.SKIPPED_EXISTING)
    ]

    if not success_pdfs:
        logger.info("No PDFs to archive")
        return None

    output_dir = result.output_dir
    if output_path is None:
        output_path = output_dir.parent / result.config.zip_name

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(str(output_path), "w", zipfile.ZIP_DEFLATED) as zf:
        # Add PDFs
        for p in success_pdfs:
            if p.local_pdf_path:
                filepath = Path(p.local_pdf_path)
                if filepath.exists():
                    zf.write(str(filepath), f"{output_dir.name}/{filepath.name}")

        # Add manifest files
        for manifest_name in ["manifest.csv", "manifest.json", "README.md"]:
            path = output_dir / manifest_name
            if path.exists():
                zf.write(str(path), f"{output_dir.name}/{manifest_name}")

        # Add failed downloads if present
        failed_path = output_dir / "failed_downloads.csv"
        if failed_path.exists():
            zf.write(str(failed_path), f"{output_dir.name}/failed_downloads.csv")

    zip_size = output_path.stat().st_size
    if zip_size > MAX_ZIP_SIZE:
        logger.warning(f"ZIP file is large: {zip_size / (1024**3):.1f} GB")

    result.zip_path = output_path
    logger.info(f"Archive: {output_path} ({zip_size} bytes, {len(success_pdfs)} PDFs)")
    return output_path
