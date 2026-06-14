"""Semantic Scholar API paper source."""
from __future__ import annotations

import logging
import re
import time
from typing import Optional

import httpx

from ..config import VenueInfo
from ..models import Paper, SourceName

logger = logging.getLogger(__name__)

S2_API = "https://api.semanticscholar.org/graph/v1"


class SemanticScholarSource:
    """Semantic Scholar API for paper metadata."""

    name = SourceName.SEMANTIC_SCHOLAR

    def __init__(self, timeout: int = 60, retries: int = 3):
        self.timeout = timeout
        self.retries = retries
        self.client = httpx.Client(
            timeout=timeout,
            headers={"User-Agent": "PaperRetrieval/1.0 (research tool; academic use)"},
        )

    def search(self, query: str, year: str = "", limit: int = 100) -> list[dict]:
        """Search Semantic Scholar for papers."""
        params = {
            "query": query,
            "limit": min(limit, 100),
            "fields": "title,authors,year,venue,abstract,externalIds,url,openAccessPdf",
        }
        if year:
            params["year"] = year

        results = []
        for attempt in range(self.retries):
            try:
                resp = self.client.get(f"{S2_API}/paper/search", params=params)
                resp.raise_for_status()
                data = resp.json()
                for paper in data.get("data", []):
                    oa = paper.get("openAccessPdf", {}) or {}
                    ext_ids = paper.get("externalIds", {}) or {}
                    authors = [a.get("name", "") for a in paper.get("authors", [])]

                    results.append({
                        "title": paper.get("title", ""),
                        "authors": authors,
                        "year": paper.get("year", ""),
                        "venue": paper.get("venue", ""),
                        "abstract": paper.get("abstract", ""),
                        "url": paper.get("url", ""),
                        "arxiv_id": ext_ids.get("ArXiv", ""),
                        "doi": ext_ids.get("DOI", ""),
                        "pdf_url": oa.get("url", ""),
                    })
                break
            except Exception as e:
                logger.warning(f"S2 attempt {attempt + 1}/{self.retries} failed: {e}")
                if attempt < self.retries - 1:
                    time.sleep(2 ** attempt)
        return results

    def search_venue(self, venue_info: VenueInfo, year: int, limit: int = 200) -> list[dict]:
        """Search for papers from a specific venue/year."""
        query = f"{venue_info.full_name} {year}"
        return self.search(query, str(year), limit)

    def match_paper(self, paper: Paper) -> Optional[dict]:
        """Find Semantic Scholar entry matching a paper title."""
        results = self.search(paper.title[:200], limit=3)
        if not results:
            return None

        def normalize(s: str) -> str:
            s = s.lower().strip()
            s = re.sub(r'[^a-z0-9\s]', '', s)
            s = re.sub(r'\s+', ' ', s)
            return s

        paper_norm = normalize(paper.title)
        for cand in results:
            cand_norm = normalize(cand.get("title", ""))
            if paper_norm == cand_norm:
                return cand
            # Word overlap
            paper_words = set(paper_norm.split())
            cand_words = set(cand_norm.split())
            if paper_words and paper_words == cand_words:
                return cand
            if paper_words and len(paper_words & cand_words) / len(paper_words | cand_words) > 0.9:
                return cand
        return None
