# Continuous medical-research system build

Read `AGENTS.md`, `research-mastery/CODEX-CONTINUOUS-MISSION.md`, and `research-mastery/data/codex-task-queue.csv` first.

Run:

```bash
python scripts/codex_orchestrator.py validate
python scripts/codex_orchestrator.py next
```

Execute the selected highest-priority unblocked task completely. Use only public or synthetic data unless explicit authorization exists. Produce substantive theory, reproducible examples, flawed cases with corrections, transfer exercises, assessment rubrics, practical artifacts, and source verification. Do not create placeholders. Do not certify human competency.

When blocked by ethics, data authorization, trial safety, real-study sample size, causal identification, clinical deployment, authorship, controlled data, or confidential material, mark only that task blocked and continue another independent task.

Before finishing:

```bash
python -m compileall scripts
python scripts/codex_orchestrator.py validate
python scripts/build_research_mastery_status.py
python scripts/validate_research_mastery.py
python scripts/build_research_mastery_status.py --check
```

Update the task queue, ledgers, and `STATUS.md`. Commit a valid checkpoint and continue the next independent unblocked task while runtime remains.
