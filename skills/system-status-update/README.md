# System Status Update

## What is this

`system-status-update` 是一个面向 `ai-skill-hub` 本体的 system-level wrapper skill，用来把状态更新收口为 layer / phase / capability / stability 口径，而不是普通项目状态摘要。

它复用 canonical skill `update-project-status` 的状态采集与写入能力，但把目标对象固定为 `skill-hub as system`，并把输出约束为系统层表达。

这是一个 system-level wrapper skill，不分叉 canonical logic，不引入 orchestration、controller 或 auto-fix，只增加 system-level output constraints。

## When to use

- 需要刷新 `ai-skill-hub` 的系统状态，而不是业务项目周报
- 需要按 `Canonical / Distribution / Governance / Tooling` 四层表达现状
- 需要输出当前 phase、capabilities 和 stability，而不是文件变更清单

## Quick Start

```text
Use `system-status-update` for this task.

System root:
- <project-root>

Expected output:
- Layer Status
- Current Phase
- Capabilities
- Stability
```

## Relation To Canonical Skill

- Canonical dependency: `update-project-status`
- Canonical skill path: `skills/update-project-status/`
- This wrapper reuses the canonical skill instead of replacing or forking it.
- It narrows the target to `ai-skill-hub` itself and only adds system-oriented output constraints.

详细执行约束见 [SKILL.md](SKILL.md)。
