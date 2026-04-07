# 示例 REVIEW_PACKET：phase-2 boundary review

## 任务标识

- 名称：phase-2 boundary review
- 阶段：`chatgpt-handoff-pilot` supporting assets 最小增强
- 日期：2026-04-07
- 对应 task package：`examples/example_task_package.md`
- 对应 execution report：`examples/example_execution_report.md`

## 本轮目标

- 为 `chatgpt-handoff-pilot` 补一层最小 `review packet` 资产
- 保持 skill 仍是轻量 handoff 母版，不扩成重型机制

## 本轮实际改动摘要

- 新增 `REVIEW_PACKET` 模板
- 新增面向 Codex / Copilot / ChatGPT 的 review packet prompt
- 新增最小 review packet 示例
- 在 `README.md` 和 `SKILL.md` 中补充 review packet 的轻量说明

## 涉及文件

- `skills/chatgpt-handoff-pilot/templates/REVIEW_PACKET_TEMPLATE.md`
- `skills/chatgpt-handoff-pilot/prompts/review_packet_prompts.md`
- `skills/chatgpt-handoff-pilot/examples/example_review_packet.md`
- `skills/chatgpt-handoff-pilot/README.md`
- `skills/chatgpt-handoff-pilot/SKILL.md`

## 明确未改 / 明确不在本轮范围

- 未新建独立 skill
- 未新增脚本、校验器、状态机、生成器
- 未修改任何业务项目脚本
- 未重写 `chatgpt-handoff-pilot` 的核心模式

## 验证摘要

- 已检查新增内容全部位于 `skills/chatgpt-handoff-pilot/` 内
- 已确认 `review packet` 与 `task package`、`execution report` 的边界单独写明
- 已确认 `SKILL.md` 仍保持 execution-focused，解释性内容主要放在 supporting assets / `README.md`

## 当前阻塞 / 风险 / 待确认

- 当前只有静态模板与示例，尚未经过多轮真实网页端审阅反馈验证
- 后续如果审阅侧希望固定输出格式，可能还需要再压缩字段，但这不属于本轮范围

## 希望审阅者重点审什么

- 这组新增资产是否已经足够支持“少复制粘贴”的审阅场景
- 当前模板字段是否已经少而够用
- `review packet` 与 `task package`、`execution report` 的边界是否清楚

## 必要上下文

- 相关文档：`README.md`、`SKILL.md`、`templates/EXECUTION_REPORT_TEMPLATE.md`
- 相关本地规则：保持 `chatgpt-handoff-pilot` 为最小 handoff 壳层，不引入自动化或新治理机制
- 必要日志/报错片段：无
