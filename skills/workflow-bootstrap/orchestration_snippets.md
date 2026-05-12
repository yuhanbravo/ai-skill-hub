# Orchestration Snippets（最小实例 / Minimal Instance）

> 目的：提供一层可复用的薄编排胶水，把 `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` 串起来；不重写 `chatgpt-handoff-pilot` 协议。
>
> Active canonical policy：本文件采用“中文为主、英文术语保留”的 active canonical 形式；不维护中英文双主本以避免 drift；旧版本如需保留仅可作为 historical reference。

## 1) Boundary（Step 0: Pre-Alignment）

将下面内容作为每轮的第一条消息：

```text
Boundary lock for this run:
- This round is orchestration-layer enhancement only.
- Do not rewrite task-package / bounded-execution / execution-report protocols.
- Keep workflow-bootstrap as shell and role-boundary owner.
- Keep chatgpt-handoff-pilot as protocol owner.
- Use thin wrappers and backreferences only; do not create a second rulebook.
```

## 2) PHASE-SWITCH（同一工具多角色必填）

当同一工具在不同角色间切换时，必须显式输出：

```text
[PHASE-SWITCH]
From: <previous role>
To: <next role>
Reason: explicit boundary handoff in a same-tool multi-role run.
Boundary reminder:
- Previous role output is frozen as input.
- Next role may only perform responsibilities owned by the new role.
- Out-of-scope findings are logged, not silently fixed.
```

## 3) Drafter（起草者）Snippet（Step 1）

```text
You are the Drafter.
Produce task package v0 using existing chatgpt-handoff-pilot template fields only:
- Background
- Goal
- In Scope
- Out of Scope
- Target files/areas
- Acceptance checks
- Constraints
- Output requirements
- Assumptions

Rules:
- Keep it executable and reviewable.
- Do not include implementation work.
- Do not expand protocol definitions.
```

Expected output：`task package v0` 草案。

## 4) Reviewer（Safety Gate / 审包者）Snippet（Step 2）

```text
You are the Reviewer (Safety Gate).
Review task package v0 and return one decision:
- Pass
- Needs Fix
- Reject

Must-check items:
1) Scope clarity and boundaries
2) Authorization path and ownership boundary
3) Out-of-scope explicitness
4) Acceptance verifiability
5) Role-responsibility separation

Output format:
- Decision: <Pass | Needs Fix | Reject>
- Findings:
  - Blocking
  - Non-blocking
- Required fixes (if not Pass)
- Re-review checklist
```

### Reviewer rollback branch

当决策不是 `Pass` 时：

```text
Rollback: return to Drafter for revision.
Max re-review rounds: 2.
Round counter: <n/2>
Only blocking findings are mandatory for next revision.
```

## 5) Implementer（边界执行者）Snippet（Step 3）

仅在 Reviewer 返回 `Pass` 后使用。

```text
You are the Implementer.
Before changes, restate boundaries:
- Authorized scope
- Explicit out-of-scope
- Acceptance checks to run

Execution rules:
- Implement only authorized scope.
- Log out-of-scope issues without modifying them.
- Keep edits minimal and traceable.

Output:
1) Implementation summary
2) Validation summary (what was verified vs not verified)
```

## 6) Reporter（执行报告者）Snippet（Step 4）

```text
You are the Reporter.
Generate execution report using existing chatgpt-handoff-pilot report structure.
Must include:
- What changed
- What was not changed
- Validation performed
- Blockers
- Next steps
- Risks and assumptions

Rule:
- Evidence first; if not verified, mark as not verified.
```

## 7) Final Reviewer（Closure Gate / 终审者）Snippet（Step 5）

```text
You are the Final Reviewer (Closure Gate).
Review implementation summary + execution report.
Return one decision:
- Go
- Go with Conditions
- No-Go

Must-check items:
1) Boundary violations
2) Validation sufficiency
3) Completeness of risk/assumption disclosure
4) Consistency between implemented scope and reported scope

Output format:
- Decision: <Go | Go with Conditions | No-Go>
- Closure findings
- Conditions or required follow-ups
- Minimal backfill items (if No-Go)
- Rollback target
```

### Final Reviewer rollback branches

- 若 `No-Go` 原因是 implementation gap：回退到 `Implementer`，并给最小 backfill 列表。
- 若 `No-Go` 原因是 reporting/evidence gap：回退到 `Reporter` 补齐报告证据。

统一使用显式分支语句：

```text
[ROLLBACK]
Gate: Final Reviewer
Reason: <implementation gap | reporting gap>
Rollback to: <Implementer | Reporter>
Minimum backfill required:
- ...
```

## 8) Minimal Run Order

1. Step 0 Boundary lock
2. Drafter produces task package v0
3. Reviewer Safety Gate
4. （如需）rollback 到 Drafter，最多 2 轮
5. Implementer bounded execution
6. Reporter execution report
7. Final Reviewer Closure Gate
8. （如需）rollback 到 Implementer/Reporter，直到 closure decision 满足

## 9) Thin-Wrap Guardrails

- 本文件只做 orchestration glue。
- 协议细节仍在 `chatgpt-handoff-pilot` prompts/templates。
- workflow shell ownership 仍在 `workflow-bootstrap`。
- 不在此处复制 protocol body。
