# ChatGPT Handoff Pilot

`chatgpt-handoff-pilot` 是一个最小可用的 handoff skill 母版，用来验证这种协作模式是否适合真实项目：

- ChatGPT 负责架构、方案拆解、约束说明、审稿
- Codex 或 Copilot 负责按任务包实施并输出 execution report

## 这是什么

这是母版，不是最终项目接入状态。

它的目标是先把最小协作框架写清楚，方便后续复制到真实项目中试跑，而不是在当前仓库里做复杂封装。

## 如何使用

后续需要把这个 skill 复制到真实项目的 `.codex/skills/` 中，再结合项目自己的目录结构、任务流和验收方式进行试跑。

推荐配合以下内容一起使用：

- `AGENTS.md`
- `docs/HANDOFF.md`、`docs/TASKBOARD.md` 或类似任务来源文档
- `ai/tasks/` 或其他任务包目录
- `ai/execution/` 或其他执行回执目录

常见做法是：

1. 由上游在 `ai/tasks/` 生成任务包
2. 在 `AGENTS.md` 里补充角色边界和协作约定
3. 由实施侧按任务包落地
4. 将 execution report 回写到 `ai/execution/`

## 推荐接入方式

在真实项目里，建议把这个 skill 当成“最小 handoff 适配层”使用，而不是替代项目文档体系。

推荐接入步骤：

1. 将本目录复制到目标项目的 `.codex/skills/chatgpt-handoff-pilot/`
2. 在项目已有协作文档里补一句：任务下发使用任务包，执行完成后回传 execution report
3. 先挑一个边界清晰、影响面小的任务试跑
4. 根据试跑结果，再决定是否增加脚本、自动检查或更细的模板

## 推荐配套文档

如果目标项目已有以下文档，建议优先配合使用：

- `AGENTS.md`：角色边界、工具规则、优先级
- `docs/HANDOFF.md`：交接背景、历史上下文、注意事项
- `docs/TASKBOARD.md` 或同类任务板：当前阶段任务来源
- `docs/current_architecture.md`、`docs/target_architecture.md`：涉及重构或迁移时的边界参照

## 推荐目录放置方式

为了降低接入成本，建议只约定“类型”，不强绑固定文件名：

- 任务包：放在 `ai/tasks/`、`docs/tasks/` 或项目已有任务目录
- execution report：放在 `ai/execution/`、`docs/execution/` 或与任务包并列的回执目录
- 模板：保留在 skill 自身目录中，供复制和引用

如果项目已经有成熟目录结构，应优先沿用项目本地目录。

## 最小 Workflow 示例

下面是一种最小试跑方式：

1. ChatGPT 或上游负责人基于 `templates/TASK_PACKAGE_TEMPLATE.md` 写一份任务包
2. 实施侧先用两三句话总结理解、边界和计划修改范围
3. 实施侧只在授权范围内落地
4. 完成后基于 `templates/EXECUTION_REPORT_TEMPLATE.md` 输出回执
5. 上游根据回执决定是验收、补任务，还是进入下一轮 handoff

## 当前刻意不做的内容

- 不提供脚本
- 不提供自动化生成器
- 不绑定固定文件名
- 不假设任何具体业务项目结构

## 为什么保持这么小

因为 handoff 协作是否顺畅，往往要到真实项目里才能验证。先保留最小母版，可以减少误设计，后续再根据试跑结果补充模板、示例或自动化。

本轮增强只补最小模板、示例和开发备注，目标是让真实项目能开始做输入输出流测试，而不是把 skill 做成复杂框架。
