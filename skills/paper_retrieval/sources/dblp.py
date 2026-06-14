"""DBLP paper source."""
from __future__ import annotations

import logging
import re
import time
from typing import Optional
from urllib.parse import urljoin

import httpx

from ..config import VenueInfo
from ..models import Paper, SourceName

logger = logging.getLogger(__name__)

DBLP_BASE = "https://dblp.org"
DBLP_SEARCH = "https://dblp.org/search/publ/api"


class DblpSource:
    """DBLP search API for paper metadata."""

    name = SourceName.DBLP

    def __init__(self, timeout: int = 60, retries: int = 3):
        self.timeout = timeout
        self.retries = retries
        self.client = httpx.Client(
            timeout=timeout,
            headers={"User-Agent": "PaperRetrieval/1.0 (research tool; academic use)"},
        )

    def search(self, venue_info: VenueInfo, year: int, max_results: int = 500) -> list[dict]:
        """Search DBLP for papers from a venue/year."""
        params = {
            "q": f"{venue_info.full_name} {year}",
            "format": "json",
            "h": max_results,
        }
        results = []
        for attempt in range(self.retries):
            try:
                resp = self.client.get(DBLP_SEARCH, params=params)
                resp.raise_for_status()
                data = resp.json()
                hits = data.get("result", {}).get("hits", {}).get("hit", [])
                for hit in hits:
                    info = hit.get("info", {})
                    results.append({
                        "title": info.get("title", ""),
                        "authors": self._parse_authors(info.get("authors", {})),
                        "year": info.get("year", year),
                        "venue_name": info.get("venue", ""),
                        "url": info.get("url", ""),
                        "doi": info.get("doi", ""),
                    })
                break
            except Exception as e:
                logger.warning(f"DBLP attempt {attempt + 1}/{self.retries} failed: {e}")
                if attempt < self.retries - 1:
                    time.sleep(2 ** attempt)
        return results

    def _parse_authors(self, authors_data: dict | list) -> list[str]:
        """Parse DBLP author data."""
        if isinstance(authors_data, dict):
            author = authors_data.get("author", [])
            if isinstance(author, list):
                return [a.get("text", "") for a in author]
            return [str(author)]
        if isinstance(authors_data, list):
            return [str(a) for a in authors_data]
        return []

    def papers_from_search(self, venue_info: VenueInfo, year: int) -> list[Paper]:
        """Get Paper objects from DBLP search results."""
        results = self.search(venue_info, year)
        papers = []
        seen_titles = set()
        index = 0

        for r in results:
            title = r.get("title", "")
            if not title or title in seen_titles:
                continue
            seen_titles.add(title)
            index += 1

            paper = Paper(
                index=index,
                title=title,
                authors=r.get("authors", []),
                venue=venue_info.name,
                year=year,
                official_page_url=r.get("url", ""),
                source=SourceName.DBLP,
            )
            papers.append(paper)

        return papers
