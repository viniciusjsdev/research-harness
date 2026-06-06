#!/usr/bin/env python
"""Search public academic indexes and save normalized paper metadata.

This script intentionally uses only the Python standard library so the harness
can run before a full dependency stack exists.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


OPENALEX_ENDPOINT = "https://api.openalex.org/works"
ARXIV_ENDPOINT = "https://export.arxiv.org/api/query"
_SSL_CONTEXT: ssl.SSLContext | None = None


@dataclass
class PaperRecord:
    source: str
    title: str
    authors: list[str]
    year: int | None
    venue: str | None
    doi: str | None
    url: str | None
    abstract: str | None
    source_id: str | None
    relevance_confidence: str = "low"


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent()})
    with urllib.request.urlopen(request, timeout=30, context=ssl_context()) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_text(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": user_agent()})
    with urllib.request.urlopen(request, timeout=30, context=ssl_context()) as response:
        return response.read().decode("utf-8", errors="replace")


def user_agent() -> str:
    mailto = os.getenv("OPENALEX_MAILTO") or os.getenv("CROSSREF_MAILTO")
    if mailto:
        return f"research-harness/0.1 (mailto:{mailto})"
    return "research-harness/0.1"


def ssl_context() -> ssl.SSLContext:
    """Return an SSL context, using certifi when available.

    Some Windows Python installs do not have a complete local issuer chain for
    public HTTPS APIs. certifi is optional and keeps verification enabled.
    """

    global _SSL_CONTEXT
    if _SSL_CONTEXT is not None:
        return _SSL_CONTEXT
    try:
        import certifi  # type: ignore

        _SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        _SSL_CONTEXT = ssl.create_default_context()
    return _SSL_CONTEXT


def reconstruct_openalex_abstract(index: dict | None) -> str | None:
    if not index:
        return None
    positions: list[tuple[int, str]] = []
    for word, offsets in index.items():
        for offset in offsets:
            positions.append((offset, word))
    if not positions:
        return None
    return " ".join(word for _, word in sorted(positions))


def clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    return re.sub(r"\s+", " ", value).strip()


def search_openalex(query: str, limit: int) -> list[PaperRecord]:
    params = {
        "search": query,
        "per-page": str(limit),
        "sort": "relevance_score:desc",
    }
    mailto = os.getenv("OPENALEX_MAILTO")
    if mailto:
        params["mailto"] = mailto
    url = f"{OPENALEX_ENDPOINT}?{urllib.parse.urlencode(params)}"
    payload = fetch_json(url)
    records: list[PaperRecord] = []

    for item in payload.get("results", []):
        authors = [
            authorship.get("author", {}).get("display_name", "")
            for authorship in item.get("authorships", [])
        ]
        authors = [author for author in authors if author]
        doi = item.get("doi")
        if isinstance(doi, str) and doi.startswith("https://doi.org/"):
            doi = doi.removeprefix("https://doi.org/")
        records.append(
            PaperRecord(
                source="openalex",
                title=clean_text(item.get("display_name")) or "",
                authors=authors,
                year=item.get("publication_year"),
                venue=clean_text(
                    (item.get("primary_location") or {})
                    .get("source", {})
                    .get("display_name")
                ),
                doi=doi,
                url=item.get("id") or item.get("landing_page_url"),
                abstract=reconstruct_openalex_abstract(
                    item.get("abstract_inverted_index")
                ),
                source_id=item.get("id"),
                relevance_confidence="medium",
            )
        )
    return records


def search_arxiv(query: str, limit: int) -> list[PaperRecord]:
    params = {
        "search_query": f"all:{query}",
        "start": "0",
        "max_results": str(limit),
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_ENDPOINT}?{urllib.parse.urlencode(params)}"
    text = fetch_text(url)
    root = ET.fromstring(text)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "arxiv": "http://arxiv.org/schemas/atom",
    }
    records: list[PaperRecord] = []
    for entry in root.findall("atom:entry", ns):
        title = clean_text(entry.findtext("atom:title", default="", namespaces=ns)) or ""
        summary = clean_text(entry.findtext("atom:summary", default="", namespaces=ns))
        authors = [
            clean_text(author.findtext("atom:name", default="", namespaces=ns)) or ""
            for author in entry.findall("atom:author", ns)
        ]
        authors = [author for author in authors if author]
        published = entry.findtext("atom:published", default="", namespaces=ns)
        year = int(published[:4]) if published[:4].isdigit() else None
        arxiv_id = entry.findtext("atom:id", default="", namespaces=ns)
        doi = entry.findtext("arxiv:doi", default="", namespaces=ns) or None
        records.append(
            PaperRecord(
                source="arxiv",
                title=title,
                authors=authors,
                year=year,
                venue="arXiv",
                doi=doi,
                url=arxiv_id or None,
                abstract=summary,
                source_id=arxiv_id or None,
                relevance_confidence="medium",
            )
        )
    return records


def dedupe(records: Iterable[PaperRecord]) -> list[PaperRecord]:
    seen: set[str] = set()
    output: list[PaperRecord] = []
    for record in records:
        key = (record.doi or record.url or record.title).lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(record)
    return output


def save_results(query: str, records: list[PaperRecord], out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", query).strip("-").lower()[:80] or "query"
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    path = out_dir / f"{timestamp}-{slug}.json"
    payload = {
        "query": query,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "count": len(records),
        "records": [asdict(record) for record in records],
    }
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def print_table(records: list[PaperRecord]) -> None:
    for index, record in enumerate(records, start=1):
        year = record.year or "????"
        doi = f" doi:{record.doi}" if record.doi else ""
        print(f"{index:02d}. [{record.source}] {year} - {record.title}{doi}")
        if record.url:
            print(f"    {record.url}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Results per source")
    parser.add_argument(
        "--source",
        choices=["all", "openalex", "arxiv"],
        default="all",
        help="Source to search",
    )
    parser.add_argument(
        "--out",
        default="data/raw",
        help="Output directory for JSON search snapshots",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    records: list[PaperRecord] = []
    if args.source in {"all", "openalex"}:
        records.extend(search_openalex(args.query, args.limit))
    if args.source in {"all", "arxiv"}:
        records.extend(search_arxiv(args.query, args.limit))
    records = dedupe(records)
    path = save_results(args.query, records, Path(args.out))
    print_table(records)
    print(f"\nSaved {len(records)} records to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
