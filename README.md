# Medical Knowledge Base

目标：建立一套可由学习者、导师与 Codex 持续执行、审查和迭代的医学研究深研系统。

本仓库的正式目的不是收集课程链接，而是通过长期、系统、项目驱动、可复现的训练，使学习者能够精通主要医学研究类型，并在陌生疾病、陌生数据和陌生研究场景中举一反三。

## 当前起点

从 `research-mastery/` 开始。

核心路径：

1. `AGENTS.md`：Codex 和贡献者必须遵守的仓库规则。
2. `research-mastery/CODEX-CONTINUOUS-MISSION.md`：Codex 持续执行总任务。
3. `research-mastery/data/codex-task-queue.csv`：32 项系统构建任务队列。
4. `scripts/codex_orchestrator.py`：选择下一项任务并校验队列。
5. `.github/workflows/codex-continuous-medical-research.yml`：定时调用 Codex 的持续构建工作流。

## 第一阶段

先完成 S00：

- 证据化基线能力评估；
- 第一个公开或合成数据复现项目；
- 第三方复现协议；
- 后续再进入 26 个 Sprint 的完整医学研究训练。

## 不做的事

- 不上传患者数据、受控数据库、密钥、未发表稿件或审稿材料。
- 不上传付费课程、盗版教材或受版权保护全文。
- 不把 AI 生成内容、课程数量、文件数量或模型运行等同于学生能力达标。
- 不由 Codex 自行认证学习者 L3–L5 能力。
