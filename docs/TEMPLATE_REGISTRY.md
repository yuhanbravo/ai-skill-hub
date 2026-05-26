# Template Registry

## Status / Source Notice
- 本文档是 **index**，不是模板正文存放地。
- 所有 templates / snippets / prompts / examples 保持在原始路径，不迁移、不复制。
- `tasks/` 中内容仅可作为 historical / candidate evidence，除非后续独立 task 显式晋升，否则不是 canonical。

## How to use this registry
1. 先按 `asset type` 与 `intended use case` 过滤。
2. 再核对 `canonical status` 与 `source surface`，避免把 adapter/bridge/historical 当作 authoring source。
3. 最后进入 `asset path` 使用原文件，不在本注册表内复制内容。

## Canonical status vocabulary
- `canonical`
- `supporting asset`
- `adapter / discovery copy`
- `bridge mirror / reference`
- `historical / candidate`
- `unknown / needs review`

## Template / Asset Registry

| asset path | asset type | owner skill | canonical status | intended use case | source surface | side-effect level | notes |
|---|---|---|---|---|---|---|---|
| `skills/SKILL_TEMPLATE.md` | template | N/A (skill authoring baseline) | canonical | 创建新 skill 时作为最小结构模板 | `skills/` | documentation-only | skill 元模板，非业务实现模板 |
| `skills/chatgpt-handoff-pilot/templates/TASK_PACKAGE_TEMPLATE.md` | template | `chatgpt-handoff-pilot` | supporting asset | 起草标准 task package | `skills/` | documentation-only | 交接输入标准化 |
| `skills/chatgpt-handoff-pilot/templates/EXECUTION_REPORT_TEMPLATE.md` | template | `chatgpt-handoff-pilot` | supporting asset | 输出结构化 execution report | `skills/` | documentation-only | 交接回执标准化 |
| `skills/chatgpt-handoff-pilot/templates/REVIEW_PACKET_TEMPLATE.md` | template | `chatgpt-handoff-pilot` | supporting asset | 生成轻量 review packet | `skills/` | documentation-only | 审阅辅助，不替代 task package |
| `skills/chatgpt-handoff-pilot/templates/HANDOFF_CHECKLIST.md` | template | `chatgpt-handoff-pilot` | supporting asset | 交接前检查边界与必填项 | `skills/` | read-only | checklist 型资产 |
| `skills/chatgpt-handoff-pilot/prompts/reusable_prompts.md` | prompt | `chatgpt-handoff-pilot` | supporting asset | 复用交接提示词 | `skills/` | documentation-only | prompt 库 |
| `skills/chatgpt-handoff-pilot/prompts/review_packet_prompts.md` | prompt | `chatgpt-handoff-pilot` | supporting asset | 审阅包提示词 | `skills/` | documentation-only | review-focused prompts |
| `skills/chatgpt-handoff-pilot/examples/example_task_package.md` | example | `chatgpt-handoff-pilot` | supporting asset | 参考 task package 写法 | `skills/` | read-only | 示例，不是模板强约束 |
| `skills/chatgpt-handoff-pilot/examples/example_execution_report.md` | example | `chatgpt-handoff-pilot` | supporting asset | 参考 execution report 写法 | `skills/` | read-only | 示例，不是 canonical 协议文本 |
| `skills/workflow-bootstrap/orchestration_snippets.md` | snippet | `workflow-bootstrap` | supporting asset | 协作编排片段复用 | `skills/` | documentation-only | workflow shell 片段 |
| `skills/workflow-bootstrap/examples/invocation_examples.md` | example | `workflow-bootstrap` | supporting asset | 查询 workflow-bootstrap 触发与调用方式 | `skills/` | read-only | 仅示例入口 |
| `skills/update-project-status/templates/skillhub_status_template.md` | template | `update-project-status` | supporting asset | 状态文档刷新时的结构参考 | `skills/` | status / handoff update | 状态模板，不是实时状态事实 |
| `.agents/skills/chatgpt-handoff-pilot/SKILL.md` | adapter | `chatgpt-handoff-pilot` | adapter / discovery copy | agent discovery fallback | `.agents/skills/` | read-only | 非 canonical authoring surface |
| `.github/skills/chatgpt-handoff-pilot.md` | adapter | `chatgpt-handoff-pilot` | adapter / discovery copy | GitHub Copilot discovery fallback | `.github/skills/` | read-only | 非 canonical authoring surface |
| `docs/bridge/templates/TASK_PACKAGE_TEMPLATE.md` | template | bridge mirror | bridge mirror / reference | 历史 mirror 参考 | `docs/bridge/` | read-only | mirror/reference，不作为 active template source |
| `docs/bridge/templates/EXECUTION_REPORT_TEMPLATE.md` | template | bridge mirror | bridge mirror / reference | 历史 mirror 参考 | `docs/bridge/` | read-only | 需优先回到 `skills/` 原始资产 |
| `tasks/copilot-codex-workflow_phase3a_template_sketch_task_package.md` | candidate | N/A | historical / candidate | 参考阶段性 template sketch 结构 | `tasks/` | read-only | historical evidence，不自动晋升 canonical |
| `tasks/workflow-bootstrap_phase3_runtime_pack_minimal_manifest_task_package.md` | candidate | N/A | historical / candidate | 参考 runtime-pack 相关 task package 形态 | `tasks/` | read-only | 候选模式，需独立审批才能推广 |
| `tasks/post_dev_dual_refresh_orchestration_template_task_package.md` | candidate | N/A | historical / candidate | 参考 post-dev orchestration task 包结构 | `tasks/` | read-only | 仅代表历史执行实践 |
