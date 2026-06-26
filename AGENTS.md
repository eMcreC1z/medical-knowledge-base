# AGENTS.md — Medical Research Mastery

## Mission

Build and maintain a rigorous, reproducible, ethics-first medical research mastery system. The learner should eventually be able to design, execute, audit, interpret, report, and transfer methods across clinical research, statistics, trials, diagnostics, prediction/AI, basic/translational research, bioinformatics/omics, systematic review/Meta, qualitative methods, implementation science, and health economics.

This is a learning and research-methods knowledge base, not a clinical decision support system.

## Non-negotiable rules

- Never commit patient-identifiable or re-identifiable data, protected health information, credentials, private keys, controlled-access datasets, confidential manuscripts, peer-review materials, or data prohibited by a data-use agreement.
- Never upload paid books, paid course archives, copyrighted PDFs, licensed datasets, or copied proprietary teaching materials.
- Never invent citations, DOIs, PMIDs, sample sizes, effect estimates, software behavior, guideline versions, or analysis results.
- Do not claim causality from observational association without a defensible design and identification strategy.
- Do not treat AI-generated text, code, figures, references, or statistical output as verified evidence.
- Do not certify human competency at L3–L5. Codex may prepare evidence and mark tasks `evidence-ready`; independent human review is required for certification.

## Required workflow

1. Read `research-mastery/CODEX-CONTINUOUS-MISSION.md`.
2. Run `python scripts/codex_orchestrator.py validate`.
3. Run `python scripts/codex_orchestrator.py next`.
4. Execute the selected highest-priority unblocked task.
5. Use only public, synthetic, or explicitly authorized inputs.
6. Create substantive artifacts rather than placeholders.
7. Update the task queue, ledgers, and `STATUS.md`.
8. Run all validation commands.
9. Commit a focused checkpoint and continue the next independent task while runtime remains.

## Validation commands

```bash
python -m compileall scripts
python scripts/codex_orchestrator.py validate
python scripts/build_research_mastery_status.py
python scripts/validate_research_mastery.py
python scripts/build_research_mastery_status.py --check
```

## Human review triggers

Stop the affected task and mark it `blocked` when it requires human ethics approval, data authorization, human genetic resource review, trial safety, real-study sample-size decisions, new causal identification strategy, clinical deployment, authorship decisions, conflict-of-interest judgment, or patient-care/regulatory claims. Continue another independent task when possible.
