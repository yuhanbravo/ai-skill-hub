# 任务包：workflow-bootstrap Phase 4 Multi-project Pilot

## 任务标识

- task id: `WF-BOOTSTRAP-PHASE4-MULTI-PROJECT-PILOT-V1`
- 名称：workflow-bootstrap Phase 4 / Multi-project Pilot
- 阶段：`Phase 4`
- 提交方：Drafter
- 日期：`2026-04-30`
- 前置输入：
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/non_git_runtime_profile.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`
  - `skills/workflow-bootstrap/review_tiers.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `docs/HANDOFF.md`
  - `docs/status/skill-hub-status.md`
  - `tasks/workflow-bootstrap_phase1_role_split_canonicalization_task_package.md`
  - `tasks/workflow-bootstrap_phase2_review_tier_guidance_task_package.md`
  - `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_task_package.md`

---

## Title

workflow-bootstrap Phase 4: Multi-project Pilot Task Package

---

## Scope Restatement

本任务只为 `workflow-bootstrap` Phase 4：`Multi-project Pilot` 起草一份 task package。

当前轮次是 Drafter 阶段，不是 pilot execution。

本轮不修改 `workflow-bootstrap` canonical guidance，不更新 `docs/HANDOFF.md` 或 `docs/status/skill-hub-status.md`，也不生成 execution report。

本 task package 的作用，是为未来一轮经过 review 的 `bounded execution` 提供清晰边界，使后续 Implementer 能在多个项目类型中验证既有 guidance 的可迁移性，而不是在当前轮次直接开展 pilot 或扩写规则。

---

## Baseline Context

`workflow-bootstrap` 的 Phase 0-3 baseline 已完成，并已形成以下稳定基础：

- Phase 0：`non-git / low-git runtime profile`
- Phase 1：`role split canonicalization`
- Phase 2：`review tier guidance`
- Phase 3：`runtime pack minimal manifest`

当前 baseline 已明确：

- `workflow-bootstrap` 负责 `workflow shell`、`role protocol`、`runtime profile`、`review tiers` 与 `runtime pack` guidance。
- `chatgpt-handoff-pilot` 继续负责 `task package`、`bounded execution` 与 `execution report` protocol。
- project-side runtime surfaces 只能保持为 thin entries、adapters 或 evidence indexes，不能演化为第二规则库。

Phase 4 的目标不是新增规则层，而是验证这些既有 guidance 是否能够跨项目类型成立，并据此沉淀未来可能回灌到 canonical assets 的 `generalized guidance`。

---

## Objective

Phase 4 的目标，是在多个项目类型中验证以下四类 guidance 的适用性与边界是否仍然成立：

- `role protocol`
- `runtime profile`
- `review tiers`
- `runtime pack guidance`

验证重点是 portability 与 boundary clarity，而不是把单次 pilot 结果直接升级为新规则、强制模板或 rollout 结论。

本阶段应持续保持以下 ownership boundary：

- `workflow-bootstrap` 继续定义 workflow-shell guidance。
- `chatgpt-handoff-pilot` 继续拥有 `task package`、`bounded execution`、`execution report` protocol。
- pilot learning 只能先作为 evidence 与 review input，后续若要吸收，也只能抽象为 `generalized guidance`，不能把 `project-local facts` 直接回灌进 canonical guidance。

---

## Pilot Coverage Requirements

未来 Phase 4 pilot 至少必须覆盖以下两类项目：

1. 一个 `Git-first project`
2. 一个 `non-git / low-git project`

可选覆盖项：

- 一个 `data analysis script project`
- `ai-skill-hub` 自身，作为 `canonical-skill-modification review case`

覆盖这些项目类型的目的，是比较不同证据路径、不同 review 习惯和不同 runtime surface 约束下，Phase 0-3 guidance 是否仍能保持轻量、清晰且不越权。

---

## Pilot Matrix

| Project type | Validation focus | Expected evidence | Review tier expectation | What must not be generalized |
| --- | --- | --- | --- | --- |
| non-git / low-git project | `tasks/ evidence path`、inactive archive、minimal handoff/status closure | `task package + execution report` pairing，必要时配合最小 handoff/status closure | `Standard Review`，若 wording 触及跨项目规则则升级 `Heavy Review` | 不得把 `tasks/` 写成所有项目 mandatory global path；不得把 archive/handoff/status 变成 per-task trace log |
| Git-first project | branch / commit / PR-style review、`task package / execution report pairing` | Git evidence、review comments、必要时保留 task artifacts pairing | `Standard Review`，若触及 canonical wording 或跨项目抽象则升级 `Heavy Review` | 不得把 Git-first review 流程写成所有项目统一模式；不得把 PR-style review 误写成 protocol owner |
| data analysis script project | `runtime pack` 是否仍然 lightweight | 小范围 task artifacts、轻量 review memo、必要的最小 evidence pairing | 通常 `Light Review` 或 `Standard Review`，如涉及跨项目 wording 则升级 | 不得因为脚本项目较轻就把 runtime pack 扩写成额外 rule set、tooling 或 automation |
| ai-skill-hub itself | canonical skill 修改是否应进入 `Heavy Review` | task package、execution report、pilot review memo、必要的 boundary review evidence | `Heavy Review` | 不得把 hub 内部路径、业务事实、环境命令或单仓经验回灌为通用 canonical guidance |

---

## Future Implementer Instructions

未来 Implementer 在执行 Phase 4 pilot 时，应遵守以下约束：

- 每类项目只选择一个 `small bounded pilot task`。
- 适用时保留 `task package + execution report pairing`，确保 evidence 可回溯。
- 每轮 pilot 结束后写一份 concise `pilot review memo`，只总结对 guidance 是否成立的观察。
- 必须明确区分 `generalized guidance` 与 `project-local facts`。
- 不得把项目路径、业务事实、环境命令回灌进 canonical guidance。
- 不强制所有项目使用 `tasks/`。
- 不强制所有项目采用同一 adapter 文件。
- 不因为 pilot 成功就提前引入 `validator`、`CI`、`automation`。
- 保持 `review tiers` 为 advisory guidance，而不是 enforcement。
- 若 pilot 涉及 canonical skill wording 或跨项目规则抽象，应按 `Heavy Review` 处理。

---

## Authorized Files for Future Execution

以下文件仅是未来 Phase 4 execution candidate，不是当前 Drafter task 的可写文件：

- `docs/reviews/workflow-bootstrap_phase4_multi_project_pilot_review.md`
- `tasks/<project-local-pilot-task-package>.md`
- `tasks/<project-local-pilot-execution-report>.md`
- `docs/HANDOFF.md`，仅用于 pilot 完成后的 minimal closure
- `docs/status/skill-hub-status.md`，仅用于 pilot 完成后的 minimal closure

必须明确：上述文件都不是当前任务授权修改的文件。它们只描述未来经过 review 的 Phase 4 execution 可能落盘的位置，不构成当前 Drafter 阶段的写入授权。

---

## Current Drafter Authorized File

当前 Copilot task 的唯一可写文件是：

- `tasks/workflow-bootstrap_phase4_multi_project_pilot_task_package.md`

除该文件外，当前任务不得修改任何其他文件。

---

## Out of Scope

以下内容全部属于当前 task package generation 的 out of scope：

- `pilot execution`
- `canonical skill changes`
- `tool adapters`
- `validators`
- `CI`
- `automation`
- `.github/instructions`
- `.github/agents`
- rewriting `HANDOFF/status`
- pushing tags or commits
- enforcing `tasks/` globally
- turning `runtime pack` into a second rule set

补充说明：当前轮次也不做 rollout、distribution、adoption、global policy promotion，且不授权任何超出 task-package drafting 的 repository changes。

---

## Acceptance Criteria

本 task package 只有在满足以下条件时才可接受：

- 覆盖至少 `Git-first` 与 `non-git / low-git` 两类 pilot。
- 保持 Phase 4 为 validation，而不是 rule promotion。
- 保持 `workflow-bootstrap` 与 `chatgpt-handoff-pilot` 的 ownership boundary。
- 将 `review tiers` 作为 advisory guidance，而不是 enforcement。
- 不引入 `validator` / `CI` / `automation` 的授权、实现或 rollout 语言。
- 清楚区分 `generalized guidance` 与 `project-local facts`。
- 只写入指定 task package 文件。

---

## Validation

由于本轮是 documentation-only task，只做轻量 validation：

- 确认目标文件已创建。
- 结合 `git status --short --untracked-files=all` 与 `git diff --name-only` 确认仅目标 task package 有变更；其中 untracked file 通过 `git status` 判断，tracked file modifications 通过 `git diff --name-only` 判断。
- 确认没有修改 canonical skill 文件。
- 确认没有修改 `docs/HANDOFF.md` 或 `docs/status/skill-hub-status.md`。

---

## 审阅通过并获准提交后的 Suggested Commit Message

```text
docs(workflow-bootstrap): add phase 4 multi-project pilot task package
```
