# ChatGPT Handoff Pilot

## What is this

`chatgpt-handoff-pilot` 是一个最小可用的 handoff 母版，用来建立“上游产出任务包，下游按边界实施，并在完成后回传 execution report”的协作基线。

它适合拿到真实项目里先试跑，验证交接输入、实施边界和执行回执是否足够稳定，而不是直接引入复杂流程或自动化框架。

## When to use

适合你已经明确要分离“方案制定”和“实施落地”，并且希望每轮执行都保留清晰边界与回执的场景。尤其适合 ChatGPT 负责方案，Codex / Copilot 负责施工的 handoff 流程。

如果项目已经有 `AGENTS.md`、`docs/HANDOFF.md`、任务板文档或 `ai/tasks/` 一类目录，这个 skill 最适合作为轻量壳层接入，而不是替代本地规则。

## Quick Start

1. 将本目录复制到目标项目的 `.codex/skills/chatgpt-handoff-pilot/`
2. 用 `templates/TASK_PACKAGE_TEMPLATE.md` 或 [SKILL.md](/d:/dev/codex-skill-hub/skills/chatgpt-handoff-pilot/SKILL.md) 中的 prompt 生成任务包
3. 让实施侧先复述目标、边界、修改范围和不做事项
4. 完成后用 `templates/EXECUTION_REPORT_TEMPLATE.md` 或 `SKILL.md` 中的模板输出回执

建议先挑一个边界清晰、影响面小的任务试跑，再决定是否在目标项目中增加更细的模板、检查或脚本。
