# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use documentation-governance for this task.

task_description:
- Audit the repository documentation structure and detect duplicate markdown topics.

constraints:
- Do not rewrite docs unless explicitly allowed.
- Keep docs/ as the engineering source of truth.

expected_output:
- Documentation audit summary
- Duplicate or conflict list
- Suggested follow-up actions

context_files:
- README.md
- docs/
- docs_readable/
```

### Output Example

```text
execution_plan:
- Scan markdown files and README structure.
- Check duplicate topics and docs/docs_readable boundaries.
- Produce an audit report without applying fixes.

changes_made:
- No repository files were modified.
- Produced a governance summary with follow-up suggestions.

files_touched:
- README.md
- docs/
- docs_readable/

risks:
- Some duplicate-topic judgments still require project-local confirmation.
```

### Mutable Status SSOT Example

```text
Use documentation-governance for this task.

task_description:
- Add technical onboarding docs for a repository without weakening the current-state SSOT.

correct_pattern:
- Keep architecture docs focused on stable module relationships, data flow, runbook commands, and file governance.
- Let README.md and docs/README.md act as navigation entrypoints.
- Let CLAUDE.md or AGENTS.md act as thin agent wrappers.
- Link current phase, completed work, next phase, latest validation, blocker, and pending-merge facts back to the declared HANDOFF/status SSOT.

anti_pattern:
- README.md repeats the current phase, completed phase list, and next phase.
- docs/technical/architecture_overview.md repeats active status and pending-merge state.
- CLAUDE.md or AGENTS.md copies latest validation results as if it were a second handoff.
- Blueprint docs become a parallel status tracker instead of roadmap context.

expected_output:
- Identify status facts that should move back to the current-state SSOT.
- Recommend replacing duplicated status facts with SSOT links.
- Preserve stable technical onboarding content.
```


## Audience-aware Round 1

- Built-in audience model: `human_machine_shared`, `human_primary_archive`, `ai_only_wrapper`, `unknown_or_mixed`.
- Built-in authority roles and doc intents are emitted in report fields without replacing existing `document_layer` model.
- Built-in conflict checks include AI-only SSOT misuse, shared-doc agent-only instructions, archive-as-current-fact references, navigation status duplication, and language mismatch for shared docs.
- Round 1 remains internal-only and does not integrate markdownlint/lychee/Vale/textlint.
