# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use system-status-update for this task.

task_description:
- Refresh ai-skill-hub as a capability system and report the current layer status.

constraints:
- Reuse update-project-status as the canonical status engine.
- Do not output file-level change lists.

expected_output:
- Layer Status
- Current Phase
- Capabilities
- Stability

context_files:
- docs/status/skill-hub-status.md
- skills/
- .agents/
- .github/
- tools/
```

### Output Example

```text
Layer Status:
- Canonical Skill Layer: stable
- Distribution Layer: evolving
- Governance Layer: evolving
- Tooling Layer: evolving

Current Phase:
- Phase 3 - Controlled System

Capabilities:
- Stable canonical source of truth
- Repeatable project-local distribution
- Read-only drift detection

Stability:
- canonical: stable
- system rollout: evolving

Risks:
- Some maturity judgments may remain provisional if enforcement evidence is incomplete.
```
