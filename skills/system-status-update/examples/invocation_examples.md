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
- If `Updated at` is older than 14 days, add a `Staleness` risk item.

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

### System Status to Handoff Linked Refresh Example

```text
Use system-status-update for a system-level status-first linked refresh.
Prompt asset: skills/system-status-update/prompts/system_status_to_handoff_refresh_prompt.md

System root: <system-root>
Status artifact: <status-artifact-path>
Handoff artifact: <handoff-artifact-path>
Refresh mode: <dry-run | write>
Handoff write authorization: <yes | no>
Status evidence pointers:
- Canonical Skill Layer: <pointers>
- Distribution Layer: <pointers>
- Governance Layer: <pointers>
- Tooling Layer: <pointers>
Current phase: <phase-or-unknown>
Validation provenance: <commands-or-reason-not-run>
```

Expected output categories:

- status snapshot with Layer Status, Current Phase, Capabilities, Stability
- handoff refresh boundary for `system-handoff`
- phase consistency result
- linked refresh receipt with risks, assumptions, and next action

Boundary note:

- Project-level post-dev dual-refresh remains owned by `workflow-bootstrap`.
- System-level status-first linked refresh remains owned by `system-status-update` and hands off only the handoff refresh boundary to `system-handoff`.
