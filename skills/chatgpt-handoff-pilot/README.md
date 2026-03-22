# ChatGPT Handoff Pilot

## What is this

`chatgpt-handoff-pilot` 是一个最小可用的 handoff skill 母版，用来验证这种协作模式是否适合真实项目：

- ChatGPT 负责架构、方案拆解、约束说明、审稿
- Codex 或 Copilot 负责按任务包实施并输出 execution report

它的目标是先把最小协作框架写清楚，方便复制到真实项目中试跑，而不是在当前仓库里做复杂封装。

## When to use

适合以下场景：

- 希望把“方案制定”和“代码落地”分开
- 希望上游先给出任务包，再由实施侧严格按范围执行
- 希望每轮执行后都有标准化 execution report
- 希望先小范围试跑，再逐步补充脚本、检查或更细模板

推荐配合以下内容一起使用：

- `AGENTS.md`
- `docs/HANDOFF.md`、`docs/TASKBOARD.md` 或类似任务来源文档
- `ai/tasks/` 或其他任务包目录
- `ai/execution/` 或其他执行回执目录

## Quick Start

推荐接入步骤：

1. 将本目录复制到目标项目的 `.codex/skills/chatgpt-handoff-pilot/`
2. 在项目已有协作文档里补充“任务下发使用任务包，执行完成后回传 execution report”
3. 先挑一个边界清晰、影响面小的任务试跑
4. 根据试跑结果，再决定是否增加脚本、自动检查或更细模板

最小 workflow：

1. 上游基于 `templates/TASK_PACKAGE_TEMPLATE.md` 生成任务包
2. 实施侧先复述目标、边界和修改范围
3. 实施侧只在授权范围内落地
4. 完成后基于 `templates/EXECUTION_REPORT_TEMPLATE.md` 输出回执

可直接使用的提示词模板见 [SKILL.md](/d:/dev/codex-skill-hub/skills/chatgpt-handoff-pilot/SKILL.md)。
