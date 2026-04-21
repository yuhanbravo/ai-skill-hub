---
name: workflow-bootstrap
description: "Adapter entry for the default Copilot-led / Codex-implemented workflow shell, minimal role split, and future runtime-pack mapping. Canonical source is in skills/workflow-bootstrap."
metadata:
  triggers:
    - bootstrap a Copilot-led Codex-implemented workflow
    - define planner implementer reviewer boundaries
    - map canonical guidance to a future runtime pack
    - explain thin entry versus full canonical guidance
    - document workflow shell boundaries without replacing handoff protocols
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/workflow-bootstrap
  adapter_type: thin-wrapper
---

# workflow-bootstrap

- Canonical skill directory: `../../../skills/workflow-bootstrap`
- Canonical skill definition: `../../../skills/workflow-bootstrap/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
