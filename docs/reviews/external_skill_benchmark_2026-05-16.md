# Skill-Hub External Benchmark & Enhancement Audit

Status: Review evidence / planning reference  
Source: Codex read-only audit  
Boundary: Not active roadmap, not implementation authorization, not canonical skill definition.  
Follow-up requirement: Any recommendation must be converted into a bounded task package and reviewed before implementation.

## 1. Scope Restatement

This was executed as a strict read-only audit/planning task: no file edits, no file creation/deletion/rename, no formatting, no commit, no PR operations. The purpose was repository inspection and planning-reference output only.

## 2. Repository Read-Only Checks Performed

- `pwd && rg --files -g 'AGENTS.md'`
- `git -C /workspace/ai-skill-hub status --short`
- `git -C /workspace/ai-skill-hub log --oneline -n 20`
- `sed -n '1,220p' /workspace/ai-skill-hub/skills/workflow-bootstrap/SKILL.md`
- `sed -n '1,220p' /workspace/ai-skill-hub/skills/chatgpt-handoff-pilot/SKILL.md`
- `sed -n '1,260p' /workspace/ai-skill-hub/tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_task_package.md`
- `cd /workspace/ai-skill-hub && find skills -maxdepth 2 -name SKILL.md | sort`
- `cd /workspace/ai-skill-hub && find .agents/skills -maxdepth 2 -name SKILL.md | sort`
- `cd /workspace/ai-skill-hub && find .github/skills -maxdepth 2 -name SKILL.md | sort`
- `cd /workspace/ai-skill-hub && [ -f SKILLS_INDEX.md ] && echo YES || echo NO`
- `sed -n '1,260p' /workspace/ai-skill-hub/README.md`
- `sed -n '1,320p' /workspace/ai-skill-hub/SKILLS_INDEX.md`
- `sed -n '1,320p' /workspace/ai-skill-hub/skills/financial-data-project-migration/SKILL.md`
- `cd /workspace/ai-skill-hub && find .github -maxdepth 3 -type f | sort`
- `cd /workspace/ai-skill-hub && nl -ba README.md | sed -n '1,140p'`
- `cd /workspace/ai-skill-hub && nl -ba SKILLS_INDEX.md | sed -n '1,220p'`
- `cd /workspace/ai-skill-hub && nl -ba skills/financial-data-project-migration/SKILL.md | sed -n '1,240p'`
- `cd /workspace/ai-skill-hub && nl -ba skills/workflow-bootstrap/SKILL.md | sed -n '1,180p'`

## 3. Current Skill Inventory

| Skill | Exists in skills/ | Listed in README | Listed in SKILLS_INDEX | Adapter present | Notes |
|---|---:|---:|---:|---:|---|
| chatgpt-handoff-pilot | Yes | Yes | Yes | Yes | Core handoff protocol skill. |
| documentation-governance | Yes | Yes | Yes | Yes | Doc governance/audit role. |
| file-structure-check | Yes | Yes | Yes | Yes | Structure audit role. |
| financial-data-project-migration | Yes | Yes | Yes | Yes | Financial migration advisory baseline. |
| project-takeover | Yes | Yes | Yes | Yes | Onboarding/takeover skill. |
| skill-governance | Yes | Yes | Yes | Yes | Skill-level evaluation/refactor gating. |
| system-handoff | Yes | Yes | Yes | Yes | System-level wrapper; should remain clearly “system” scoped. |
| system-status-update | Yes | Yes | Yes | Yes | System-level wrapper over status concerns. |
| system-takeover | Yes | Yes | Yes | Yes | System architecture takeover/assessment. |
| update-project-status | Yes | Yes | Yes | Yes | Project status refresh. |
| workflow-bootstrap | Yes | No | Yes | Yes | Present canonically and in index, but omitted from README’s “当前包含的 Skills”. |

Note: Original audit notes included line-number file citations; they are retained as planning evidence context and are not upgraded here into implementation-truth claims.

## 4. Index / Inventory Inconsistencies

1. README missing `workflow-bootstrap` in top-level skill list.
2. README adapter-layer wording can be clarified to avoid SKILL.md directory-parity misunderstanding for `.github/skills`.
3. System-wrapper distinction exists in SKILLS_INDEX categories but is less explicit in README plain list.

Recommended minimal documentation fixes (planning-only, not executed):
- Add `workflow-bootstrap` to README skill list.
- Group README skills by category aligned with SKILLS_INDEX taxonomy.
- Add one-line note clarifying `system-*` skills are system-layer wrappers.

## 5. External Benchmark Matrix

| Internal Skill / Candidate | External Comparable Category | Reuse Decision | Rationale | Risk Notes |
|---|---|---|---|---|
| workflow-bootstrap | Anthropic-style workflow shell + progressive disclosure | KEEP + ABSORB | Already strong on thin-entry, canonical/reference-first, and role-chain boundaries. | Avoid verbatim template import; preserve local protocol ownership. |
| chatgpt-handoff-pilot | Microsoft-style bounded execution + acceptance/report loop | KEEP + ABSORB | Existing task package + execution report protocol is mature; can absorb acceptance checklist ideas. | Avoid overfitting to a single vendor vocabulary. |
| documentation-governance | awesome-copilot documentation governance patterns | ABSORB | Can absorb testable doc-check and consistency patterns. | Preserve provenance; avoid direct copying. |
| project-takeover | acquire-codebase-knowledge onboarding patterns | ABSORB + REFACTOR | Can strengthen evidence matrix and takeover packet standardization. | External scanning patterns may imply unsafe execution assumptions. |
| update-project-status | weekly status automation patterns | KEEP + ABSORB | Role is clear; can improve acceptance criteria and verification mode clarity. | Keep Git/non-Git boundary explicit. |
| skill-governance | governance scorecard / quality-gate styles | REFACTOR | Benefit likely from harness-like pass/fail scenario rubric. | Avoid turning governance into a second rulebook. |
| financial-data-project-migration | Python/data migration playbooks | REFACTOR (major) | Advisory baseline is good; needs deeper runtime-coupling taxonomy + executable task-package output conventions. | Avoid unsafe automation; preserve conservative posture. |
| Candidate: python-data-project-scaffold | Python package builder / data project scaffold categories | ADD | Distinct from migration diagnosis; targets greenfield/structured rebuild planning. | Enforce non-goals to prevent overreach. |
| Candidate: data-pipeline-quality-gate | data-quality gate and pipeline assurance categories | ADD | Orthogonal reusable quality-gate capability across financial pipelines. | Include confidentiality/lineage and false-positive controls. |

Short risk note: External sources are benchmarking inspiration only. Any future adoption requires license/provenance review and security review before implementation.

Recommended future benchmark report location (already used by this landing):
- `docs/reviews/external_skill_benchmark_2026-05-16.md`

## 6. `financial-data-project-migration` Enhancement Plan

### Current strengths
- Clear 4-stage flow: `scan -> understand -> structure -> output`.
- Explicit coupling checks for Wind/Excel/network path/CWD/script orchestration.
- Conservative downgrade for high-coupling scenarios.
- Strong advisory/non-destructive default boundary.

### Current gaps
- Coupling taxonomy present but not formally scored.
- No explicit decision schema for desktop-script vs package-project.
- Target `src/` layout guidance not normalized into blueprint profiles.
- Legacy wrapper strategy mentioned but not operationalized.
- Minimal testing safety net not concretely defined.
- First executable migration task-package output not explicitly templated.

### Proposed new sections (planning-only)
1. Coupling Taxonomy & Readiness Scoring
2. Desktop Script vs Package Project Decision Tree
3. Target `src/` Blueprint Profiles
4. Legacy Wrapper Strategy
5. Minimal Test Safety Net
6. First Executable Migration Task Package Template

### Proposed acceptance criteria
- Explicit readiness class and rationale.
- Coupling matrix with evidence snippets.
- One recommended and one fallback target layout.
- Wrapper strategy with rollback trigger.
- Minimal test-gate list before any file move.

### Recommended examples to add later
- Excel-heavy desktop monolith → inventory-first output.
- Mixed scripts + partial package repo → staged modularization output.
- Wind/network-drive coupled project → conservative boundary-first output.

### Boundary conditions
- No auto-move/refactor by default.
- No assumed desktop/Wind/network availability.
- No handling regulated/private datasets without explicit authorization envelope.

## 7. New Skill Candidate: `python-data-project-scaffold`

Recommendation: ADD as a standalone skill.

### Recommended scope
- Reusable scaffold planning for financial-data Python projects covering config/db/pipelines/api/cli/tests/docs/tasks/sample-data/package layout.

### Non-goals
- No full business-logic generation.
- No direct legacy migration execution.
- No infrastructure provisioning unless separately scoped.

### Candidate SKILL.md outline
1. Purpose & triggers
2. Inputs and constraints
3. Scaffold profile selection
4. Target structure proposal
5. Quality/test baseline
6. First implementation task-package draft
7. Constraints and non-goals

### Example invocation scenarios
- Scaffold planning for NAV/holdings batch analytics service.
- `src/` layout planning for FastAPI + database + batch import project.
- Greenfield package baseline to receive migrated legacy scripts.

### Relationship with existing skills
- Complementary with `financial-data-project-migration`.
- Downstream links to `documentation-governance`, `update-project-status`, `chatgpt-handoff-pilot`.

## 8. New Skill Candidate: `data-pipeline-quality-gate`

Recommendation: ADD as a standalone skill.

### Recommended scope
- Financial data pipeline gate design/review including schema/required fields/type/domain/duplicate/unique/date continuity/batch completeness/reconciliation/idempotency/manual review queues.

### Non-goals
- Not a pipeline orchestrator replacement.
- Not a full observability platform.
- Not destructive data correction.

### Candidate SKILL.md outline
1. Scope and covered data domains
2. Gate families
3. Severity model and fail/warn policy
4. Evidence/report template
5. Escalation/manual-review workflow
6. Integration notes with status/handoff
7. Constraints and boundaries

### Example invocation scenarios
- Minimum production quality gates for holdings import pipeline.
- NAV daily batch rerun-safety gate design.
- Trade/position consistency acceptance criteria design.

### Relationship with existing skills
- Pairs with `financial-data-project-migration` for pre/post migration risk control.
- Documentation alignment via `documentation-governance`.
- Progress tracking via `update-project-status`.

## 9. Prioritized Roadmap

Planning order (not active authorization):
1. Fix README / SKILLS_INDEX inventory consistency.
2. Create external skill benchmark report.
3. Enhance `financial-data-project-migration`.
4. Add `python-data-project-scaffold`.
5. Add `data-pipeline-quality-gate`.

For each stage (planning summary):
- goal
- likely inspect files
- likely future modify files
- suggested task package name
- suggested validation checks
- risk/boundary note
- local vs cloud suitability

## 10. Suggested Future Task Packages

- `skillhub_inventory_consistency_fix_v1`
- `external_skill_benchmark_baseline_v1`
- `financial_migration_skill_refactor_phase1`
- `python_data_scaffold_skill_add_v1`
- `pipeline_quality_gate_skill_add_v1`
- optional follow-up: `financial_skill_suite_cross_integration_v1`

## 11. Risks, Assumptions, and Non-Goals

### Risks
- Index drift can recur without periodic audits.
- Benchmark misuse risk if external content copied without review.
- Migration skill expansion could drift into unsafe automation.

### Assumptions
- `skills/` remains canonical SSOT.
- Adapter layers remain thin.
- This document remains evidence/reference, not authorization.

### Non-goals
- No implementation, no skill rewrites, no adapter regeneration, no automation changes in this landing task.

## 12. Final Recommendation

Decision labels:
- workflow-bootstrap: KEEP
- README/index consistency: REFACTOR (minimal)
- external ecosystem intake: ABSORB (idea-level only)
- financial-data-project-migration: REFACTOR (bounded)
- python-data-project-scaffold: ADD
- data-pipeline-quality-gate: ADD

Final boundary reminder: This review memo is planning evidence only. Any implementation must be authorized via an independent bounded task package and review cycle.
