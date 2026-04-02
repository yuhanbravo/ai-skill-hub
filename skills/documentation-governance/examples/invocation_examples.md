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
