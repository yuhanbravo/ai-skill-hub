# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use skill-governance on <skill-path>
rewrite=false
```

If rewrite is explicitly allowed:

```text
Use skill-governance on <skill-path>
rewrite=true
```

### Output Example

```text
execution_plan:
- Evaluate the target skill against the template.
- Produce SCORECARD, DIAGNOSIS, and LEVEL.
- Decide whether rewrite is allowed.

changes_made:
- No rewrite was performed because rewrite=false.

files_touched:
- skills/<target-skill>/SKILL.md
- skills/<target-skill>/README.md

risks:
- A rewrite decision without enough evidence may cause unnecessary drift.
```

See also:

* prompts/skill-invocation.md
