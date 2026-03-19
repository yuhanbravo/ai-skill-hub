Use this skill when a project has its own documentation policy, heading vocabulary, or multilingual README requirements.

Recommended configuration points:
- `styleguide_paths`: ordered candidate files to probe for the project style guide
- `styleguide_required_section_headings`: accepted section titles inside the style guide that define required README sections
- `readme_section_aliases`: canonical section names mapped to heading aliases across languages
- `template_language`: `auto`, `en`, or `zh`

The parser reads list items that appear under the configured style-guide heading. If a project uses unusual prose-only guidance, prefer adding a project-local override config instead of changing the bundled defaults.

For Documentation Governance OS, treat the style guide as a local override layer. It may refine naming, category, or README policy, but it must not violate the anti-pattern rules in `anti_pattern.md`.
