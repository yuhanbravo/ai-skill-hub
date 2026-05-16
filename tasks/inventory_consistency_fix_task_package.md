# Task Package: Stage 1 Inventory Consistency Fix

## 1. Background
上一轮 external skill benchmark audit 指出 root docs 的 skill inventory 与 `SKILLS_INDEX.md` 存在轻微漂移风险，重点是 `workflow-bootstrap` 已存在于 `skills/` 与 `SKILLS_INDEX.md`，但 README 的技能清单可能遗漏。

## 2. Goal
在不做大规模文档治理的前提下，完成一次小范围 inventory consistency 修复：
- 核对 `skills/`、`SKILLS_INDEX.md`、`README.md`、`AI_USAGE.md` 的 skill inventory 导航一致性；
- 对最明显 mismatch 做最小修改；
- 优先处理 `workflow-bootstrap` 在 README 中的遗漏（若存在）。

## 3. In Scope
- 仅执行 inventory/index consistency 检查与轻量修复。
- 比对 canonical skills（以 `skills/*/SKILL.md` 为准）与 root index/docs 的可发现性。
- 必要时最小修改 `README.md` 与/或 `SKILLS_INDEX.md`。
- 生成本轮 execution report。

## 4. Out of Scope
- 不做 root docs 大清理。
- 不做 current-state SSOT 重构。
- 不修改 `skills/`。
- 不修改 `docs/HANDOFF.md`、`docs/status/`。
- 不新增 skill / adapter / automation / validator / CI。
- 不刷新 handoff/status 内容。

## 5. Target files/areas
Authorized files only:
- `README.md`
- `SKILLS_INDEX.md`
- `AI_USAGE.md`（仅当入口一致性确有问题）
- `tasks/inventory_consistency_fix_execution_report.md`
- `tasks/inventory_consistency_fix_task_package.md`

## 6. Acceptance checks
- `skills/` 中 canonical skills 与 `SKILLS_INDEX.md` 记录无明显遗漏。
- README 的 skill list 与 `SKILLS_INDEX.md` 在名称层面对齐到最小可接受一致性。
- `workflow-bootstrap` mismatch 已修复，或明确说明 not applicable。
- README 仍保持 entry/onboarding 定位，不承载大量 mutable status facts。
- Restricted paths 未被修改。

## 7. Constraints
- `skills/` 是 canonical skill source。
- `SKILLS_INDEX.md` 是 active index/router，不是 current-state SSOT。
- `README.md` 是 entry/onboarding，不应复制大量易变状态事实。
- `docs/HANDOFF.md` 与 `docs/status/` 是 current-state surfaces，本轮不更新。
- 仅做最小必要变更，不做风格性重写。

## 8. Output requirements
- 产出最小修复 diff（若发现 mismatch）。
- 产出 `tasks/inventory_consistency_fix_execution_report.md`，至少包含：
  1. Scope Restatement
  2. Files Changed
  3. What Changed
  4. What Did Not Change
  5. Validation Performed
  6. Boundary Checks
  7. Risks and Assumptions
  8. Deferred Items
  9. Recommended Commit Message

## 9. Assumptions
- `skills/*/SKILL.md` 列表代表当前 canonical skills 全量集合。
- `SKILLS_INDEX.md` 若已覆盖 canonical skills，则优先保持不改。
- `AI_USAGE.md` 若仍为 compatibility/router 角色且未误导 inventory，则不改。
- 本轮以“最小一致性修复”优先于“文案优化”。

## Validation commands
- `git diff -- README.md SKILLS_INDEX.md AI_USAGE.md tasks/inventory_consistency_fix_task_package.md tasks/inventory_consistency_fix_execution_report.md`
- `git diff --name-only`
- `git status --short`
- `rg "workflow-bootstrap" README.md SKILLS_INDEX.md AI_USAGE.md`
- `rg "current-state SSOT|docs/HANDOFF.md|docs/status|canonical skill source|inventory" README.md SKILLS_INDEX.md tasks/inventory_consistency_fix_execution_report.md`
