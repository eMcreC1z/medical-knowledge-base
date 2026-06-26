#!/usr/bin/env python3
"""Validate and select the next Codex task."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "research-mastery" / "data" / "codex-task-queue.csv"
HEADER = [
    "task_id", "phase", "sprint", "module", "priority", "depends_on", "status",
    "title", "deliverables", "acceptance", "human_review", "last_updated",
]
STATUSES = {"not-started", "in-progress", "evidence-ready", "completed", "blocked"}
READY = {"evidence-ready", "completed"}


@dataclass(frozen=True)
class Task:
    task_id: str
    priority: int
    depends_on: tuple[str, ...]
    status: str
    row: dict[str, str]


def load() -> tuple[list[Task], list[dict[str, str]]]:
    with QUEUE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            raise ValueError(f"bad queue header: {reader.fieldnames!r}")
        rows = list(reader)
    tasks: list[Task] = []
    for line, row in enumerate(rows, 2):
        try:
            priority = int(row["priority"])
        except ValueError as exc:
            raise ValueError(f"line {line}: priority must be integer") from exc
        deps = tuple(item.strip() for item in row.get("depends_on", "").split(";") if item.strip())
        tasks.append(Task(row["task_id"].strip(), priority, deps, row["status"].strip(), row))
    return tasks, rows


def validate(tasks: list[Task]) -> list[str]:
    errors: list[str] = []
    ids = [t.task_id for t in tasks]
    counts = Counter(ids)
    for task_id, count in counts.items():
        if not task_id:
            errors.append("missing task_id")
        if count > 1:
            errors.append(f"duplicate task_id: {task_id}")
    known = set(ids)
    for task in tasks:
        if task.status not in STATUSES:
            errors.append(f"{task.task_id}: invalid status {task.status}")
        for field in ["title", "deliverables", "acceptance", "human_review"]:
            if not task.row.get(field, "").strip():
                errors.append(f"{task.task_id}: missing {field}")
        try:
            date.fromisoformat(task.row["last_updated"])
        except ValueError:
            errors.append(f"{task.task_id}: last_updated must be YYYY-MM-DD")
        for dep in task.depends_on:
            if dep not in known:
                errors.append(f"{task.task_id}: unknown dependency {dep}")
            if dep == task.task_id:
                errors.append(f"{task.task_id}: self dependency")
    return sorted(set(errors))


def ready_tasks(tasks: list[Task]) -> list[Task]:
    statuses = {t.task_id: t.status for t in tasks}
    return sorted(
        [t for t in tasks if t.status == "not-started" and all(statuses.get(dep) in READY for dep in t.depends_on)],
        key=lambda t: (t.priority, t.task_id),
    )


def next_task(tasks: list[Task]) -> Task | None:
    active = sorted([t for t in tasks if t.status == "in-progress"], key=lambda t: (t.priority, t.task_id))
    if active:
        return active[0]
    ready = ready_tasks(tasks)
    return ready[0] if ready else None


def render(task: Task) -> str:
    deps = ", ".join(task.depends_on) if task.depends_on else "none"
    row = task.row
    return "\n".join([
        f"# Next Codex task: {row['task_id']}", "",
        f"- Title: {row['title']}",
        f"- Sprint: {row['sprint']}",
        f"- Module: {row['module']}",
        f"- Status: {row['status']}",
        f"- Dependencies: {deps}",
        f"- Deliverables: {row['deliverables']}",
        f"- Acceptance: {row['acceptance']}",
        f"- Human review: {row['human_review']}",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["validate", "next", "summary"])
    args = parser.parse_args()
    try:
        tasks, _ = load()
        errors = validate(tasks)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        if args.command == "validate":
            print(f"Codex task queue valid: {len(tasks)} tasks.")
            return 0
        if args.command == "summary":
            print(json.dumps({"total": len(tasks), "counts": Counter(t.status for t in tasks)}, ensure_ascii=False, indent=2, default=dict))
            return 0
        task = next_task(tasks)
        if not task:
            print("No unblocked task is currently ready.", file=sys.stderr)
            return 2
        print(render(task))
        return 0
    except Exception as exc:
        print(f"codex_orchestrator failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
