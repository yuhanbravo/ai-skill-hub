# SYSTEM_TAKEOVER_QUICK_COMMANDS

## 用途与适用范围

- 这是一份给 `ai-skill-hub` 人类维护者直接查阅、复制、粘贴的 `system-takeover` 速查页。
- 适用于 `capability system`、`skill-hub`、`multi-agent system`、`orchestration system` 这类 system-level takeover 场景。
- 它不是普通业务项目 onboarding 口令表，也不是 controller、CI enforcement、auto-fix 或自动重构工具说明。

## 使用原则

- 默认先把对象当作 capability system，而不是普通项目。
- 默认以 system-level analysis 为主，优先 read-only。
- 固定口令的重点是快速补一句“本轮目标 / focus layers / 约束”，不必每次重写完整方法论。
- 除非显式授权，通常不要把它写成会直接修改 `protocol`、`router`、`pipeline` 或已有 `skills`。

## system-takeover 的 3 档标准调用模板

### 极短版

```text
请用 `system-takeover` 重新接管当前 `ai-skill-hub`，做一轮 system-level analysis。
```

### 标准版

```text
请使用 `system-takeover` 重新接管当前 `ai-skill-hub`。

目标：
- 继续当前 capability system 开发前，先刷新整体系统判断

focus：
- `routing layer`
- `pipeline layer`
- `adapter layer`
- `tooling`

约束：
- 默认 read-only 优先
- 不把它当普通业务项目 onboarding
- 不修改 `protocol`、`router`、`pipeline` 或已有 `skills`

输出：
- `System Structure`
- `Capability Map`
- `Maturity Assessment`
- `Top Bottlenecks`
- `Evolution Plan`
```

### 复杂版

```text
请按 `system-takeover` 的方式对当前 capability system 做一轮严格分层接管分析。

对象：
- `ai-skill-hub`

范围：
- `skills/`
- `tools/`
- `docs/`
- `.agents/`
- `.github/`
- `tests/`

focus layers：
- `routing layer`
- `pipeline layer`
- `adapter layer`
- `governance`
- `tooling`

约束：
- 默认 read-only 分析
- 不把它写成普通项目 onboarding
- 不修改 `protocol`、`router`、`pipeline` 或已有 `skills`
- 明确区分已确认事实、推断、待验证项

输出要求：
- `System Structure`
- `Capability Map`
- `Maturity Assessment`
- `Top Bottlenecks`
- `Evolution Plan`
```

## 固定口令库（10 条高频一句话调用）

这组口令适合在 `skill-hub` / `capability system` 日常维护中快速补一句本轮目标、focus layers 或约束，然后直接进入 system-level takeover analysis。

- `请用 system-takeover 重新接管当前 ai-skill-hub，并给我一版最新的 system-level analysis。`
- `请用 system-takeover 接上我在办公室 / 家里切换前的上下文，重新判断当前 capability system 现在最该看哪几层。`
- `请用 system-takeover 只做 read-only 的 system analysis，不修改 protocol、router、pipeline 或已有 skills。`
- `请用 system-takeover 聚焦 routing layer 和 pipeline layer，判断当前 orchestration 相关瓶颈。`
- `请用 system-takeover 聚焦 adapter layer 和 governance，判断 current discoverability、drift 风险和治理边界。`
- `请用 system-takeover 聚焦 tooling、local validation 和 sync 相关能力，评估当前维护面是否够稳。`
- `请用 system-takeover 对当前 skill-hub 做一轮 system health check，并按层输出成熟度与主要风险。`
- `请用 system-takeover 判断下一步优先补哪一层：routing、pipeline、adapter、governance 还是 tooling。`
- `请用 system-takeover 输出 takeover analysis，并明确区分哪些是事实、哪些是推断、哪些还需要验证。`
- `请用 system-takeover 给当前 ai-skill-hub 做一轮正式的收工前 takeover analysis，输出 System Structure、Capability Map、Maturity Assessment、Top Bottlenecks、Evolution Plan。`

## 推荐默认口令（4 条）

```text
请用 `system-takeover` 重新接管当前 `ai-skill-hub`，做一轮 system-level analysis。
```

```text
请用 `system-takeover` 接上我在办公室 / 家里切换前的上下文，重新判断当前 capability system 最该先看哪几层。
```

```text
请用 `system-takeover` 聚焦 `routing layer`、`pipeline layer`、`adapter layer`，给我当前系统的主要瓶颈判断。
```

```text
请用 `system-takeover` 做一轮 read-only 的正式 takeover analysis，并明确区分事实、推断和待验证项。
```

## 最小调用骨架

```text
请使用 `system-takeover` 处理本次任务。

目标：
- <一句话目标>

focus layers：
- <1-3 个想重点看的层>

约束：
- 默认 read-only 优先
- 不修改 `protocol`、`router`、`pipeline` 或已有 `skills`

输出：
- `System Structure`
- `Capability Map`
- `Maturity Assessment`
- `Top Bottlenecks`
- `Evolution Plan`
```

默认一句话加少量 `focus layers` 就够用，不必每次写长提示词；但最好补一句这轮更想看哪一层，避免分析过泛。

## 什么时候从短版升级到复杂版

- 这次不是简单续接上下文，而是第一次接管新的 capability system。
- 你需要明确指定 `routing layer`、`pipeline layer`、`adapter layer`、`governance`、`tooling` 的 focus。
- 你需要它在输出里明确区分事实、推断和待验证项。
- 你准备把结果当作收工前或阶段性系统诊断结论来参考。

## 推荐维护方式

- 日常切换场景优先复制一条固定口令，再补一句 focus。
- 如果只是重新接上当前仓库，不必每次重写长说明。
- 如果这轮判断容易过泛，优先补 `routing / pipeline / adapter / governance / tooling` 中的 1 到 3 层。
- 需要正式结论时，再升级到复杂版或“收工前正式 takeover analysis”口令。

## 一句话心法

先点名 `system-takeover`，再补一句本轮想看哪几层，默认 read-only 优先，别把它写成普通项目 onboarding。
