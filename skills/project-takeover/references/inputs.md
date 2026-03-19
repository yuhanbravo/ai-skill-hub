This skill is designed to work with many repository shapes and document conventions.

Recommended project-local inputs:
- `README.md`
- `docs/**/*.md`
- task lists such as `TODO.md` or `docs/**/*task*.md`
- optional structure and documentation audit scripts

Portable configuration points:
- `doc_candidate_globs`: document discovery patterns for onboarding summaries
- `priority_task_globs`: task discovery patterns for current-priority summaries
- `support_scripts.structure`: path to a structure audit script that supports `--root` and `--json`
- `support_scripts.docs`: path to a documentation audit script that supports `--root` and `--json`

The bundled script does not require `conda`; it reports missing tools instead of crashing.
