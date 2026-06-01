#!/usr/bin/env python
"""Extract text from PDFs into local generated data.

The script requires pypdf:

    pip install pypdf

Raw PDFs and extracted text are ignored by Git by default.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path


def require_pypdf():
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: pypdf. Install with: pip install pypdf"
        ) from exc
    return PdfReader


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_pdfs(path: Path) -> list[Path]:
    if path.is_file() and path.suffix.lower() == ".pdf":
        return [path]
    if path.is_dir():
        return sorted(path.glob("*.pdf"))
    raise SystemExit(f"No PDF file or directory found: {path}")


def extract_pdf(pdf_path: Path, out_dir: Path) -> dict:
    PdfReader = require_pypdf()
    reader = PdfReader(str(pdf_path))
    pages: list[str] = []
    for index, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append(f"\n\n--- Page {index} ---\n\n{text.strip()}")

    digest = sha256_file(pdf_path)
    stem = f"{pdf_path.stem}-{digest[:12]}"
    text_path = out_dir / f"{stem}.txt"
    meta_path = out_dir / f"{stem}.metadata.json"
    out_dir.mkdir(parents=True, exist_ok=True)
    text_path.write_text("".join(pages).strip() + "\n", encoding="utf-8")

    metadata = {
        "source_path": str(pdf_path),
        "sha256": digest,
        "pages": len(reader.pages),
        "text_path": str(text_path),
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return metadata


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="PDF file or directory containing PDFs")
    parser.add_argument(
        "--out",
        default="data/processed/pdf_text",
        help="Output directory for extracted text",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    source = Path(args.path)
    out_dir = Path(args.out)
    pdfs = iter_pdfs(source)
    if not pdfs:
        print(f"No PDFs found in {source}")
        return 0
    for pdf in pdfs:
        metadata = extract_pdf(pdf, out_dir)
        print(f"Extracted {pdf} -> {metadata['text_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
