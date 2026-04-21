---
name: system-status-update
description: "Use when refreshing ai-skill-hub as a capability system and the output must stay layer-oriented instead of file-oriented."
metadata:
   triggers:
      - refresh ai-skill-hub system status
      - update skill-hub layer status and phase
      - generate a capability-system status summary
      - produce layer-oriented status for ai-skill-hub
      - summarize canonical distribution governance and tooling layers
   side_effects:
      - read_only
      - write_files
      - requires_git
---
# System Status Update

This execution-focused skill definition keeps the behavior, invocation shape, and adapter-facing contract unchanged while moving explanation-oriented content into supporting assets.

## Supporting Assets

- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)

## 4. 核心模式（Pattern）

### System Layer Status Refresh Pattern（系统分层状态刷新模式）

这个 pattern 的核心是：

- 复用 `update-project-status` 收集近期系统信号
- 把信号映射到 system layers，而不是文件列表
- 用 phase、capabilities 和 stability 组织状态输出

Input:
- `ai-skill-hub` 根目录
- Git history 与 working tree 信号
- `skills/`、`.agents/`、`.github/`、`tools/`、`docs/status/`

Process:
- `scan`
- `understand`
- `structure`
- `output`

Output:
- `Layer Status`
- `Current Phase`
- `Capabilities`
- `Stability`

这样组织的原因是，system status 的价值在于说明系统边界和成熟度，而不是把最近提交翻译成文件级流水账。底层刷新能力继续由 canonical skill `update-project-status` 提供，这个 wrapper 只负责 system-oriented 收口。

## 5. 核心原则（Principles）

- 先复用 canonical status engine，再收口到 system output。  
  Reuse the canonical status engine before adding system-level framing.

- 输出必须按层表达，而不是按文件表达。  
  Express status by layers, not by files.

- phase、capabilities 和 stability 是主口径。  
  Make phase, capabilities, and stability the primary vocabulary.

- 不把 system status 退化成项目日报。  
  Do not degrade system status into a project activity report.

- 写入动作仍保持最小化。  
  Keep writes minimal and scoped to system status artifacts.

## 6. 执行流程（Execution Steps）

1. 读取 system context。  
   先把目标对象确认为 `ai-skill-hub` 自身，并读取 `docs/status/skill-hub-status.md`、`README.md`、`skills/`、distribution surfaces 和 tooling 入口。

2. 调用 canonical status logic。  
   复用 `update-project-status` 的 `scan -> understand -> structure -> output` 方法收集 Git、working tree 和系统资产信号，但不要沿用普通项目视角输出。

3. 建立 layer mapping。  
   把近期变化映射到 `Canonical Skill Layer`、`Distribution Layer`、`Governance Layer`、`Tooling Layer` 四层，并判断 phase 与 stability。

4. 组织 system-oriented output。  
   输出必须至少包含 `Layer Status`、`Current Phase`、`Capabilities`、`Stability`；若需要写入状态文档，也应按这个结构落盘。

5. 执行 freshness gate（时效门槛检查）。  
   读取状态文档中的 `Updated at` 时间；若距离当前日期超过 `14` 天，必须在输出中显式增加 `Staleness` 提示，并把该项写入 `Risks / Gaps`。若在门槛内，也应说明本次刷新已满足时效门槛。

6. 回传风险与未确认项。  
   若证据不足，应明确说明哪些判断来自代码与文档证据，哪些仍需后续验证，避免把推断写成确定事实。

7. 处理与 system-handoff 的联动。  
   若本轮还要更新 `docs/HANDOFF.md`，应先完成 status 刷新，再把 `Current Phase` 和关键边界提供给 `system-handoff`；handoff 落盘前必须通过 phase consistency 检查。

## 7. 约束（Constraints）

- 必须复用 `update-project-status` 作为 canonical dependency，不得复制出第二套状态刷新逻辑
- 这是一个 system-level wrapper skill，只复用 canonical skill，不得分叉 canonical logic
- 不得引入 orchestration、controller、auto-fix 或其他新的 system framework 机制
- 当前 wrapper 只允许增加 system-level output constraints，不允许扩展底层状态能力
- 主输出不得列文件修改、函数实现细节或逐项施工记录
- 不得发明新的 phase 体系，必须沿用仓库已有 system-phase 语义
- 不得把 layer status 退化为代码清单或提交列表
- 除状态文档本身外，不应顺带修改其他系统资产
- 若检测到状态文档超过 `14` 天未刷新，主输出必须显式包含 `Staleness` 提示
- 若与 `system-handoff` 联动执行，必须先更新 status，再校验 handoff phase 一致性

## Invocation

### When to use

- 当你需要刷新 `ai-skill-hub` 自身的状态，并强制输出 layer / phase / capability / stability 结构时使用。


### Supporting assets
- Human-oriented context: [README.md](README.md)
- Reusable prompts: [prompts/reusable_prompts.md](prompts/reusable_prompts.md)
- Invocation examples: [examples/invocation_examples.md](examples/invocation_examples.md)
