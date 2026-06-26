#!/usr/bin/env python3
"""Generate research-mastery/STATUS.md from the Codex queue."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "research-mastery" / "data" / "codex-task-queue.csv"
OUT = ROOT / "research-mastery" / "STATUS.md"
LABEL = {"not-started": "未开始", "in-progress": "进行中", "evidence-ready": "证据待审", "completed": "已完成", "blocked": "受阻"}


def load() -> list[dict[str, str]]:
    with QUEUE.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def is_ready(row: dict[str, str], statuses: dict[str, str]) -> bool:
    deps = [item.strip() for item in row.get("depends_on", "").split(";") if item.strip()]
    return row["status"] == "not-started" and all(statuses.get(dep) in {"evidence-ready", "completed"} for dep in deps)


def generate() -> str:
    rows = load()
    counts = Counter(row["status"] for row in rows)
    statuses = {row["task_id"]: row["status"] for row in rows}
    active = [row for row in rows if row["status"] == "in-progress"]
    ready = sorted([row for row in rows if is_ready(row, statuses)], key=lambda r: (int(r["priority"]), r["task_id"]))
    current = active or ready[:3]
    lines = [
        "# 医学研究精通计划状态", "",
        "> 自动生成；请运行 `python scripts/build_research_mastery_status.py` 更新。", "",
        "## Codex持续执行队列", "",
        "| 状态 | 数量 |", "|---|---:|",
    ]
    for status in ["not-started", "in-progress", "evidence-ready", "completed", "blocked"]:
        if counts.get(status):
            lines.append(f"| {LABEL[status]} | {counts[status]} |")
    lines += ["", "## 当前或下一任务", "", "| Task | Sprint | 主题 | 状态 | 人工审查 |", "|---|---|---|---|---|"]
    for row in current:
        lines.append(f"| {row['task_id']} | {row['sprint']} | {row['title']} | {LABEL.get(row['status'], row['status'])} | {row['human_review']} |")
    lines += ["", "## 运行命令", "", "```bash", "python -m compileall scripts", "python scripts/codex_orchestrator.py validate", "python scripts/build_research_mastery_status.py", "python scripts/validate_research_mastery.py", "python scripts/build_research_mastery_status.py --check", "```", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = generate()
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != content:
            print("STATUS.md is stale; rebuild it.")
            return 1
        print("STATUS.md is up to date.")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(content, encoding="utf-8")
    print("Wrote research-mastery/STATUS.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
