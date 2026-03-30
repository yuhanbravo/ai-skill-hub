# ChatGPT Handoff Pilot

## What is this

`chatgpt-handoff-pilot` 是一个最小可用的 handoff 母版，用来建立“上游产出任务包，下游按边界实施，并在完成后回传 execution report”的协作基线。

当它被用于项目 handoff 文档时，默认策略是把内容收口到 `docs/HANDOFF.md`，并按 V2 规则持续维护：

- 如果 `docs/HANDOFF.md` 已存在，默认做 section-aware 增量更新
- 如果 `docs/HANDOFF.md` 不存在，默认创建该文件
- 默认维护 `## Update Log`
- 默认不再生成新的 `minimal_handoff_manual.md`

## When to use

适合在已经明确分离“方案制定”和“实施落地”，并且希望每轮执行都保留清晰边界与回执时使用；如果项目已有 `AGENTS.md`、`docs/HANDOFF.md` 或 `ai/tasks/` 等本地机制，这个 skill 应作为轻量壳层接入，并优先服从本地规则。

## Quick Start

```text
Use the `chatgpt-handoff-pilot` skill to generate a task package, execute within scope, and return an execution report.

# For project handoff docs (V2):
# - update docs/HANDOFF.md incrementally if it exists
# - merge by section instead of rewriting the whole file
# - append an Update Log entry
# - do not generate minimal_handoff_manual.md by default
```

详细模板见 [SKILL.md](SKILL.md)。
