"""arXiv API paper source."""
from __future__ import annotations

import logging
import re
import time
import xml.etree.ElementTree as ET
from typing import Optional
from urllib.parse import urlencode

import httpx

from ..models import Paper, SourceName

logger = logging.getLogger(__name__)

ARXIV_API = "https://export.arxiv.org/api/query"


class ArxivSource:
    """arXiv API search and fetch."""

    name = SourceName.ARXIV

    def __init__(self, timeout: int = 60, retries: int = 3):
        self.timeout = timeout
        self.retries = retries
        self.client = httpx.Client(
            timeout=timeout,
            headers={"User-Agent": "PaperRetrieval/1.0 (research tool; academic use)"},
        )

    def search_by_title(self, title: str, max_results: int = 3) -> list[dict]:
        """Search arXiv for papers matching a title. Returns list of result dicts."""
        # Clean the title for search
        clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', title)
        clean = re.sub(r'\s+', ' ', clean).strip()

        params = {
            "search_query": f"ti:{clean[:200]}",
            "max_results": max_results,
            "sortBy": "relevance",
        }

        results = []
        for attempt in range(self.retries):
            try:
                resp = self.client.get(ARXIV_API, params=params)
                resp.raise_for_status()
                results = self._parse_response(resp.text)
                break
            except Exception as e:
                logger.warning(f"arXiv attempt {attempt + 1}/{self.retries} failed: {e}")
                if attempt < self.retries - 1:
                    time.sleep(2 ** attempt)

        return results

    def match_paper(self, paper: Paper) -> Optional[dict]:
        """Find arXiv version of a paper by title matching.

        Returns best match if title similarity > 0.85, else None.
        """
        candidates = self.search_by_title(paper.title, max_results=3)
        if not candidates:
            return None

        # Normalize titles for comparison
        def normalize(s: str) -> str:
            s = s.lower().strip()
            s = re.sub(r'[^a-z0-9\s]', '', s)
            s = re.sub(r'\s+', ' ', s)
            return s

        paper_norm = normalize(paper.title)

        best_score = 0.0
        best_match = None
        for cand in candidates:
            cand_title = cand.get("title", "")
            cand_norm = normalize(cand_title)

            # Simple word overlap score
            paper_words = set(paper_norm.split())
            cand_words = set(cand_norm.split())
            if not paper_words:
                continue

            if paper_norm == cand_norm:
                best_score = 1.0
                best_match = cand
                break

            overlap = len(paper_words & cand_words)
            union = len(paper_words | cand_words)
            score = overlap / union if union > 0 else 0

            if score > best_score:
                best_score = score
                best_match = cand

        if best_score >= 0.85 and best_match:
            return best_match
        return None

    def fetch_pdf_url(self, arxiv_id: str) -> str:
        """Get the PDF URL for an arXiv ID."""
        arxiv_id = arxiv_id.replace("http://arxiv.org/abs/", "").replace("arxiv:", "")
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

    def _parse_response(self, xml_text: str) -> list[dict]:
        """Parse arXiv API XML response."""
        results = []
        try:
            root = ET.fromstring(xml_text)
            ns = {
                "atom": "http://www.w3.org/2005/Atom",
                "arxiv": "http://arxiv.org/schemas/atom",
            }
            for entry in root.findall("atom:entry", ns):
                title_elem = entry.find("atom:title", ns)
                summary_elem = entry.find("atom:summary", ns)
                id_elem = entry.find("atom:id", ns)
                pdf_link = None

                for link in entry.findall("atom:link", ns):
                    if link.get("title") == "pdf":
                        pdf_link = link.get("href")
                        break
                if not pdf_link:
                    for link in entry.findall("atom:link", ns):
                        href = link.get("href", "")
                        if "pdf" in href.lower():
                            pdf_link = href
                            break

                authors = []
                for author in entry.findall("atom:author", ns):
                    name = author.find("atom:name", ns)
                    if name is not None and name.text:
                        authors.append(name.text)

                arxiv_id = ""
                if id_elem is not None and id_elem.text:
                    arxiv_id = id_elem.text.split("/abs/")[-1]

                results.append({
                    "title": title_elem.text.strip() if title_elem is not None and title_elem.text else "",
                    "summary": summary_elem.text.strip()[:2000] if summary_elem is not None and summary_elem.text else "",
                    "authors": authors,
                    "arxiv_id": arxiv_id,
                    "arxiv_url": f"https://arxiv.org/abs/{arxiv_id}",
                    "pdf_url": pdf_link or self.fetch_pdf_url(arxiv_id),
                })
        except ET.ParseError as e:
            logger.error(f"arXiv XML parse error: {e}")
        return results
