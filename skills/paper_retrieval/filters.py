"""Paper filtering by keyword matching."""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

from .config import get_category_keywords
from .models import Paper

logger = logging.getLogger(__name__)


# Weight multipliers
TITLE_WEIGHT = 3.0
ABSTRACT_WEIGHT = 1.5
SESSION_WEIGHT = 1.0
USER_KEYWORD_WEIGHT = 5.0  # User-provided keywords get highest priority


@dataclass
class MatchResult:
    """Result of matching a paper against keywords."""
    paper: Paper
    score: float
    matched_keywords: list[str] = field(default_factory=list)
    match_details: list[str] = field(default_factory=list)


def _normalize(text: str) -> str:
    """Normalize text for keyword matching."""
    return text.lower().strip()


def _tokenize(text: str) -> list[str]:
    """Split text into tokens for matching."""
    return re.findall(r'[a-zA-Z0-9]+', text.lower())


def _match_keywords(text: str, keywords: list[str]) -> tuple[float, list[str], list[str]]:
    """Match keywords in text. Returns (score, matched_keywords, details)."""
    score = 0.0
    matched = []
    details = []
    text_lower = _normalize(text)
    text_tokens = set(_tokenize(text))

    for kw in keywords:
        kw_lower = _normalize(kw)
        kw_tokens = set(_tokenize(kw))

        # Exact match (case insensitive)
        if kw_lower in text_lower:
            score += 1.0
            matched.append(kw)
            details.append(f"exact:{kw}")
            continue

        # Phrase match: all tokens present in order
        if len(kw_tokens) > 1 and all(t in text_tokens for t in kw_tokens):
            score += 0.8
            matched.append(kw)
            details.append(f"phrase:{kw}")
            continue

        # Partial token match
        kw_token_list = _tokenize(kw)
        matched_count = sum(1 for t in kw_token_list if t in text_tokens)
        if matched_count > 0:
            partial_score = matched_count / len(kw_token_list)
            score += partial_score * 0.5
            matched.append(kw)
            details.append(f"partial({partial_score:.1f}):{kw}")

    return score, matched, details


def filter_papers(
    papers: list[Paper],
    keywords: list[str],
    category: str = "",
    min_score: float = 1.0,
) -> list[MatchResult]:
    """Filter papers by keyword relevance.

    Args:
        papers: List of papers to filter.
        keywords: User-provided keywords (highest priority).
        category: Category name for default keyword expansion.
        min_score: Minimum score to include a paper.

    Returns:
        Sorted list of MatchResult objects (highest score first).
    """
    # Combine categories
    all_keywords = list(set(keywords))

    # Add category defaults
    if category:
        cat_keywords = get_category_keywords(category)
        all_keywords.extend(kw for kw in cat_keywords if kw not in all_keywords)

    if not all_keywords:
        logger.warning("No keywords specified for filtering")
        return []

    results = []
    for paper in papers:
        score = 0.0
        matched = []
        details = []

        # Title match (highest weight)
        title_score, title_matched, title_details = _match_keywords(paper.title, all_keywords)
        score += title_score * TITLE_WEIGHT
        matched.extend(title_matched)
        details.extend(title_details)

        # User keywords get extra boost
        if keywords:
            user_score, user_matched, user_details = _match_keywords(paper.title, keywords)
            if user_score > 0:
                score += user_score * USER_KEYWORD_WEIGHT
                details.append(f"user_keyword_in_title:{user_matched}")

            user_abs_score, user_abs_matched, user_abs_details = _match_keywords(
                paper.abstract, keywords
            )
            if user_abs_score > 0:
                score += user_abs_score * USER_KEYWORD_WEIGHT * 0.5
                details.append(f"user_keyword_in_abstract:{user_abs_matched}")

        # Abstract match (medium weight)
        if paper.abstract:
            abs_score, abs_matched, abs_details = _match_keywords(paper.abstract, all_keywords)
            score += abs_score * ABSTRACT_WEIGHT
            matched.extend(abs_matched)
            details.extend(abs_details)

        # Session name match (lower weight)
        if paper.session:
            sess_score, sess_matched, sess_details = _match_keywords(paper.session, all_keywords)
            score += sess_score * SESSION_WEIGHT
            matched.extend(sess_matched)
            details.extend(sess_details)

        if score >= min_score:
            deduped = list(dict.fromkeys(matched))  # preserve order, remove dupes
            results.append(MatchResult(
                paper=paper,
                score=score,
                matched_keywords=deduped,
                match_details=details,
            ))

    # Sort by score descending
    results.sort(key=lambda r: r.score, reverse=True)

    return results
