# ChatGPT Handoff Pilot

## What is this

`chatgpt-handoff-pilot` 是一个最小可用的 handoff 母版，用来建立“上游产出任务包，下游按边界实施，并在完成后回传 execution report”的协作基线。

## When to use

适合在已经明确分离“方案制定”和“实施落地”，并且希望每轮执行都保留清晰边界与回执时使用；如果项目已有 `AGENTS.md`、`docs/HANDOFF.md` 或 `ai/tasks/` 等本地机制，这个 skill 应作为轻量壳层接入。

## Quick Start

```text
Use the `chatgpt-handoff-pilot` skill to generate a task package, execute within scope, and return an execution report.

# optional
# Follow project-local handoff rules first if they already exist
```

详细模板见 [SKILL.md](/d:/dev/codex-skill-hub/skills/chatgpt-handoff-pilot/SKILL.md)。
