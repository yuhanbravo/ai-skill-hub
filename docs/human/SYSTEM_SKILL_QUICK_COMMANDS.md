# SYSTEM_SKILL_QUICK_COMMANDS

## 用途与适用范围

- 这是一份给 `ai-skill-hub` 人类维护者直接查阅、复制、粘贴的 system skill 快速口令表。
- 只覆盖 `system-status-update` 和 `system-handoff` 两类常用调用。
- 这是一页 human docs 速查页，不负责定义新的协议、治理机制或 system 边界。

## 使用原则

### 短提示词优先

- 能用一句话说清，就先用一句话。
- 先点名 skill，再补最少必要事实，通常比长篇背景更稳。

### 只补本轮事实增量

- 优先只写这轮新增事实，不重复整份仓库背景。
- 当前高频事实增量通常就是这三类：
  - explicit `system-takeover` 路由补强已落地
  - `check_adapter_consistency.py` 已增加 `hub|consumer` mode
  - `tools/run_local_checks.ps1` 已成为默认本地验证入口

### 长提示词只在复杂轮次使用

- 只有在事实分散、边界容易写重、需要指定 section 或输出形状时，再升级到复杂版。

固定边界句建议原样保留：

- `router` 仍是 heuristic
- governance 仍是 read-only
- local validation 仍不是 CI enforcement

## system-status-update：3 档调用模板

### 极短版

```text
请用 `system-status-update` 刷新 `ai-skill-hub` 的 system status，只输出 `Layer Status`、`Current Phase`、`Capabilities`、`Stability`。
```

### 标准版

```text
请使用 `system-status-update` 处理这次 `ai-skill-hub` status 更新。

只补本轮事实增量：
- explicit `system-takeover` 路由补强已落地
- `check_adapter_consistency.py` 已增加 `hub|consumer` mode
- `tools/run_local_checks.ps1` 已成为默认本地验证入口

保留边界：
- `router` 仍是 heuristic
- governance 仍是 read-only
- local validation 仍不是 CI enforcement

输出：
- `Layer Status`
- `Current Phase`
- `Capabilities`
- `Stability`
```

### 复杂版

```text
请按 `system-status-update` 的方式刷新 `ai-skill-hub` 的 system status。

范围：
- `skills/`
- `.agents/`
- `.github/`
- `tools/`
- `docs/status/skill-hub-status.md`
- `docs/HANDOFF.md`

本轮事实增量：
- 显式点名 `system-takeover` 时，router 已补强为优先命中对应 system wrapper
- `tools/check_adapter_consistency.py` 现在显式区分 `--mode hub` 与 `--mode consumer`
- `tools/run_local_checks.ps1` 现在是默认本地验证入口

硬边界：
- `router` 仍是 heuristic，不是 controller
- governance 仍是 read-only，不是 auto-fix
- local validation 仍不是 CI enforcement
- 沿用现有 phase 表达，不新增 phase 叙事

输出要求：
- 只按 `Layer Status` / `Current Phase` / `Capabilities` / `Stability` 组织
- 不输出文件级改动清单
- 若有判断仍属推断，请明确标出
```

## system-handoff：3 档调用模板

### 极短版

```text
请用 `system-handoff` 增量更新 `docs/HANDOFF.md`，只做 section-aware merge，不全文重写。
```

### 标准版

```text
请使用 `system-handoff` 更新 `ai-skill-hub` 的 `docs/HANDOFF.md`。

只补本轮事实增量：
- explicit `system-takeover` 路由补强已落地
- `check_adapter_consistency.py` 已增加 `hub|consumer` mode
- `tools/run_local_checks.ps1` 已成为默认本地验证入口

保留边界：
- `router` 仍是 heuristic
- governance 仍是 read-only
- local validation 仍不是 CI enforcement

要求：
- 只做 section-aware merge
- 不全文重写
- `Next Phase Direction` 只写方向，不写任务清单
```

### 复杂版

```text
请按 `system-handoff` 的方式更新 `docs/HANDOFF.md`。

本轮只合并这些新增事实：
- 显式点名 `system-takeover` 时，router 已补强为优先命中对应 system wrapper
- `tools/check_adapter_consistency.py` 现在显式区分 `hub|consumer` 两种治理检查口径
- `tools/run_local_checks.ps1` 现在是默认本地验证入口

更新要求：
- 只增量更新相关 section
- 保持 `Hard Boundaries`、`Key Design Decisions`、`Intentional Gaps` 现有边界不变形
- `router` 仍是 heuristic，不写成 controller
- governance 仍是 read-only，不写成 enforcement 或 auto-fix
- local validation 仍不是 CI enforcement
- `Next Phase Direction` 只保留方向级表达，不新增 phase 叙事或任务清单

回执要求：
- 说明更新了哪些 section
- 说明哪些 hard boundaries 保持不变
```

## 固定口令库（10 条高频一句话调用）

- `请用 system-status-update 刷新 ai-skill-hub 的 system status，只输出 layer / phase / capabilities / stability。`
- `请用 system-status-update 刷新 status，并补上 explicit system-takeover 路由补强这条事实。`
- `请用 system-status-update 刷新 status，并补上 check_adapter_consistency.py 已增加 hub|consumer mode 这条事实。`
- `请用 system-status-update 刷新 status，并补上 run_local_checks.ps1 已成为默认本地验证入口这条事实。`
- `请用 system-status-update 刷新 status，只补三条增量事实，同时保留 router 仍是 heuristic、governance 仍是 read-only、local validation 仍不是 CI enforcement。`
- `请用 system-handoff 增量更新 docs/HANDOFF.md，只做 section-aware merge，不全文重写。`
- `请用 system-handoff 把 explicit system-takeover 路由补强这条事实并入 docs/HANDOFF.md。`
- `请用 system-handoff 把 check_adapter_consistency.py 的 hub|consumer mode 并入 docs/HANDOFF.md，并保持 governance 仍是 read-only。`
- `请用 system-handoff 把 run_local_checks.ps1 成为默认本地验证入口这条事实并入 docs/HANDOFF.md，并保留 local validation 仍不是 CI enforcement。`
- `请用 system-handoff 合并三条增量事实，保持 router 仍是 heuristic、governance 仍是 read-only、local validation 仍不是 CI enforcement，且不要全文重写。`

## 推荐默认口令（4 条）

```text
请使用 `system-status-update` 处理这次 `ai-skill-hub` status 更新，只补本轮事实增量，并保留 `router` 仍是 heuristic、governance 仍是 read-only、local validation 仍不是 CI enforcement。
```

```text
请使用 `system-status-update` 刷新 `ai-skill-hub` 的 system status，并补上 explicit `system-takeover` 路由补强、`check_adapter_consistency.py` 的 `hub|consumer` mode、`tools/run_local_checks.ps1` 默认本地验证入口这三条事实。
```

```text
请使用 `system-handoff` 更新 `docs/HANDOFF.md`，只做 section-aware merge，只补本轮事实增量，不全文重写。
```

```text
请使用 `system-handoff` 合并三条新增事实：explicit `system-takeover` 路由补强、`check_adapter_consistency.py` 增加 `hub|consumer` mode、`tools/run_local_checks.ps1` 成为默认本地验证入口，并保持现有边界表达不变形。
```

## 最小调用骨架

### status 更新骨架

```text
请使用 `system-status-update` 处理本次任务。

目标：
- <一句话目标>

只补本轮事实增量：
- <事实 1>
- <事实 2>

保留边界：
- `router` 仍是 heuristic
- governance 仍是 read-only
- local validation 仍不是 CI enforcement

输出：
- `Layer Status`
- `Current Phase`
- `Capabilities`
- `Stability`
```

### handoff 更新骨架

```text
请使用 `system-handoff` 处理本次任务。

目标：
- <一句话目标>

只补本轮事实增量：
- <事实 1>
- <事实 2>

保留边界：
- `router` 仍是 heuristic
- governance 仍是 read-only
- local validation 仍不是 CI enforcement

要求：
- 只做 section-aware merge
- 不全文重写 `docs/HANDOFF.md`
- `Next Phase Direction` 只写方向，不写任务清单
```

## 什么时候从短版升级到复杂版

- 本轮新增事实不止一条，而且分散在 `README.md`、`docs/status/skill-hub-status.md`、`docs/HANDOFF.md` 等多个位置。
- 你需要明确指定哪些 section 可以更新，哪些边界必须原样保留。
- 你担心 AI 把 `router` 写成 controller，或把 governance / local validation 写重。
- 你需要它在回执里说明“更新了什么”与“哪些边界没变”。

## 推荐维护方式

- 日常轮次先复制“推荐默认口令”，不够再升级到复杂版。
- 每次只补本轮新增事实，避免把旧背景整段重复贴进去。
- 如果事实已经很清楚，优先用一句话口令，不必先写成长说明。
- 需要本地自检时，优先把 `tools/run_local_checks.ps1` 当默认入口使用，但不要把它表述成 CI enforcement。

## 一句话心法

先点名 skill，再补本轮事实增量，边界三句尽量原样保留，复杂版只留给复杂轮次。
