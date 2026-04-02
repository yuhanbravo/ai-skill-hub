# Invocation Examples

These examples were split out of `SKILL.md` to keep the execution contract focused.

### Input Example

```text
Use chatgpt-handoff-pilot for this task.

task_description:
- Prepare a bounded handoff package for updating docs/HANDOFF.md.

constraints:
- Do not edit any Python scripts.
- Keep docs/HANDOFF.md as the single source of truth.

expected_output:
- Updated handoff document
- Execution report

context_files:
- docs/HANDOFF.md
- AGENTS.md
```

### Output Example

```text
execution_plan:
- Read the handoff package and local handoff rules.
- Update docs/HANDOFF.md section by section.
- Return a bounded execution report.

changes_made:
- Updated Current Status and Recommended Next Steps in docs/HANDOFF.md.
- Did not modify legacy generated handoff files.

files_touched:
- docs/HANDOFF.md

risks:
- Some acceptance criteria were inferred from the task package and should be confirmed.
```

`chatgpt-handoff-pilot` 最适合解决“任务需要先拆清楚，再交给另一个实施侧严格落地”的协作问题。它的价值不在于流程复杂，而在于稳定输入、边界和回执。

使用这个 skill 时，最重要的边界是保持最小化定位，不把它扩写成完整框架；最重要的规则是先明确任务包，再按范围执行，并在结束后回传结构化 `execution report`。当它被用于项目 handoff 文档时，默认应把内容收口到 `docs/HANDOFF.md` 这一份单一主文档，并通过 `Update Log + section-aware merge` 的方式长期维护，而不是继续产生新的平行手册。
