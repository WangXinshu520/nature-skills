"""Tests for paper_retrieval module."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from paper_retrieval.config import (
    VENUES,
    CATEGORY_KEYWORDS,
    VenueInfo,
    get_category_keywords,
    get_venue_info,
    resolve_venue,
)
from paper_retrieval.filters import (
    MatchResult,
    _match_keywords,
    _normalize,
    filter_papers,
)
from paper_retrieval.models import (
    DownloadStatus,
    Paper,
    RetrievalConfig,
    RetrievalResult,
    SourceName,
)


# ── Models ────────────────────────────────────────────────────

class TestPaper:
    def test_safe_title(self):
        p = Paper(title="Hello: World's Best Paper!?")
        assert ":" not in p.safe_title
        assert "'" not in p.safe_title
        assert "?" not in p.safe_title
        assert "!" not in p.safe_title
        assert p.safe_title == "Hello_Worlds_Best_Paper"

    def test_safe_title_long(self):
        p = Paper(title="a" * 200)
        assert len(p.safe_title) <= 150

    def test_filename(self):
        p = Paper(index=3, title="My Paper")
        assert p.filename == "03_My_Paper.pdf"

    def test_filename_zero_pad(self):
        p = Paper(index=5, title="Test")
        assert p.filename == "05_Test.pdf"
        p.index = 12
        assert p.filename == "12_Test.pdf"


class TestRetrievalConfig:
    def test_normalized_venue(self):
        c = RetrievalConfig(venue="nsdi", year=2026, category="ai_sys")
        assert c.normalized_venue == "NSDI"

    def test_output_dir(self):
        c = RetrievalConfig(
            venue="NSDI", year=2026, category="ai_sys",
            output_root="/tmp/paper",
        )
        assert c.output_dir == Path("/tmp/paper/NSDI/2026/ai_sys")

    def test_zip_name(self):
        c = RetrievalConfig(venue="OSDI", year=2025, category="llm-serving")
        assert c.zip_name == "OSDI_2025_llm_serving_papers.zip"


# ── Config ────────────────────────────────────────────────────

class TestVenueConfig:
    def test_all_venues_have_sources(self):
        for name, vi in VENUES.items():
            assert vi.sources, f"{name} has no sources"
            assert vi.name == name

    def test_usenix_venues(self):
        for name in ["NSDI", "OSDI", "ATC", "FAST"]:
            vi = VENUES[name]
            assert vi.usenix_short
            assert vi.is_open_access

    def test_category_keywords(self):
        assert len(CATEGORY_KEYWORDS) >= 10
        for kws in CATEGORY_KEYWORDS.values():
            assert len(kws) > 0


class TestResolveVenue:
    def test_exact(self):
        assert resolve_venue("NSDI") == "NSDI"
        assert resolve_venue("nsdi") == "NSDI"
        assert resolve_venue(" osdi ") == "OSDI"

    def test_unknown(self):
        with pytest.raises(ValueError):
            resolve_venue("UNKNOWN_VENUE_12345")


class TestGetVenueInfo:
    def test_known(self):
        vi = get_venue_info("NSDI")
        assert vi is not None
        assert vi.full_name == "Symposium on Networked Systems Design and Implementation"

    def test_unknown(self):
        assert get_venue_info("UNKNOWN") is None


class TestCategoryKeywords:
    def test_known(self):
        kws = get_category_keywords("ai_sys")
        assert "LLM" in kws

    def test_unknown(self):
        assert get_category_keywords("nonexistent") == []


# ── Filters ───────────────────────────────────────────────────

class TestNormalize:
    def test_basic(self):
        assert _normalize("Hello World") == "hello world"

    def test_strip(self):
        assert _normalize("  text  ") == "text"


class TestMatchKeywords:
    def test_exact_match(self):
        score, matched, details = _match_keywords(
            "LLM serving for large language models",
            ["LLM serving"],
        )
        assert score > 0
        assert "LLM serving" in matched

    def test_phrase_match(self):
        score, matched, details = _match_keywords(
            "this paper is about large language model inference",
            ["large language model"],
        )
        assert score > 0

    def test_no_match(self):
        score, matched, details = _match_keywords(
            "some other topic",
            ["LLM", "GPU", "inference"],
        )
        assert score == 0.0
        assert len(matched) == 0

    def test_partial_match(self):
        score, matched, details = _match_keywords(
            "using GPU for computation",
            ["GPU memory"],
        )
        assert score > 0  # partial "GPU" match


class TestFilterPapers:
    def _paper(self, title: str, abstract: str = "", session: str = "") -> Paper:
        return Paper(
            index=1, title=title, abstract=abstract, session=session,
        )

    def test_filter_with_keywords(self):
        papers = [
            self._paper("LLM Serving at Scale", "We optimize KV cache"),
            self._paper("Unrelated Topic", "Completely different"),
            self._paper("GPU Communication for Training", "Uses all-reduce"),
        ]
        results = filter_papers(papers, keywords=["LLM", "GPU"])
        assert len(results) == 2
        assert "LLM" in results[0].matched_keywords or "GPU" in results[1].matched_keywords

    def test_filter_with_category(self):
        papers = [
            self._paper("Efficient LLM Inference", "serving models"),
            self._paper("Network Routing", "BGP protocol"),
        ]
        results = filter_papers(papers, keywords=[], category="llm_serving")
        assert len(results) == 1

    def test_filter_empty_keywords(self):
        papers = [self._paper("Test")]
        results = filter_papers(papers, keywords=[], category="")
        assert len(results) == 0


# ── Downloader helpers ────────────────────────────────────────

class TestDownloadStatus:
    def test_values(self):
        assert DownloadStatus.SUCCESS.value == "success"
        assert DownloadStatus.FAILED.value == "failed"


# ── Integration: dry run ──────────────────────────────────────

class TestRetrievePapers:
    def test_dry_run_nsdi(self):
        """Test that dry run works without crashing."""
        from paper_retrieval import retrieve_papers

        result = retrieve_papers(
            venue="NSDI",
            year=2026,
            category="ai_sys",
            keywords=["LLM serving"],
            dry_run=True,
            output_root="/tmp/paper_retrieval_test",
        )

        assert result.config.venue == "NSDI"
        assert result.config.year == 2026
        assert result.total >= 0
        # dry_run: nothing should be downloaded
        for p in result.papers:
            assert p.download_status == DownloadStatus.NO_PDF
