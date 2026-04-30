# workflow-bootstrap Phase 4 Multi-project Pilot Review

## Scope Restatement

本轮执行 `workflow-bootstrap` Phase 4 的第一轮最小 `bounded execution`，目标是用 read-only pilot validation 检查 Phase 0-3 guidance 是否能跨项目类型保持可迁移、轻量且边界清楚。

本轮不修改 canonical guidance，不修改任何 `skills/**`，不更新 `docs/HANDOFF.md` 或 `docs/status/skill-hub-status.md`，不创建 validator / CI / automation / tool adapters，也不把任何 project-local facts 回灌为 canonical guidance。

## Baseline Context

Phase 0-3 baseline 已明确：

- `workflow-bootstrap` 负责 `workflow shell`、`role protocol`、`runtime profile`、`review tiers` 与 `runtime pack guidance`。
- `chatgpt-handoff-pilot` 继续拥有 `task package`、`bounded execution` 与 `execution report` protocol。
- `review tiers` 是 advisory guidance，不是 enforcement。
- project-side runtime surfaces 应保持为 thin entries、adapters 或 evidence indexes，不应成为第二规则库。
- `tasks/` 可在 non-git / low-git 场景作为 preferred project-local evidence path，但不是 mandatory global path。

## Pilot Candidate Matrix

| Project type | Candidate project | Evidence found | Pilot status | Review tier expectation | Notes |
| --- | --- | --- | --- | --- | --- |
| Git-first project | `D:\dev\financial_data_center_lt` | `.git` directory, `docs/HANDOFF.md`, `docs/tasks/*.md`, `docs/reports/*.md`, README handoff link | Partially executed / Git metadata evidence gap | `Standard Review`; `Heavy Review` if generalized wording is proposed | Git commands were blocked by dubious ownership; no safe.directory mutation was performed. |
| non-git / low-git project | `D:\dev\AMS_Data` | `ai/tasks/*.md`, `docs/HANDOFF.md`, `docs/perf/**/execution_report*.md`, project docs | Executed as low-git evidence-path review | `Standard Review`; `Heavy Review` for cross-project abstraction | Git commands were also blocked by dubious ownership, so local task/report evidence carried the review. |
| data analysis script project | `D:\dev\financial_data_center_lt` / `D:\dev\AMS_Data` | Python scripts, reports, task artifacts | Covered only as optional observation | `Light Review` to `Standard Review` unless cross-project wording is proposed | Evidence supports script/report workflows, but no separate pilot task was executed. |
| ai-skill-hub self case | `D:\dev\ai-skill-hub` | `AGENTS.md`, `.github/copilot-instructions.md`, Phase 1-4 task packages and reports | Optional read-only review only | `Heavy Review` for canonical skill modification | No canonical skill modification was made or recommended. |

## Git-first Project Review

`financial_data_center_lt` is a plausible Git-first candidate because the repository contains a `.git` directory and normal project structure (`src`, `scripts`, `tests`, `docs`). Read-only inspection found:

- `docs/HANDOFF.md` provides minimal closure and current-stage context.
- `docs/tasks/phase1a_003_nav_analysis.md` is a bounded task package for a Portfolio NAV Analysis MVP.
- `docs/reports/sample_nav_analysis_report.example.md` is stable report evidence.
- README routes readers to `docs/HANDOFF.md`, blueprint docs, schema docs, and the current task package.

Evidence gap: `git rev-parse` and `git status` were blocked by Git dubious ownership because the repository is owned by a different Windows user. This pilot did not run `git config --global --add safe.directory` because that would mutate environment configuration outside the read-only validation intent.

Finding: Git-first projects can combine Git evidence with task artifacts, but this case shows a useful boundary: when Git metadata is inaccessible, the pilot should record the gap rather than silently treating local docs as equivalent Git evidence.

## Non-git / Low-git Project Review

`AMS_Data` is suitable for low-git evidence-path validation in this round because Git metadata was also inaccessible under the sandbox user, while project-local evidence is strong and active.

Read-only inspection found:

- `ai/tasks/phase1_candidate_index_review_task_package.md` and `ai/tasks/phase2d_stable_window_review_task_package.md` as bounded task inputs.
- `docs/HANDOFF.md` as the single project handoff surface with update log, current status, boundaries, environment blockers, and next-step guidance.
- Multiple execution reports under `docs/perf/phase1/` and `docs/perf/phase2/`.
- No need to create new project-side runtime surfaces for this review.

Finding: The non-git / low-git profile holds up when task packages and execution reports are project-local and inspectable. `docs/HANDOFF.md` works as minimal closure, but it is also large and should not become the per-task primary trace log. The active evidence path remains task/report artifacts.

## Optional Project Review

`ai-skill-hub` itself was checked only as a canonical-skill-modification review case. Existing `AGENTS.md` and `.github/copilot-instructions.md` are thin, reference-first surfaces that route back to canonical guidance and explicitly avoid becoming a second rulebook.

This supports the Phase 3 runtime pack guidance, but it must remain a hub-local fact. It does not prove every project needs the same entrypoint pair, nor does it authorize `.github/instructions`, `.github/agents`, validators, CI, automation, or tool adapters.

## Cross-project Findings

- The role chain `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` remains usable across the inspected candidates.
- `task package + execution report` pairing works well as evidence when Git evidence is unavailable, weak, or blocked.
- `review tiers` remain useful as advisory classification: routine project-local review fits `Standard Review`, while any canonical wording or cross-project abstraction should move to `Heavy Review`.
- Runtime-pack guidance should remain project-aware. `financial_data_center_lt`, `AMS_Data`, and `ai-skill-hub` expose different evidence paths and should not be forced into one file layout.

## What Can Be Generalized

- Phase 4 pilots should record whether Git evidence was available, unavailable, or intentionally not used.
- Low-git validation can rely on inspectable task/report artifacts when they are clearly paired and scoped.
- HANDOFF/status surfaces should keep minimal closure facts, while detailed per-task evidence should remain in task/report artifacts.
- Review tier selection should stay advisory and risk-based, with canonical or cross-project wording reviewed more heavily.

## What Must Remain Project-local

- Exact project paths such as `D:\dev\financial_data_center_lt` and `D:\dev\AMS_Data`.
- Business facts, database table names, portfolio/report details, environment names, interpreter paths, and validation commands from candidate projects.
- Local artifact layout choices such as `docs/tasks`, `ai/tasks`, `docs/perf`, or project-specific report directories.
- Git dubious-ownership behavior observed under this sandbox user.

## Risks / Gaps

- Git evidence for both external candidate repositories was blocked by dubious ownership, so this round cannot claim full Git-first validation.
- No cross-project file mutation was performed, so findings are evidence-review results rather than implementation proof.
- `Long_Short_Fund_Analysis` was not present at `D:\dev\Long_Short_Fund_Analysis`; it was not executed.
- The review did not inspect secrets, external systems, databases, or live runtime behavior.

## Recommendation

Keep Phase 4 as validation, not rule promotion. A future round may either ask a maintainer to provide safe Git evidence for a Git-first candidate or select another accessible Git-first repository. Do not introduce validators, CI, automation, tool adapters, `.github/instructions`, or `.github/agents` from this round.

## Out of Scope Confirmation

This round did not:

- modify `skills/**`;
- modify `docs/HANDOFF.md` or `docs/status/skill-hub-status.md`;
- execute any project pilot task outside read-only inspection;
- create validators, CI, automation, tool adapters, `.github/instructions`, or `.github/agents`;
- redefine `task package`, `bounded execution`, or `execution report` protocol;
- promote `tasks/` to a mandatory global path;
- turn runtime pack guidance into a second rule set;
- commit, tag, or push.
