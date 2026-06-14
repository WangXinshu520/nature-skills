"""USENIX conference paper scraper."""
from __future__ import annotations

import logging
import re
import time
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin, urlparse

import httpx

from ..config import VenueInfo
from ..models import Paper, SourceName

logger = logging.getLogger(__name__)

# USENIX proceedings URL pattern
USENIX_BASE = "https://www.usenix.org"


class UsenixSource:
    """Scraper for USENIX conference proceedings."""

    name = SourceName.USENIX

    def __init__(self, timeout: int = 60, retries: int = 3):
        self.timeout = timeout
        self.retries = retries
        self.client = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers={
                "User-Agent": "PaperRetrieval/1.0 (research tool; academic use)",
                "Accept": "text/html,application/xhtml+xml",
            },
        )

    def _url(self, venue_info: VenueInfo, year: int) -> str:
        """Build the proceedings URL."""
        short = f"{venue_info.usenix_short}{str(year)[-2:]}"
        return f"https://www.usenix.org/conference/{short}/technical-sessions"

    def fetch(self, venue_info: VenueInfo, year: int) -> list[Paper]:
        """Fetch all papers from a USENIX conference."""
        url = self._url(venue_info, year)
        logger.info(f"USENIX: Fetching {url}")

        papers = []
        for attempt in range(self.retries):
            try:
                resp = self.client.get(url)
                resp.raise_for_status()
                papers = self._parse_papers(resp.text, venue_info, year)
                break
            except httpx.HTTPError as e:
                logger.warning(f"USENIX attempt {attempt + 1}/{self.retries} failed: {e}")
                if attempt < self.retries - 1:
                    time.sleep(2 ** attempt)
                else:
                    logger.error(f"USENIX: All retries exhausted for {url}")
            except Exception as e:
                logger.error(f"USENIX: Unexpected error: {e}")
                break

        logger.info(f"USENIX: Found {len(papers)} papers")
        return papers

    def _parse_papers(self, html: str, venue_info: VenueInfo, year: int) -> list[Paper]:
        """Parse USENIX proceedings page HTML."""
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            logger.error("beautifulsoup4 is required for HTML parsing")
            return []

        soup = BeautifulSoup(html, "html.parser")
        papers = []
        seen_titles = set()
        index = 0
        short = f"{venue_info.usenix_short}{str(year)[-2:]}"
        current_session = ""

        # USENIX pages typically use <div class="view-content"> with links to presentations
        # Or use <article> or <div class="node--paper--teaser">
        # Strategy: find all links to /presentation/xxx

        # Find session headers
        for elem in soup.select("h2, h3, .session-title, .field--name-field-session, .paragraph--type--session"):
            text = elem.get_text(strip=True)
            if text and len(text) > 3 and len(text) < 200:
                current_session = text

        # Find all paper presentation links
        paper_links = []
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if "/presentation/" in href and href not in paper_links:
                paper_links.append(href)

        # Also look for <div class="views-row"> or article elements
        if not paper_links:
            # Try alternate USENIX layout: node teaser style
            for node in soup.select(".node--view-mode-teaser, .node--type-paper, .views-row"):
                link_elem = node.find("a", href=re.compile(r"/presentation/"))
                if link_elem:
                    href = link_elem["href"]
                    if href not in [p[0] if isinstance(p, tuple) else p for p in paper_links]:
                        paper_links.append(href)

        if not paper_links:
            logger.warning(f"USENIX: No paper links found on {self._url(venue_info, year)}")
            # Return empty - let other sources fill in
            return []

        for href in paper_links:
            full_url = urljoin(USENIX_BASE, href)

            # Try to get paper details from this page
            try:
                paper = self._parse_paper_page(full_url, venue_info, year, short, current_session)
                if paper and paper.title not in seen_titles:
                    index += 1
                    paper.index = index
                    seen_titles.add(paper.title)
                    papers.append(paper)
            except Exception as e:
                logger.warning(f"USENIX: Failed to parse paper page {full_url}: {e}")
                # Create minimal entry from URL
                slug = href.rstrip("/").split("/")[-1]
                title = slug.replace("-", " ").title()
                if title not in seen_titles:
                    index += 1
                    pdf_url = f"https://www.usenix.org/system/files/{short}-{slug}.pdf"
                    paper = Paper(
                        index=index,
                        title=title,
                        venue=venue_info.name,
                        year=year,
                        category="",
                        official_page_url=full_url,
                        pdf_url=pdf_url,
                        source=SourceName.USENIX,
                    )
                    seen_titles.add(title)
                    papers.append(paper)

            # Be polite - small delay between page fetches
            time.sleep(0.3)

        return papers

    def _parse_paper_page(
        self, url: str, venue_info: VenueInfo, year: int, short: str, session: str
    ) -> Optional[Paper]:
        """Parse a single USENIX paper presentation page."""
        try:
            resp = self.client.get(url)
            resp.raise_for_status()
        except Exception:
            return None

        soup = None
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(resp.text, "html.parser")
        except ImportError:
            return None
        if soup is None:
            return None

        # Extract title
        title = ""
        title_elem = soup.find("h1") or soup.find("title")
        if title_elem:
            title_text = title_elem.get_text(strip=True)
            # Remove " | USENIX" suffix
            title_text = re.sub(r'\s*\|?\s*USENIX\s*$', '', title_text)
            title = title_text[:300]

        # Extract authors
        authors = []
        for author_elem in soup.select(".field--name-field-presenters, .field--name-field-authors, .author, .field--name-field-paper-people"):
            author_text = author_elem.get_text(strip=True)
            authors = [a.strip() for a in re.split(r'[,;&]|\band\b', author_text) if a.strip()]
        if not authors:
            # Try meta tags
            for meta in soup.find_all("meta", attrs={"name": re.compile(r"citation_author", re.I)}):
                if meta.get("content"):
                    authors.append(meta["content"].strip())

        # Extract abstract
        abstract = ""
        abstract_elem = soup.select_one(".field--name-body, .field--name-field-paper-abstract, .abstract")
        if abstract_elem:
            abstract = abstract_elem.get_text(strip=True)[:2000]

        # Extract PDF URL
        pdf_url = ""
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.endswith(".pdf") and "/system/files/" in href:
                pdf_url = urljoin(USENIX_BASE, href)
                break
        if not pdf_url:
            # Try to construct from paper slug
            slug = url.rstrip("/").split("/")[-1]
            pdf_url = f"https://www.usenix.org/system/files/{short}-{slug}.pdf"

        # Try to get session info from the page
        page_session = session
        for elem in soup.select(".field--name-field-session, .session, .field--name-field-paper-session"):
            s = elem.get_text(strip=True)
            if s:
                page_session = s
                break

        return Paper(
            title=title,
            authors=authors,
            venue=venue_info.name,
            year=year,
            session=page_session,
            abstract=abstract,
            official_page_url=url,
            pdf_url=pdf_url,
            source=SourceName.USENIX,
        )

    def fetch_paper_page(self, url: str) -> Optional[Paper]:
        """Fetch a single paper page (used as fallback)."""
        try:
            resp = self.client.get(url)
            resp.raise_for_status()
        except Exception:
            return None

        soup = None
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(resp.text, "html.parser")
        except ImportError:
            return None
        if soup is None:
            return None

        title = ""
        title_elem = soup.find("h1") or soup.find("title")
        if title_elem:
            title_text = title_elem.get_text(strip=True)
            title_text = re.sub(r'\s*\|?\s*USENIX\s*$', '', title_text)
            title = title_text[:300]

        authors = []
        for meta in soup.find_all("meta", attrs={"name": re.compile(r"citation_author", re.I)}):
            if meta.get("content"):
                authors.append(meta["content"].strip())

        abstract = ""
        abstract_elem = soup.select_one(".field--name-body, .field--name-field-paper-abstract, .abstract")
        if abstract_elem:
            abstract = abstract_elem.get_text(strip=True)[:2000]

        pdf_url = ""
        for link in soup.find_all("a", href=True):
            if link["href"].endswith(".pdf"):
                pdf_url = urljoin(USENIX_BASE, link["href"])
                break

        return Paper(
            title=title,
            authors=authors,
            official_page_url=url,
            pdf_url=pdf_url,
            abstract=abstract,
            source=SourceName.USENIX,
        )
