# System Status to Handoff Refresh Prompt

Purpose: copyable invocation prompt for system-level status-first refresh followed by handoff refresh.

Canonical owner: `system-status-update`
Handoff receiver: `system-handoff`

Boundary:
- This prompt is system-level and status-first.
- Project-level cross-skill post-dev dual-refresh remains owned by `workflow-bootstrap`.
- `system-status-update` owns layer / phase / capability / stability status output.
- `system-handoff` receives the status baseline and owns handoff section merge output.
- Do not copy the project-level dual-refresh prompt into this system-level flow.

```text
Please run a system-level status-to-handoff refresh.

First use `system-status-update` to refresh the system status baseline.
Then pass a concise status baseline to `system-handoff` for section-aware handoff refresh.

Inputs:
- System root: <system-root>
- Status artifact: <status-artifact-path>
- Handoff artifact: <handoff-artifact-path>
- Refresh mode: <dry-run | write>
- Handoff write authorization: <yes | no>
- Status evidence pointers:
  - Canonical Skill Layer: <pointers>
  - Distribution Layer: <pointers>
  - Governance Layer: <pointers>
  - Tooling Layer: <pointers>
- Current phase: <phase-or-unknown>
- Capabilities: <capability-summary-placeholders>
- Stability: <stability-summary-placeholders>
- Validation provenance: <commands-or-reason-not-run>
- Assumptions: <explicit assumptions>

Execution boundaries:
- Refresh system status before handoff.
- Keep system status output layer-based; do not turn it into a file-level change list.
- Pass only status snapshot fields and handoff-relevant boundaries into `system-handoff`.
- Let `system-handoff` handle handoff refresh and handoff output boundaries.
- Run phase consistency check before handoff write if both artifacts are updated.
- Do not modify adapters, indexes, tools, or project-level prompt assets.

Expected output:
- Status snapshot: Layer Status, Current Phase, Capabilities, Stability, Risks / Gaps.
- Handoff refresh boundary: target sections, status baseline used, phase consistency result, write result.
- Linked refresh receipt: status result, handoff result, validation provenance, assumptions, remaining risks, next action.

Stop conditions:
- The target is a normal project rather than the `ai-skill-hub` system or another capability system.
- Status baseline cannot be established but handoff write is requested.
- Phase consistency cannot be checked for a requested handoff write.
- The run would require project-level dual-refresh ownership, adapter edits, tool logic changes, or unverified system facts.
```
