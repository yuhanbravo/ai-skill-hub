# Anti-Pattern Guide

This file explains common failure modes already governed by `SKILL.md`.

## Typical Failure Modes

- creating a new markdown file for every revision
- keeping sibling files with version suffixes
- splitting one engineering truth across multiple peer documents
- mirroring `docs/` into `docs_readable/` without a reader need
- allowing `docs_readable/` to state decisions, status, or current state not grounded in `docs/`

## Review Questions

Use these questions before adding a document:

1. Is there already a same-topic canonical file?
2. Can the content be merged instead?
3. Would the new file create a second truth source?

If any answer is yes, the likely next step is merge, not creation.
