# 任务包：workflow-bootstrap Phase 4 Round 2 Git-first Evidence Gap

## 任务标识

- task id: `WF-BOOTSTRAP-PHASE4-ROUND2-GIT-FIRST-EVIDENCE-V1`
- 名称：workflow-bootstrap Phase 4 Round 2 / Git-first Evidence Gap
- 阶段：`Phase 4 Round 2`
- 提交方：Drafter
- 日期：`2026-04-30`
- 前置输入：
  - `tasks/workflow-bootstrap_phase4_multi_project_pilot_task_package.md`
  - `docs/reviews/workflow-bootstrap_phase4_multi_project_pilot_review.md`
  - `tasks/workflow-bootstrap_phase4_multi_project_pilot_execution_report.md`
  - `docs/HANDOFF.md`
  - `docs/status/skill-hub-status.md`
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/non_git_runtime_profile.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`
  - `skills/workflow-bootstrap/review_tiers.md`
  - `skills/workflow-bootstrap/runtime_pack_minimal_manifest.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `tasks/workflow-bootstrap_phase1_role_split_canonicalization_task_package.md`
  - `tasks/workflow-bootstrap_phase2_review_tier_guidance_task_package.md`
  - `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_task_package.md`

---

## Title

workflow-bootstrap Phase 4 Round 2: Git-first Evidence Gap Task Package

---

## Scope Restatement

本轮只为 `workflow-bootstrap` 的 Phase 4 Round 2 起草一份 task package。

当前轮次是 `task package drafting`，不是 Round 2 execution。

本轮不补 Git evidence，不修改外部项目，不更新 `docs/HANDOFF.md` 或 `docs/status/skill-hub-status.md`，不生成 execution report，也不修改 canonical guidance。

本 task package 的作用，是为后续一轮更窄的 Codex bounded execution 提供清晰边界，用于补充 Phase 4 Round 1 遗留的 Git-first evidence gap，而不是在当前轮次直接开展外部项目检查、修复 Git 环境或推进下一阶段工作。

---

## Round 1 Context

Phase 4 Round 1 已完成 read-only multi-project pilot review，并已产出：

- `tasks/workflow-bootstrap_phase4_multi_project_pilot_task_package.md`
- `docs/reviews/workflow-bootstrap_phase4_multi_project_pilot_review.md`
- `tasks/workflow-bootstrap_phase4_multi_project_pilot_execution_report.md`

Round 1 的 Git-first candidate 是：

- `D:\dev\financial_data_center_lt`

Round 1 发现该 candidate 的本地 Git commands 被 dubious ownership 阻断，因此本轮只能把这部分记录为 `evidence gap`，而不能声称已经完成完整的 Git-first validation。

Round 2 不重做整个 multi-project pilot，只聚焦这一处 Git-first evidence gap，并继续把该问题视为 evidence limitation / environment limitation，而不是通过修改外部环境来消除它。

---

## Objective

Round 2 的目标是：在不修改外部 repo、不修改 Git config、不修复 dubious ownership 的前提下，尽可能补充 Git-first project evidence。

后续执行应优先验证以下问题：

- `branch / commit / PR-style review evidence` 是否能够由已有文档、GitHub PR、local docs、execution reports 或用户提供的文本证据支撑；
- `task package + execution report pairing` 是否能与 Git history / PR review 协同，而不是互相替代；
- `docs/HANDOFF.md` 与 status surfaces 是否继续保持 `minimal closure`，而不是变成 per-task trace log；
- project-local facts 是否仍被限制在项目局部，没有被提升为 canonical guidance。

本轮目标是补证据，不是修环境，不是推动规则扩张，也不是把单一 Git-first 项目的做法升级为跨项目 canonical guidance。

---

## Authorized Future Execution Files

若后续进入 Round 2 execution，未来执行阶段只允许写入以下文件：

- `docs/reviews/workflow-bootstrap_phase4_round2_git_first_evidence_review.md`
- `tasks/workflow-bootstrap_phase4_round2_git_first_evidence_execution_report.md`

必要时，只有在 `Final Reviewer` 阶段才可考虑 minimal `HANDOFF/status` closure，但本 Round 2 execution 不直接授权修改以下文件：

- `docs/HANDOFF.md`
- `docs/status/skill-hub-status.md`

当前 Drafter 轮次的唯一可写文件是：

- `tasks/workflow-bootstrap_phase4_round2_git_first_evidence_task_package.md`

除上述范围外，本轮及后续 Round 2 execution 默认无权修改其他文件或目录。

---

## Candidate Evidence Sources

未来 Implementer 可以优先查看以下 evidence sources，但必须保持只读：

- `ai-skill-hub` 内已经存在的 Phase 4 Round 1 review memo 与 execution report
- `D:\dev\financial_data_center_lt` 中可读的文档证据，例如：
  - `docs/HANDOFF.md`
  - `docs/tasks/*.md`
  - `docs/reports/*.md`
  - `README.md`
- 若本地 Git metadata 仍被 blocked，则应明确记录为 `environment limitation`
- 如用户提供 GitHub PR 链接、PR 文本、commit 摘要或其他文本证据，可纳入 review memo

注意事项：

- 不要假设外部项目路径一定存在。
- 不要修改外部项目。
- 不要运行会改变 Git config 的命令。
- 不要为了读取 evidence 而修复权限、ownership 或其他外部环境问题。

---

## Future Implementer Instructions

未来 Implementer 应遵守以下执行约束：

- 先确认 `ai-skill-hub` 工作区干净。
- 只读检查 Git-first candidate evidence。
- 如果 Git commands 仍然 blocked by dubious ownership，再次记录为 `evidence gap / environment limitation`。
- 不执行 `git config --global --add safe.directory ...`。
- 不修改 `financial_data_center_lt`。
- 不修改任何外部项目。
- 不补写外部项目的 task package 或 execution report。
- 只在 `ai-skill-hub` 中写 review memo 与 execution report。
- 明确区分以下证据与结论层级：
  - `Git-first evidence`
  - `local documentation evidence`
  - `Git metadata evidence gap`
  - `project-local facts`
  - `generalized guidance candidates`

若证据不足，应如实收窄结论，不得用推断填补 Git-first evidence gap。

---

## Review Memo Requirements

未来应创建：

- `docs/reviews/workflow-bootstrap_phase4_round2_git_first_evidence_review.md`

该 review memo 必须包含以下 section：

1. `Title`
2. `Scope Restatement`
3. `Round 1 Gap Context`
4. `Candidate Evidence Sources`
5. `Git-first Evidence Review`
6. `Task Package / Execution Report Pairing Review`
7. `PR-style / Branch / Commit Evidence Review`
8. `HANDOFF/status Minimal Closure Review`
9. `Evidence Gaps`
10. `What Can Be Generalized`
11. `What Must Remain Project-local`
12. `Recommendation`
13. `Out of Scope Confirmation`

该 review memo 的重点是记录证据质量、边界保持情况与 generalized guidance 的上限，不是为外部项目补写新的运行规则。

---

## Execution Report Requirements

未来应创建：

- `tasks/workflow-bootstrap_phase4_round2_git_first_evidence_execution_report.md`

该 execution report 必须包含以下 section：

1. `Scope Restatement`
2. `Files Changed`
3. `Validation Performed`
4. `Candidate Reviewed`
5. `Evidence Sources Reviewed`
6. `Key Findings`
7. `Evidence Gaps`
8. `Boundaries Preserved`
9. `Recommended Next Step`
10. `Suggested Commit Message`

Suggested commit message:

```text
docs(workflow-bootstrap): add phase 4 round 2 git-first evidence review
```

---

## Out of Scope

以下内容全部属于当前 task package drafting 以及后续 Round 2 execution 的 out of scope：

- 修复 dubious ownership
- 执行 `git config --global --add safe.directory ...`
- 修改 `financial_data_center_lt`
- 修改任何外部项目
- 创建或修改外部项目 task package / execution report
- 修改 canonical guidance
- 修改 `skills/**`
- 修改 `docs/HANDOFF.md`
- 修改 `docs/status/skill-hub-status.md`
- 创建 validators
- 创建 CI
- 创建 automation
- 创建 tool adapters
- 创建 `.github/instructions`
- 创建 `.github/agents`
- 进入 Phase 4 Round 2 execution
- 进入 Phase 5
- 把单一 Git-first 项目 practice 推广为 canonical guidance

---

## Acceptance Criteria

本 task package 只有在满足以下条件时才可接受：

1. 明确 Round 2 只聚焦 Git-first evidence gap。
2. 明确当前只是 `task package drafting`。
3. 明确不修复 dubious ownership。
4. 明确不修改外部项目。
5. 明确 future execution 只写 review memo 与 execution report。
6. 明确 `HANDOFF/status` closure 留给 `Final Reviewer` 阶段。
7. 保持 `workflow-bootstrap` / `chatgpt-handoff-pilot` ownership boundary。
8. 不引入 validator / CI / automation 的授权、实现或 rollout 语言。
9. 不把 `tasks/` 写成 mandatory global path。
10. 不把 project-local facts 回灌为 canonical guidance。

---

## Validation

由于当前是 documentation-only task package drafting，修改后只做：

```powershell
git -C "D:\dev\ai-skill-hub" status --short --untracked-files=all
git -C "D:\dev\ai-skill-hub" diff --name-only
```

如果目标文件是 untracked file，`git diff --name-only` 可能为空。应结合 `git status --short --untracked-files=all` 一起判断。

预期只出现：

- `tasks/workflow-bootstrap_phase4_round2_git_first_evidence_task_package.md`

---

## Suggested Commit Message after review/approval

```text
docs(workflow-bootstrap): add phase 4 round 2 git-first evidence task package
```