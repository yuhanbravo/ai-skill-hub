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
- `ai/tasks/`
- `ai/execution/`

常见做法是：

1. 由上游在 `ai/tasks/` 生成任务包
2. 在 `AGENTS.md` 里补充角色边界和协作约定
3. 由实施侧按任务包落地
4. 将 execution report 回写到 `ai/execution/`

## 当前刻意不做的内容

- 不提供脚本
- 不提供自动化生成器
- 不绑定固定文件名
- 不假设任何具体业务项目结构

## 为什么保持这么小

因为 handoff 协作是否顺畅，往往要到真实项目里才能验证。先保留最小母版，可以减少误设计，后续再根据试跑结果补充模板、示例或自动化。
