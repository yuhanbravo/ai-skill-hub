# AMS_Report Documentation Governance Dogfood Audit

Date: 2026-05-28

## 1. Scope

This was a read-only dogfood audit of `AMS_Report` using the audience-aware Round 1 behavior added to `documentation-governance` after ai-skill-hub PR #9.

- Target project: `Z:\营销材料\Python_Lib\AMS_Report`
- Checker-resolved root: `\\172.16.20.110\hxhyFile\营销材料\Python_Lib\AMS_Report`
- Skill source: `D:\dev\ai-skill-hub`
- Git state checked: `main` at `e0c2446 (HEAD -> main, origin/main, origin/HEAD) documentation-governance: add audience-aware Round 1 classifier and conflict checks (#9)`
- Script used: `D:\dev\ai-skill-hub\skills\documentation-governance\scripts\check_documentation_governance.py`
- Config used: `D:\dev\ai-skill-hub\skills\documentation-governance\references\default_governance.json`

No `AMS_Report` files were modified. No `documentation-governance` skill, script, config, catalog, registry, adapter, CI, validator, or bridge-doc implementation files were modified. The only written artifact was this dogfood audit report under `D:\dev\ai-skill-hub\tasks\`.

## 2. Commands Run

### Confirm ai-skill-hub main state

```powershell
git -c safe.directory=D:/dev/ai-skill-hub -C D:\dev\ai-skill-hub status --short --branch
git -c safe.directory=D:/dev/ai-skill-hub -C D:\dev\ai-skill-hub log -1 --oneline --decorate
git -c safe.directory=D:/dev/ai-skill-hub -C D:\dev\ai-skill-hub branch --show-current
```

Result: success.

Key output:

```text
## main...origin/main
e0c2446 (HEAD -> main, origin/main, origin/HEAD) documentation-governance: add audience-aware Round 1 classifier and conflict checks (#9)
main
```

Notes:

- Git emitted sandbox-user warnings for `C:\Users\imado/.config/git/ignore` and `.pytest_cache/`, but repository state was still readable.
- Initial direct Git reads without `safe.directory` failed due Git dubious ownership protection; rerun used one-shot `-c safe.directory=...` and did not edit global Git config.

### Run documentation-governance checker

```powershell
& "D:\dev\dev_tools\run-conda-python.cmd" dev-core-py312 `
  skills\documentation-governance\scripts\check_documentation_governance.py `
  --root "Z:\营销材料\Python_Lib\AMS_Report" `
  --config "D:\dev\ai-skill-hub\skills\documentation-governance\references\default_governance.json" `
  --dry-run `
  --report "D:\dev\ai-skill-hub\tasks\ams_report_documentation_governance_dogfood_audit_2026-05-28.md"
```

Result: success.

Key stdout summary:

```text
Scanned files: 12
Style guide found: no
Engineering docs root: docs (present)
Readable docs root: docs_readable (missing)
Engineering docs count: 11
Readable docs count: 0
High Priority Issues:
- navigation_doc_duplicates_mutable_status: README.md
- archive_referenced_as_current_fact: docs/HANDOFF.md
- archive_referenced_as_current_fact: docs/SCRIPT_MAP.md
- archive_referenced_as_current_fact: docs/status.md
Language Findings:
- README.md
- docs/README.md
- docs/status.md
```

No stderr failure was observed.

### Read-only review commands

Read-only `Get-Content` and `rg` commands were used against the marked AMS_Report markdown files to classify true positives, false positives, acceptable advisories, config gaps, and skill behavior gaps. Because `Z:` is not mounted for the sandbox user, these read commands were run with elevated access and did not write to AMS_Report.

## 3. Audience Classification Summary

### ai_only_docs

None detected.

Judgment: correct for the current scanned file set. The project does not expose `AGENTS.md`, `.agents/`, `.codex/`, or configured AI-only wrapper docs in the scanned markdown set.

### human_primary_docs

Detected as `human_primary_archive`:

- `docs/archive/README.md`
- `docs/archive/strategy-return-max-drawdown/最大回撤修复说明.md`
- `docs/archive/strategy-return-max-drawdown/最大回撤修复说明_更新版.md`
- `docs/archive/strategy-return-max-drawdown/最大回撤修复说明_最终版.md`

Judgment: correct. These files are explicitly under `docs/archive/` and are historical/superseded notes.

### shared_docs

Detected as `human_ai_shared`:

- `README.md` -> `navigation_index`, `navigation`
- `docs/README.md` -> `navigation_index`, `navigation`
- `docs/status.md` -> `current_status_ssot`, `status`
- `docs/HANDOFF.md` -> `handoff_ssot`, `handoff`
- `docs/AMS_Report_SSOT治理记录_20260515.md` -> `stable_reference`, `reference`
- `docs/MIGRATION_BLUEPRINT.md` -> `stable_reference`, `reference`
- `docs/SCRIPT_MAP.md` -> `stable_reference`, `reference`
- `docs/TECH_DEBT.md` -> `stable_reference`, `reference`

Judgment: mostly correct. `docs/status.md`, `docs/HANDOFF.md`, and both README files were classified with useful roles. The default fallback of all other `docs/*.md` files to shared stable references is acceptable for Round 1.

### unknown_or_mixed

None detected.

Judgment: acceptable. The configured scan set is entirely README or `docs/**`, so every scanned file has a deterministic audience class.

### Clear Correct Cases

- `docs/status.md` as `current_status_ssot`: correct and useful.
- `docs/HANDOFF.md` as `handoff_ssot`: correct and useful.
- `docs/archive/**` as `human_primary_archive`: correct and useful.
- `README.md` and `docs/README.md` as navigation indexes: correct.

### Possible Classification Limits

- The classifier does not currently distinguish "historical governance record" from general stable reference, so `docs/AMS_Report_SSOT治理记录_20260515.md` becomes `stable_reference`. This is acceptable for now, but a future `governance_record` role could improve reporting.

## 4. Findings Review

### audience_conflicts

| Finding | File | Judgment | Review |
| --- | --- | --- | --- |
| `navigation_doc_duplicates_mutable_status` | `README.md` | `false_positive` / `skill_gap` | The root README contains a "Governance Notes" sentence saying navigation docs should link to `docs/status.md` instead of duplicating mutable facts. This is not duplicating status; it is stating the SSOT rule. The heuristic fires because the navigation doc includes the phrase "mutable project status". |
| `archive_referenced_as_current_fact` | `docs/HANDOFF.md` | `false_positive` / `skill_gap` | The file explicitly says archived Strategy assets are not current facts and links `docs/archive/strategy-return-max-drawdown/` only for traceability. The checker sees `docs/archive/` plus "current" language and flags it, but the semantic meaning is the opposite of the finding. |
| `archive_referenced_as_current_fact` | `docs/SCRIPT_MAP.md` | `false_positive` / `skill_gap` | The script map has a dedicated historical section for archived `Strategy_Data.py` / `Strategy_Return.py`, stating they are not active scripts. It references archive as history, not current fact. |
| `archive_referenced_as_current_fact` | `docs/status.md` | `false_positive` / `skill_gap` | The status doc says `docs/archive/` is not a current engineering fact source. This is a healthy boundary statement and should not be high priority. |

Overall audience_conflicts judgment: the categories are useful, but the archive-current heuristic is too broad. It should avoid flagging explicit negations or phrases like "not current", "not a current engineering fact source", "historical", "archived", and "traceability".

### language_findings

| Finding | File | Judgment | Review |
| --- | --- | --- | --- |
| `language_mismatch_for_shared_doc` | `README.md` | `acceptable advisory` / `config_gap` | The root README is English-dominant in a zh-first config. That is a reasonable advisory, not a high-risk finding. |
| `language_mismatch_for_shared_doc` | `docs/README.md` | `acceptable advisory` / `config_gap` | The docs index is English-dominant but short and navigational. Advisory is acceptable. |
| `language_mismatch_for_shared_doc` | `docs/status.md` | `acceptable advisory` / `config_gap` | The status doc is English-dominant. Given AMS_Report's mixed-language documentation style, this is useful only as a soft signal. |

Overall language_findings judgment: usable as advisory. The `latin > cjk * 8` heuristic is simple and works as a low-cost first pass, but this project needs either local config to allow English navigation/status docs or severity labeling to prevent language findings from feeling like correctness failures.

### archive/current-fact issues

Judgment: `skill_gap`.

The checker found the right document family to inspect, but the archive-current fact rule needs semantic guardrails. In AMS_Report, current docs correctly say:

- archived Strategy files are historical assets;
- archive docs are retained for traceability;
- archive is not a current engineering fact source;
- restoring archived scripts requires a separate task.

These are governance-positive statements. The tool should not classify them as archive content being referenced as current fact.

### navigation/status duplication issues

Judgment: `false_positive` for `README.md`, with a smaller `skill_gap`.

`README.md` links to `docs/status.md` and includes a governance note telling readers not to duplicate mutable operational facts. That note supports the intended SSOT model. The checker should distinguish "declares status SSOT boundary" from "duplicates mutable status facts".

### README required-section findings

| Finding | File | Judgment | Review |
| --- | --- | --- | --- |
| Missing `overview` | `README.md` | `acceptable advisory` | The README has a one-line project description under the title but lacks an explicit configured heading. Useful style nudge, not a dogfood blocker. |
| Missing `installation` | `README.md` | `acceptable advisory` | The project is a local script workspace without a standard install flow. A setup/prerequisites section would help, but omission is understandable. |

### Heading issues

| Finding | File(s) | Judgment | Review |
| --- | --- | --- | --- |
| H1 to H3 jumps | archived max-drawdown docs | `acceptable advisory` | Real markdown structure issues, but all are in archived historical docs. Good to report as advisory; not important for current governance. |

### Layer and duplicate checks

| Area | Judgment | Review |
| --- | --- | --- |
| Layer placement conflicts | `true_positive_absence` | No conflicts detected; this matches the project shape. |
| Duplicate candidates | `true_positive_absence` | No duplicate topic candidates detected; reasonable. |
| Engineering SSOT conflicts | `true_positive_absence` | No engineering-layer SSOT conflicts detected; matches the explicit status/handoff split. |
| Readable second-truth conflicts | `true_positive_absence` | No readable layer exists, so none should be detected. |
| Readable generation targets | `acceptable advisory_absence` | No missing readable summaries detected. Given `docs_readable` is missing, this is acceptable under the default config. |
| API docs | `acceptable advisory_absence` | No API docs detected; correct for a script workspace and `require_api_docs=false`. |

## 5. Skill Dogfood Judgment

Conclusion: Go with follow-ups.

Round 1 is usable on a real project. The audience classifier correctly separates navigation docs, status SSOT, handoff SSOT, stable references, and archive docs. The checker ran cleanly in dry-run mode and produced explainable output.

However, the high-priority audience conflict output is currently too noisy for AMS_Report. Three archive-current findings and one navigation-status finding are false positives caused by broad keyword matching. These should be addressed before treating high-priority audience conflicts as implementation blockers in downstream workflows.

## 6. Follow-up Recommendations

### AMS_Report follow-ups

- Consider adding explicit README headings for `Overview` / `项目概览` and setup/prerequisites if this project is meant to be maintained by new operators.
- Consider deciding whether root README, docs README, and status should be Chinese-first or intentionally bilingual/English-dominant.
- Optionally normalize heading levels in archived max-drawdown docs if archived docs are still frequently read. This is not urgent.
- Do not treat the current archive references in `HANDOFF.md`, `SCRIPT_MAP.md`, or `status.md` as defects; they are useful boundary statements.

### documentation-governance skill follow-ups

- Refine `archive_referenced_as_current_fact` to account for negation and historical/traceability context.
- Refine `navigation_doc_duplicates_mutable_status` so SSOT boundary statements do not count as duplicated mutable status facts.
- Add severity levels for audience and language findings, especially `advisory` vs `high_priority`.
- Consider a project-local config option for language posture, such as `allow_english_navigation_docs` or per-path language overrides.
- Consider a `governance_record` / `historical_governance_record` authority role for files like `docs/AMS_Report_SSOT治理记录_20260515.md`.
- Include grouped summary lists in the report for `ai_only_docs`, `human_primary_docs`, `shared_docs`, and `unknown_or_mixed`, not only per-file classification lines.

### Noise not recommended for immediate handling

- Do not ask AMS_Report to remove archive references that explicitly say archive is historical or not current.
- Do not treat English-dominant short navigation/status docs as hard failures.
- Do not require `docs_readable/` for this project unless a human-readable layer is actually part of its governance target.
- Do not prioritize archived heading-level cleanup over current documentation governance work.

## 7. AI_Workbench Update Recommendation

Recommendation: advance `pending_trigger` from `dogfood_in_progress` to `dogfood_recorded`.

Rationale:

- The checker was run successfully against AMS_Report in dry-run mode.
- The dogfood findings were reviewed and categorized.
- The audit identified concrete true utility and concrete follow-up gaps.
- No implementation changes were made to AMS_Report or documentation-governance.

Do not mark fully `done` yet if `done` implies the Round 1 follow-up gaps are resolved. Use `dogfood_recorded` as the accurate next state, with follow-up issues/tasks for heuristic refinement.
