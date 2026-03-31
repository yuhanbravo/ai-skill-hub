---
name: system-status-update
description: "Adapter entry for updating ai-skill-hub system status with layer-oriented output constraints. Canonical source is in skills/system-status-update."
metadata:
  triggers:
    - refresh ai-skill-hub system status
    - update skill-hub layer status and phase
    - generate a capability-system status summary
    - produce layer-oriented status for ai-skill-hub
    - summarize canonical distribution governance and tooling layers
  side_effects:
    - read_only
    - write_files
    - requires_git
  canonical_path: ../../../skills/system-status-update
  adapter_type: thin-wrapper
---

# system-status-update

- Canonical skill directory: `../../../skills/system-status-update`
- Canonical skill definition: `../../../skills/system-status-update/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.