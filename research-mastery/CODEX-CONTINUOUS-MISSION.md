# Codex Continuous Mission — Medical Research Mastery

## Mission

Continuously build, verify, integrate, and improve the complete medical-research mastery system until every planned artifact has been produced, validated, cross-linked, and audited.

“Deep learning” here means deep study and sustained practice, not changing Codex model weights.

## Start sequence for every run

1. Read `AGENTS.md`.
2. Read this file.
3. Read `research-mastery/data/codex-task-queue.csv`.
4. Run `python scripts/codex_orchestrator.py validate`.
5. Run `python scripts/codex_orchestrator.py next`.
6. Execute the selected task completely.

## Execution loop

For each task:

1. Restate measurable deliverables.
2. Check privacy, ethics, data authorization, copyright, and human-review triggers.
3. Mark only that task `in-progress`.
4. Produce real artifacts: theory, concept maps, reproducible public/synthetic examples, flawed cases with corrections, transfer exercises, assessments, rubrics, and source verification.
5. Update affected ledgers and `STATUS.md`.
6. Run all validation commands.
7. Mark the task `evidence-ready` only when machine-verifiable acceptance criteria pass.
8. If blocked by a human-only decision, record the exact blocker and continue another independent task.
9. Commit a checkpoint.
10. If runtime remains, immediately continue to the next unblocked task.

## Completion criteria

System construction is complete only when:

- all queued tasks are `evidence-ready` or `completed`;
- all 26 sprints have executable learning packages;
- all 78 competencies map to exercises, artifacts, and assessment;
- each research type has public or synthetic examples and deliberately flawed cases;
- automated validation passes;
- a full red-team review and clean-environment rebuild pass.

This does not certify a learner. Human mastery requires independent review.
