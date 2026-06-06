#!/usr/bin/env python
"""Create an auditable Hermes run folder from the checked-in template."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_TEMPLATE = Path("data/raw/hermes_runs/_template")
DEFAULT_RUN_ROOT = Path("data/raw/hermes_runs")
RUN_ID_PATTERN = re.compile(r"^run-[0-9]{8}-[0-9]{6}(?:-[a-z0-9][a-z0-9-]*)?$")


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return slug[:80]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def make_run_id(now: datetime, suffix: str | None) -> str:
    run_id = f"run-{now:%Y%m%d-%H%M%S}"
    if suffix:
        run_id = f"{run_id}-{slugify(suffix)}"
    return run_id


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--purpose", required=True, help="Short purpose of this run")
    parser.add_argument(
        "--suffix",
        help="Optional slug suffix for the run id, such as harness-audit-01",
    )
    parser.add_argument("--operator", default="Codex", help="Run operator")
    parser.add_argument(
        "--mode",
        choices=["interactive", "oneshot"],
        default="interactive",
        help="Hermes session mode",
    )
    parser.add_argument("--session-id", help="Hermes session id when known")
    parser.add_argument("--model", help="Hermes model when known")
    parser.add_argument("--provider", help="Hermes provider when known")
    parser.add_argument(
        "--template",
        default=str(DEFAULT_TEMPLATE),
        help="Template directory to copy",
    )
    parser.add_argument(
        "--run-root",
        default=str(DEFAULT_RUN_ROOT),
        help="Directory where run folders are created",
    )
    parser.add_argument(
        "--run-id",
        help="Explicit run id. Must match run-YYYYMMDD-HHMMSS[-slug]",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    template = Path(args.template)
    run_root = Path(args.run_root)
    metadata_template = template / "00_metadata.json"

    if not metadata_template.is_file():
        raise SystemExit(f"Missing template metadata: {metadata_template}")

    now = utc_now()
    run_id = args.run_id or make_run_id(now, args.suffix)
    if not RUN_ID_PATTERN.match(run_id):
        raise SystemExit(
            "Invalid run id. Expected run-YYYYMMDD-HHMMSS or "
            "run-YYYYMMDD-HHMMSS-slug"
        )

    run_dir = run_root / run_id
    if run_dir.exists():
        raise SystemExit(f"Run directory already exists: {run_dir}")

    run_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, run_dir)
    metadata = load_json(run_dir / "00_metadata.json")
    metadata["run_id"] = run_id
    metadata["created_at"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    metadata["workspace"] = str(Path.cwd())
    metadata["operator"] = args.operator
    metadata["purpose"] = args.purpose
    metadata["hermes_session"] = {
        "session_id": args.session_id,
        "mode": args.mode,
        "model": args.model,
        "provider": args.provider,
    }
    write_json(run_dir / "00_metadata.json", metadata)

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
