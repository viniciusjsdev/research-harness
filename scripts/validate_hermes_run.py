#!/usr/bin/env python
"""Validate Hermes run folders against the harness logging contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


OFFICIAL_ROLES = {
    "Research Lead",
    "Literature Scout",
    "Methodology Reviewer",
    "Devil's Advocate",
    "Angel Advocate",
    "Argument Arbiter",
    "Evidence Auditor",
    "Experiment Designer",
    "Research Scribe",
}

VALID_STATUSES = {"planned", "completed", "skipped", "failed"}
CURATED_DESTINATIONS = ("reports/", "memory/", "skills/", "prompts/", "schemas/")
IGNORED_FILES = {".gitkeep"}


class Reporter:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def load_json(path: Path, reporter: Reporter) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        reporter.error(f"Missing metadata file: {path}")
        return None
    except json.JSONDecodeError as exc:
        reporter.error(f"Invalid JSON in {path}: {exc}")
        return None
    if not isinstance(payload, dict):
        reporter.error(f"Metadata root must be an object: {path}")
        return None
    return payload


def has_real_files(path: Path) -> bool:
    if not path.is_dir():
        return False
    return any(item.is_file() and item.name not in IGNORED_FILES for item in path.iterdir())


def source_exists(run_dir: Path, source: str) -> bool:
    source_path = Path(source)
    if source_path.is_absolute():
        return source_path.exists()
    return (run_dir / source_path).exists() or source_path.exists()


def validate_role_entry(
    run_dir: Path, entry: Any, index: int, reporter: Reporter
) -> Path | None:
    if not isinstance(entry, dict):
        reporter.error(f"roles[{index}] must be an object")
        return None

    role = entry.get("role")
    status = entry.get("status")
    profile_dir_value = entry.get("profile_dir")
    step = entry.get("step")

    if not isinstance(step, int) or step < 1:
        reporter.error(f"roles[{index}].step must be a positive integer")
    if role not in OFFICIAL_ROLES:
        reporter.error(f"roles[{index}].role is not official: {role!r}")
    if status not in VALID_STATUSES:
        reporter.error(f"roles[{index}].status is invalid: {status!r}")
    if not isinstance(profile_dir_value, str):
        reporter.error(f"roles[{index}].profile_dir must be a string")
        return None

    profile_dir = run_dir / profile_dir_value
    input_dir = run_dir / str(entry.get("input_dir", ""))
    output_dir = run_dir / str(entry.get("output_dir", ""))
    artifacts_dir = run_dir / str(entry.get("artifacts_dir", ""))

    for label, path in (
        ("profile_dir", profile_dir),
        ("input_dir", input_dir),
        ("output_dir", output_dir),
        ("artifacts_dir", artifacts_dir),
    ):
        if not path.is_dir():
            reporter.error(f"roles[{index}].{label} does not exist: {path}")

    if status == "completed":
        if not has_real_files(input_dir):
            reporter.error(f"Completed role has no captured input files: {input_dir}")
        if not has_real_files(output_dir):
            reporter.error(f"Completed role has no captured output files: {output_dir}")
    if status == "skipped" and (has_real_files(input_dir) or has_real_files(output_dir)):
        reporter.warn(f"Skipped role has captured input/output files: {profile_dir}")

    return profile_dir


def validate_promotions(run_dir: Path, metadata: dict[str, Any], reporter: Reporter) -> None:
    promotions = metadata.get("artifacts_promoted", [])
    if not isinstance(promotions, list):
        reporter.error("artifacts_promoted must be a list")
        return

    for index, promotion in enumerate(promotions):
        if not isinstance(promotion, dict):
            reporter.error(f"artifacts_promoted[{index}] must be an object")
            continue
        source = promotion.get("source_file")
        destination = promotion.get("destination_file")
        if not isinstance(source, str) or not source:
            reporter.error(f"artifacts_promoted[{index}].source_file must be a string")
        elif not source_exists(run_dir, source):
            reporter.warn(f"Promoted source is not present: {source}")
        if not isinstance(destination, str) or not destination:
            reporter.error(
                f"artifacts_promoted[{index}].destination_file must be a string"
            )
        elif not destination.startswith(CURATED_DESTINATIONS):
            reporter.error(
                "Promoted destination must be under reports/, memory/, skills/, "
                f"prompts/, or schemas/: {destination}"
            )


def validate_run(run_dir: Path) -> Reporter:
    reporter = Reporter()
    metadata = load_json(run_dir / "00_metadata.json", reporter)
    if metadata is None:
        return reporter

    run_id = metadata.get("run_id")
    if run_dir.name != "_template" and run_id != run_dir.name:
        reporter.error(f"metadata.run_id does not match folder name: {run_id!r}")

    roles = metadata.get("roles")
    if not isinstance(roles, list) or not roles:
        reporter.error("metadata.roles must be a non-empty list")
        roles = []

    referenced_profiles: set[Path] = set()
    seen_steps: set[int] = set()
    seen_roles: set[str] = set()
    for index, entry in enumerate(roles):
        if isinstance(entry, dict):
            step = entry.get("step")
            role = entry.get("role")
            if isinstance(step, int):
                if step in seen_steps:
                    reporter.error(f"Duplicate role step: {step}")
                seen_steps.add(step)
            if isinstance(role, str):
                if role in seen_roles:
                    reporter.warn(f"Role appears more than once: {role}")
                seen_roles.add(role)
        profile_dir = validate_role_entry(run_dir, entry, index, reporter)
        if profile_dir is not None:
            referenced_profiles.add(profile_dir.resolve())

    profiles_root = run_dir / "profiles"
    if not profiles_root.is_dir():
        reporter.error(f"Missing profiles directory: {profiles_root}")
    else:
        for profile_dir in sorted(path for path in profiles_root.iterdir() if path.is_dir()):
            if profile_dir.resolve() not in referenced_profiles:
                reporter.warn(f"Profile directory is not listed in metadata: {profile_dir}")

    validate_promotions(run_dir, metadata, reporter)
    return reporter


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", help="Hermes run directory to validate")
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="Exit non-zero when warnings are present",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    run_dir = Path(args.run_dir)
    reporter = validate_run(run_dir)

    for warning in reporter.warnings:
        print(f"WARN: {warning}")
    for error in reporter.errors:
        print(f"ERROR: {error}")

    if reporter.errors:
        print(
            f"Validation failed: {len(reporter.errors)} error(s), "
            f"{len(reporter.warnings)} warning(s)"
        )
        return 1
    if args.warnings_as_errors and reporter.warnings:
        print(f"Validation failed: {len(reporter.warnings)} warning(s)")
        return 1

    print(f"Validation passed: {run_dir}")
    if reporter.warnings:
        print(f"Warnings: {len(reporter.warnings)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
