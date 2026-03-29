---
name: update-project-status
description: "Adapter entry for Git-based status refresh, weekly summaries, and handoff-ready project updates. Canonical source is in skills/update-project-status."
metadata:
  triggers:
    - refresh project status from Git history
    - generate a weekly project summary
    - merge commits and task sources into a status report
    - sync project status to a shared document
    - produce a handoff status update
  side_effects:
    - read_only
    - write_files
    - requires_git
  canonical_path: ../../../skills/update-project-status
  adapter_type: thin-wrapper
---

# update-project-status

- Canonical skill directory: `../../../skills/update-project-status`
- Canonical skill definition: `../../../skills/update-project-status/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
