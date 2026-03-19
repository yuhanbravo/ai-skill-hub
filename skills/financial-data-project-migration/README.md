# Financial Data Project Migration

This skill helps a financial-data Python project move from scattered scripts toward a standard `src`-based engineering structure.

It does:
- Judge the current project type and migration stage.
- Suggest a target structure for a `src` transition.
- Classify current files by role.
- Produce a minimal migration TODO for the next step.

It does not:
- Perform large-scale refactors.
- Move files automatically.
- Integrate with live business repositories in this first version.

It fits projects such as:
- Data extraction repositories.
- Analysis and reporting repositories.
- Batch pipeline repositories.
- Hybrid migration-state repositories that mix root scripts with emerging package structure.

First-version output includes:
- Project type judgment.
- Migration stage judgment.
- Target structure recommendation.
- File role classification.
- Minimal migration TODO.
