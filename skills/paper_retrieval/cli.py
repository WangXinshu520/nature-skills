"""CLI entry point: python -m paper_retrieval retrieve ..."""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from . import retrieve_papers
from .config import VENUES, CATEGORY_KEYWORDS
from .models import SourceName


def _setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def cmd_retrieve(args: argparse.Namespace) -> int:
    """Run a paper retrieval task."""
    _setup_logging(args.verbose)

    keywords = [kw.strip() for kw in args.keywords.split(",")] if args.keywords else []

    source_priority = None
    if args.sources:
        source_priority = []
        for s in args.sources.split(","):
            try:
                source_priority.append(SourceName(s.strip().lower()))
            except ValueError:
                print(f"Unknown source: {s} — valid: {[e.value for e in SourceName]}")
                return 1

    result = retrieve_papers(
        venue=args.venue,
        year=args.year,
        category=args.category or "",
        keywords=keywords,
        output_root=args.output_root,
        max_papers=args.max_papers,
        download_pdf=not args.no_download,
        make_zip=not args.no_zip,
        force=args.force,
        dry_run=args.dry_run,
        source_priority=source_priority,
        retries=args.retries,
        timeout=args.timeout,
    )

    print(f"\n{'='*60}")
    print(f"  Venue: {result.config.normalized_venue}")
    print(f"  Year: {result.config.year}")
    print(f"  Category: {result.config.normalized_category or 'none'}")
    print(f"  Keywords: {', '.join(result.config.keywords) or 'none'}")
    print(f"  Output: {result.output_dir}")
    print(f"  {'='*60}")
    print(f"  Total papers: {result.total}")
    print(f"  Downloaded:   {result.success}")
    print(f"  Failed:       {result.failed}")
    print(f"  No PDF:       {result.no_pdf}")
    print(f"  Skipped:      {result.skipped_existing}")
    print(f"  {'='*60}")
    if result.manifest_csv != Path():
        print(f"  Manifest CSV: {result.manifest_csv}")
    if result.manifest_json != Path():
        print(f"  Manifest JSON: {result.manifest_json}")
    if result.zip_path:
        print(f"  ZIP archive: {result.zip_path}")
    print()

    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """List known venues and categories."""
    if args.venues:
        print("\nKnown venues:")
        for name, vi in VENUES.items():
            print(f"  {name:12s} — {vi.full_name}")
            print(f"              Sources: {[s.value for s in vi.sources]}")
            print()
    elif args.categories:
        print("\nCategory keywords:")
        for cat, kws in CATEGORY_KEYWORDS.items():
            print(f"  {cat:25s} — {', '.join(kws[:8])}" + ("..." if len(kws) > 8 else ""))
        print()
    else:
        print("\nKnown venues:")
        for name, vi in VENUES.items():
            print(f"  {name:12s} — {vi.full_name}")
        print("\nCategories:")
        for cat in CATEGORY_KEYWORDS:
            print(f"  {cat}")
        print()
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="paper_tool",
        description="Automated paper retrieval, download, and manifest generation.",
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand")

    # retrieve
    retrieve = subparsers.add_parser("retrieve", help="Retrieve and download papers")
    retrieve.add_argument("--venue", required=True, help="Conference/journal name (e.g., NSDI, OSDI)")
    retrieve.add_argument("--year", type=int, required=True, help="Publication year")
    retrieve.add_argument("--category", default="", help="Category for keyword expansion")
    retrieve.add_argument("--keywords", default="", help="Comma-separated keywords")
    retrieve.add_argument("--output-root", default="/mnt/disk1/wangxinshu/wxs/docs/paper")
    retrieve.add_argument("--max-papers", type=int, default=0)
    retrieve.add_argument("--no-download", action="store_true", help="Skip PDF download")
    retrieve.add_argument("--no-zip", action="store_true", help="Skip ZIP archive")
    retrieve.add_argument("--force", action="store_true", help="Force re-download")
    retrieve.add_argument("--dry-run", action="store_true", help="Fetch and filter without download")
    retrieve.add_argument("--sources", default="", help="Comma-separated source priority")
    retrieve.add_argument("--retries", type=int, default=3)
    retrieve.add_argument("--timeout", type=int, default=60)
    retrieve.add_argument("--verbose", action="store_true")
    retrieve.set_defaults(func=cmd_retrieve)

    # list
    list_cmd = subparsers.add_parser("list", help="List venues and categories")
    list_cmd.add_argument("--venues", action="store_true")
    list_cmd.add_argument("--categories", action="store_true")
    list_cmd.set_defaults(func=cmd_list)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
