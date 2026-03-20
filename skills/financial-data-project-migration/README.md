# Financial Data Project Migration

This skill helps a financial-data Python project move from scattered scripts toward a more maintainable structure without forcing a rewrite.

It does:
- Judge the current project type and migration stage.
- Detect conservative high-risk migration signals for desktop Excel + Wind projects.
- Suggest a target structure for a later `src` transition.
- Classify current files by role.
- Produce a minimal migration TODO for the next step.
- Include example mapping candidates from the current project.

It does not:
- Perform large-scale refactors.
- Move files automatically.
- Integrate with live business repositories in this first version.

It fits projects such as:
- Data extraction repositories.
- Analysis and reporting repositories.
- Batch pipeline repositories.
- Hybrid migration-state repositories that mix root scripts with emerging package structure.
- Desktop Excel + Wind + network-share coupled script projects.

First-version output includes:
- Project type judgment.
- Migration stage judgment.
- Fixed risk assessment.
- Target structure recommendation with example mapping candidates.
- File role classification.
- Minimal migration TODO.
