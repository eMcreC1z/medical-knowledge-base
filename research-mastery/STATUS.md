# 医学研究精通计划状态

> 自动生成；请运行 `python scripts/build_research_mastery_status.py` 更新。

## Codex持续执行队列

| 状态 | 数量 |
|---|---:|
| 未开始 | 31 |
| 证据待审 | 1 |

## 当前或下一任务

| Task | Sprint | 主题 | 状态 | 人工审查 |
|---|---|---|---|---|
| SYS-002 | S00 | Evidence-based learner baseline instrument | 未开始 | required-for-final-levels |
| SYS-003 | S00 | First public reproducibility project | 未开始 | required-if-source-or-license-unclear |

## 运行命令

```bash
python -m compileall scripts
python scripts/codex_orchestrator.py validate
python scripts/build_research_mastery_status.py
python scripts/validate_research_mastery.py
python scripts/build_research_mastery_status.py --check
```
