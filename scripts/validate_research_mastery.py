#!/usr/bin/env python3
"""Validate the medical research mastery repository bootstrap."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "research-mastery/CODEX-CONTINUOUS-MISSION.md",
    "research-mastery/data/codex-task-queue.csv",
    "scripts/codex_orchestrator.py",
    "scripts/build_research_mastery_status.py",
]
FORBIDDEN = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip", ".rar", ".7z", ".rds", ".rda", ".RData", ".sqlite", ".db", ".bam", ".fastq", ".fq", ".vcf"}


def main() -> int:
    errors: list[str] = []
    for name in REQUIRED:
        path = ROOT / name
        if not path.exists():
            errors.append(f"missing required file: {name}")
        elif path.is_file() and not path.read_text(encoding="utf-8").strip():
            errors.append(f"empty required file: {name}")

    queue = ROOT / "research-mastery" / "data" / "codex-task-queue.csv"
    if queue.exists():
        with queue.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        if len(rows) < 32:
            errors.append(f"task queue should contain at least 32 tasks; found {len(rows)}")

    for path in ROOT.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file() and path.suffix.lower() in FORBIDDEN:
            errors.append(f"forbidden research-data or binary extension: {path.relative_to(ROOT)}")

    result = subprocess.run([sys.executable, "scripts/codex_orchestrator.py", "validate"], cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        errors.append((result.stderr or result.stdout).strip())

    if errors:
        print("Research mastery validation FAILED:", file=sys.stderr)
        for index, error in enumerate(errors, 1):
            print(f"{index}. {error}", file=sys.stderr)
        return 1
    print("Research mastery validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
