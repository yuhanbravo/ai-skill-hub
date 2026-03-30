# Skill Hub Status

- Updated at: `2026-03-30`
- Scope: `ai-skill-hub`
- Method: `update-project-status` system-level status refresh
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, distribution surfaces, governance assets, `tools/`, `tests/`

## Current Status

`ai-skill-hub` 当前处于 `Phase 3 - Controlled System`：它已经不再只是 skill 集合，而是一个具备 canonical source、distribution surfaces、局部治理能力和可重复工具链的 capability system。

- Overall maturity: `evolving`
- Stable core: canonical skill layer 已形成稳定事实源
- Main direction: 从“可发现、可调用”继续推进到“可分发、可校验、可控漂移”的系统阶段

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- Current shape: canonical source 维持在 `8` 个正式 skill 上，覆盖 `template / audit / project / governance / system` 五类能力。
- Maturity judgment: canonical layer 已具备稳定的 skill 定义主轴、统一调用契约和可持续扩展边界，本轮没有引入新的 source-of-truth 歧义。

### Distribution Layer (`.codex / .agents / .github`)

- Status: `evolving`
- Current shape: hub 内 discovery layer 已完整存在，项目侧 distribution 也已形成 `.codex/skills` 为内容落点、`.agents/.github` 为 project-local adapter surfaces 的闭环。
- Maturity judgment: distribution 不再停留在“能下发 skill 内容”，而是进入“下发后仍保持 multi-AI discoverability”的阶段；但这一层仍主要依赖本地工具与脚本执行，不属于强约束治理。

### Governance Layer (consistency checker)

- Status: `evolving`
- Current shape: governance 已从“结构约定 + 人工观察”推进到“脚本辅助漂移检测”，能够对 `.codex/skills`、`.agents/skills`、`.github/skills` 三层关系做只读一致性检查。
- Maturity judgment: 当前治理能力已经能发现 missing adapter、orphan adapter 和 wrong reference，但仍属于本地脚本辅助，不是 CI 级 enforcement。

### Tooling Layer (sync / tools)

- Status: `evolving`
- Current shape: tooling 已覆盖 canonical sync、project-local adapter emit、metadata build、router、pipeline 和本地 governance check。
- Maturity judgment: 工具链已经能够把多 AI capability system 的维护工作从手工操作推进到可重复流程，但调度、发布和治理仍是“可用但非完全受控”的状态。

## Phase Assessment

- Current phase: `Phase 3 - Controlled System`
- Phase meaning: 系统已经具备稳定 canonical layer、可用 distribution layer、脚本辅助 governance 和可重复 tooling，但还没有进入 CI-backed governance 或更强 orchestration 的下一阶段。
- Stability: `stable` for canonical definition, `evolving` for distribution and governance, `experimental-to-evolving` for heuristic routing behavior.

## New Capabilities In This Phase

- Distribution capability: 项目侧 skill distribution 已具备 project-local adapter surfaces，不再只停留在内容复制。
- Governance capability: 系统已具备 adapter drift detection，能够识别缺失、孤儿和错误引用三类一致性问题。
- Layer clarity: canonical source、distribution surfaces 和 governance check 三层职责更加清晰，系统边界比上一阶段更明确。
- Operational repeatability: 本地维护者或后续 AI agent 已可以用统一工具完成分发、发现层闭环和只读治理检查。

## Risks / Gaps

- Canonical layer 已稳定，但 distribution 和 governance 仍依赖本地执行路径，尚未形成仓库级强制校验。
- Routing 与 pipeline 仍具有启发式特征，系统整体还不是 fully deterministic orchestration stack。
- 当前状态生成仍需要 skill-hub 视角模板；若退回普通项目模板，会削弱系统层表达能力。
- [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 仍存在编码异常，影响系统文档面的一致性。
- 在未提交阶段，working tree 对状态判断影响较大，意味着 status refresh 仍然部分依赖即时工作上下文，而不是纯 Git 历史。

## Recommended Next Steps

- 把 governance checker 提升到仓库级例行验证流程，减少 distribution drift 的人工发现成本。
- 为 router 与 pipeline 补充更稳定的意图提示或别名层，降低启发式误选的系统风险。
- 持续保持 skill-hub 专用状态模板，确保后续 status refresh 继续按 system layer 而不是业务功能视角表达。
- 修复 [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 的编码问题，避免文档层拖累系统治理成熟度。

## Notes

- 本次状态更新按 capability-system 视角组织，重点是 layer maturity 与 readiness，而不是普通项目的功能进度。
- 当前判断反映的是“最近 commit + 当前 working tree”的综合系统状态，而不是仅基于已提交历史生成的业务型周报。
