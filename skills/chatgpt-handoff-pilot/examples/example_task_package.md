# 示例任务包：phase-2 boundary review

## 任务标识

- 名称：phase-2 boundary review
- 阶段：Long_Short_Fund_Analysis skill 试跑
- 提交方：上游方案侧
- 日期：2026-03-20

## 背景

当前仓库已经新增了 `chatgpt-handoff-pilot` skill 母版，但还缺少最小模板、示例和开发备注，不利于在真实项目中试跑 handoff 流程。

## 本次目标

- 在 `.codex/skills/chatgpt-handoff-pilot/` 内补齐最小可试跑资产
- 保持 skill 为母版定位，不引入复杂自动化
- 让新同事或 AI 可以直接按模板完成一次 handoff 输入输出演练

## 本次范围

- 允许修改：`.codex/skills/chatgpt-handoff-pilot/` 下的文档与模板
- 重点关注：`SKILL.md`、`README.md`、模板、示例、开发备注

## 明确不做

- 不修改 `Strategy_Data.py`
- 不修改 `Strategy_Return.py`
- 不修改业务脚本
- 不调整项目其他业务文档

## 目标文件或目录

- `.codex/skills/chatgpt-handoff-pilot/SKILL.md`
- `.codex/skills/chatgpt-handoff-pilot/README.md`
- `.codex/skills/chatgpt-handoff-pilot/templates/`
- `.codex/skills/chatgpt-handoff-pilot/examples/`

## 验收标准

- skill 目录下新增最小模板、示例和开发备注
- `SKILL.md` 补充任务包字段、实施回执边界、额外问题处理规则
- `README.md` 补充真实项目接入方式、推荐目录、最小 workflow
- 所有内容中文为主，简洁实用

## 约束条件

- 只做最小增强
- 不把文档写成抽象方法论
- 与项目本地规则冲突时，以项目本地规则为准

## 输出要求

- 需要 execution report
- 需要列出风险/待确认项
- 需要附简短验证说明

## 补充上下文

- 相关文档：`.codex/skills/chatgpt-handoff-pilot/README.md`
- 参考说明：本次用于 Long_Short_Fund_Analysis 内部试跑 handoff skill
