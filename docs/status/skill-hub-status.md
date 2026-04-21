# Skill Hub Status

- Updated at: `2026-04-20`
- Scope: `ai-skill-hub`
- Method: `system-status-update` wrapper over `update-project-status`
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, `.agents/`, `.github/`, `tools/`, `docs/status/`

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- Canonical layer 仍然是唯一事实源，当前保持 `10` 个正式 skill、`template / audit / project / governance / system` 五类能力，以及 wrapper-only 的 system entrypoints。
- 本轮变化没有引入第二套 status 机制，而是继续增强 canonical `update-project-status`：它现在支持 `git / workspace / hybrid` 三种刷新模式、workspace signal 采集，以及面向 status artifact 的 SSOT-lite 角色表达。

### Distribution Layer (`.agents/` / `.github/` / bridge-facing continuity)

- Status: `evolving`
- Hub-side thin wrapper 与 GitHub fallback surface 仍保持可发现性，system wrappers 也继续通过 adapter 指回 canonical source，而不是复制完整实现。
- 最近的 bridge mirror refresh 说明 handoff/status 的 continuity surface 仍在维护，但 active ownership 依然留在 `docs/HANDOFF.md` 与 `docs/status/skill-hub-status.md`；这一层可用性是稳定的，自动一致性仍然不强。

### Governance Layer

- Status: `evolving`
- Governance 已不只是 adapter drift check；当前还具备 commit convention、hub-vs-consumer dual-mode adapter guidance，以及新增的 derivative-surface drift audit，能以只读方式审视 bridge / metadata 这类派生面是否发生语义漂移。
- 当前 working tree 还显示了一份 `documentation-governance` 与 `update-project-status` 的最小联动约定，说明文档角色边界正在继续收口，但它目前仍应视为 in-progress signal，而不是已强制落地的仓库规则。

### Tooling Layer (`tools/`)

- Status: `evolving`
- Tooling layer 现在覆盖 sync、router、pipeline、metadata generation、local checks、adapter consistency、re-seed audit、derivative-surface audit，以及面向 skill-hub 模板的 status refresh。
- 最近一轮强化主要体现在两点：`generate_skill_metadata.py` 对 example-file layout 的提取更稳，`update_project_status.py` 在 no-git / workspace-driven 场景下也能给出结构化 refresh，而不需要退回普通项目口径。

## Current Phase

- Current phase: `Phase 3 - Controlled System`
- Phase judgment: 当前系统已经具备稳定 canonical source、可用 distribution surfaces、read-only governance、repeatable tooling，以及 system-level wrapper entrypoints，但还没有进入 CI-backed enforcement 或 controller-style orchestration。
- Why unchanged: 最近增强的是 status engine 的适应性、metadata/tooling 的稳健性，以及 derivative/mirror 面的审计可见性；这些变化提升了系统韧性，但没有改变当前 phase 的边界定义。
- Main direction: 继续在不打破层边界的前提下，把本地可重复流程推进到更可信的跨层治理与更低漂移维护。

## Capabilities

- Layered capability system: canonical skills、distribution adapters、governance checks 与 tooling 仍保持清晰分层，没有重新混成单层仓库。
- Workspace-aware status refresh: `update-project-status` 现在可以基于 `git`、`workspace` 或 `hybrid` 信号刷新状态，并明确 `primary status doc`、snapshot 与 truth precedence 这类 SSOT-lite 角色。
- Derivative-surface auditing: 仓库现在能只读检查 bridge / metadata 这类派生面的语义漂移，而不把 mirror surface 提升为新的 active source。
- Invocation metadata resilience: invocation example extraction 已经适配 example-file layout，降低了 metadata build 与 discovery surface 因布局差异产生的抽取漂移。
- Bridge continuity: handoff/status 的 bridge-facing mirror 现在可以按语义刷新，并保持 active source 与 continuity copy 的边界明确。
- Local-first validation: 系统仍以本地入口和脚本化检查为主，但这些入口已经足够支持 status、metadata、adapter、mirror 等关键维护面上的重复执行。
- Wrapper coordination baseline: `system-status-update` 与 `system-handoff` 现在具备最小联动规则（14 天 freshness gate、status 先于 handoff、handoff phase consistency 检查），用于降低双文档口径漂移。

## Stability

- Overall maturity: `evolving`
- Stable: canonical ownership、wrapper-only system skills、active-source documentation ownership，以及 hub-vs-consumer contract separation。
- Evolving: distribution freshness、derivative-surface governance、workspace-aware status refresh ergonomics，以及 metadata/discovery robustness。
- Not yet stable: CI-backed enforcement、automatic mirror consistency、automatic governance-mode detection，以及 deterministic orchestration。
- Evidence boundary: 本次刷新先复用了 `update-project-status` 的 dry-run signal collection，再结合当前 working tree 判断系统状态；未提交的治理约定被当作 live signal 记录，但没有被表述成已落地保证。
- Freshness gate: `Updated at` 已通过 14 天时效门槛检查（当前年龄 0 天），本次无需新增 `Staleness` 风险项。
