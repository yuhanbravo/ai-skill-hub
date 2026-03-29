---
name: documentation-governance
description: "Adapter entry for documentation audits, duplicate markdown detection, and README governance. Canonical source is in skills/documentation-governance."
metadata:
  triggers:
    - audit repository documentation structure
    - detect duplicate markdown documents
    - fix README governance issues
    - classify docs and docs_readable layers
    - archive or merge outdated documentation
  side_effects:
    - read_only
    - write_files
  canonical_path: ../../../skills/documentation-governance
  adapter_type: thin-wrapper
---

# documentation-governance

- Canonical skill directory: `../../../skills/documentation-governance`
- Canonical skill definition: `../../../skills/documentation-governance/SKILL.md`
- Use this wrapper for discovery only. Read the canonical skill before execution.
