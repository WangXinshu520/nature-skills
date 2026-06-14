"""Data models for paper retrieval."""
from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional


class DownloadStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED_EXISTING = "skipped_existing"
    NO_PDF = "no_pdf"


class SourceName(str, Enum):
    USENIX = "usenix"
    ACM_DL = "acm_dl"
    ARXIV = "arxiv"
    DBLP = "dblp"
    SEMANTIC_SCHOLAR = "semantic_scholar"
    OPENREVIEW = "openreview"
    MANUAL = "manual"


@dataclass
class Paper:
    """A single paper entry."""
    index: int = 0
    title: str = ""
    authors: list[str] = field(default_factory=list)
    venue: str = ""
    year: int = 0
    category: str = ""
    session: str = ""
    abstract: str = ""
    official_page_url: str = ""
    pdf_url: str = ""
    arxiv_url: str = ""
    source: SourceName = SourceName.MANUAL
    match_keywords: list[str] = field(default_factory=list)
    match_reason: str = ""
    local_pdf_path: str = ""
    download_status: DownloadStatus = DownloadStatus.NO_PDF
    file_size_bytes: int = 0
    sha256: str = ""
    downloaded_at: str = ""
    notes: str = ""

    @property
    def safe_title(self) -> str:
        """Generate a filesystem-safe version of the title."""
        import re
        # Keep alphanumeric, spaces, underscores, hyphens
        s = re.sub(r'[^a-zA-Z0-9 _\-]', '', self.title)
        s = re.sub(r'\s+', '_', s)
        s = s.strip('_')
        # Remove duplicate underscores
        s = re.sub(r'_+', '_', s)
        # Limit length
        max_len = 150
        if len(s) > max_len:
            # Try to cut at a word boundary
            s = s[:max_len].rsplit('_', 1)[0]
        return s

    @property
    def filename(self) -> str:
        """Generate the PDF filename: {index:02d}_{safe_title}.pdf"""
        return f"{self.index:02d}_{self.safe_title}.pdf"

    def compute_sha256(self, filepath: Path) -> str:
        """Compute SHA-256 hash of a file."""
        sha = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                sha.update(chunk)
        return sha.hexdigest()


@dataclass
class RetrievalConfig:
    """Configuration for a retrieval run."""
    venue: str
    year: int
    category: str
    keywords: list[str] = field(default_factory=list)
    output_root: str = "/mnt/disk1/wangxinshu/wxs/docs/paper"
    max_papers: int = 0
    download_pdf: bool = True
    make_zip: bool = True
    force: bool = False
    dry_run: bool = False
    source_priority: list[SourceName] = field(default_factory=lambda: [
        SourceName.USENIX,
        SourceName.ACM_DL,
        SourceName.ARXIV,
        SourceName.DBLP,
        SourceName.SEMANTIC_SCHOLAR,
    ])
    retries: int = 3
    timeout: int = 60

    @property
    def normalized_venue(self) -> str:
        """Return uppercase venue name."""
        return self.venue.upper()

    @property
    def normalized_category(self) -> str:
        """Return lowercase category with underscores."""
        return self.category.lower().replace(" ", "_").replace("-", "_")

    @property
    def output_dir(self) -> Path:
        """Full output directory path."""
        return Path(self.output_root) / self.normalized_venue / str(self.year) / self.normalized_category

    @property
    def zip_name(self) -> str:
        """ZIP archive name."""
        return f"{self.normalized_venue}_{self.year}_{self.normalized_category}_papers.zip"


@dataclass
class RetrievalResult:
    """Result of a retrieval run."""
    config: RetrievalConfig
    output_dir: Path = field(default_factory=Path)
    manifest_csv: Path = field(default_factory=Path)
    manifest_json: Path = field(default_factory=Path)
    zip_path: Optional[Path] = None
    papers: list[Paper] = field(default_factory=list)
    total: int = 0
    success: int = 0
    failed: int = 0
    no_pdf: int = 0
    started_at: str = ""
    finished_at: str = ""

    @property
    def skipped_existing(self) -> int:
        return sum(1 for p in self.papers if p.download_status == DownloadStatus.SKIPPED_EXISTING)
