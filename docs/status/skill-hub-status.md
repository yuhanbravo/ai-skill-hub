# Skill Hub Status

- Updated at: `2026-03-31`
- Scope: `ai-skill-hub`
- Method: `system-status-update` wrapper over `update-project-status`
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, distribution surfaces, governance assets, `tools/`, `tests/`

## Current Status

`ai-skill-hub` 当前处于 `Phase 3 - Controlled System`：它已经不再只是 skill 集合，而是一个具备 canonical source、distribution surfaces、局部治理能力和可重复工具链的 capability system。

- Overall maturity: `evolving`
- Stable core: canonical skill layer 已形成稳定事实源
- Main direction: 从“可发现、可调用”继续推进到“可分发、可校验、可控漂移、可标准化系统调用”的系统阶段

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- Current shape: canonical source 维持在 `10` 个正式 skill 上，覆盖 `template / audit / project / governance / system` 五类能力，并补齐了 system-level status 与 handoff wrapper 入口。
- Maturity judgment: canonical layer 继续保持单一事实源；新引入的 `system-status-update` 与 `system-handoff` 通过 wrapper 方式复用 canonical skill，没有制造第二套实现或新的 source-of-truth 歧义。

### Distribution Layer (`.codex / .agents / .github`)

- Status: `evolving`
- Current shape: hub 内 discovery layer 已覆盖新的 system wrapper skills，项目侧 distribution 继续以 `.codex/skills` 为内容落点、`.agents/.github` 为 project-local adapter surfaces，并新增了 `Targets` 选择以控制 rollout scope。
- Maturity judgment: distribution 已从“能下发 skill 内容”推进到“下发后仍保持 multi-AI discoverability 且可选择 rollout layer”的阶段；但这一层仍主要依赖本地工具与脚本执行，不属于强约束治理。

### Governance Layer (consistency checker)

- Status: `evolving`
- Current shape: governance 已从“结构约定 + 人工观察”推进到“脚本辅助漂移检测 + 关键回归覆盖”，能够对 `.codex/skills`、`.agents/skills`、`.github/skills` 三层关系做只读一致性检查，并锁定 DryRun 无副作用与 adapter 引用正确性。
- Maturity judgment: 当前治理能力已经能发现 missing adapter、orphan adapter 和 wrong reference，并能回归校验 DryRun 与 adapter contract；但仍属于本地脚本与测试辅助，不是 CI 级 enforcement。

### Tooling Layer (sync / tools)

- Status: `evolving`
- Current shape: tooling 已覆盖 canonical sync、project-local adapter emit、metadata build、router、pipeline、本地 governance check，以及 `sync_skills_to_nongit_project.ps1` 的 target-scoped rollout 与无副作用 DryRun contract。
- Maturity judgment: 工具链已经能够把多 AI capability system 的维护工作从手工操作推进到可重复流程，并开始支持更可控的分发边界；但调度、发布和治理仍是“可用但非完全受控”的状态。

## Phase Assessment

- Current phase: `Phase 3 - Controlled System`
- Phase meaning: 系统已经具备稳定 canonical layer、可用 distribution layer、脚本辅助 governance、可重复 tooling，以及面向系统操作的标准 wrapper 入口，但还没有进入 CI-backed governance 或更强 orchestration 的下一阶段。
- Stability: `stable` for canonical definition, `evolving` for distribution and governance, `evolving` for system-level invocation surfaces, `experimental-to-evolving` for heuristic routing behavior.

## New Capabilities In This Phase

- Distribution capability: 项目侧 skill distribution 已具备 project-local adapter surfaces，不再只停留在内容复制。
- Governance capability: 系统已具备 adapter drift detection，能够识别缺失、孤儿和错误引用三类一致性问题。
- Layer clarity: canonical source、distribution surfaces 和 governance check 三层职责更加清晰，系统边界比上一阶段更明确。
- Operational repeatability: 本地维护者或后续 AI agent 已可以用统一工具完成分发、发现层闭环和只读治理检查。
- System invocation capability: 系统现在具备 `system-status-update` 与 `system-handoff` 两个标准 wrapper 入口，用于把 status 与 handoff 收口到 system-layer 语义。
- Controlled rollout capability: 分发工具现在支持 target-scoped rollout，在保持默认行为不变的前提下控制 `codex / agents / github` 层级输出。

## Risks / Gaps

- Canonical layer 已稳定，但 distribution 和 governance 仍依赖本地执行路径，尚未形成仓库级强制校验。
- Routing 与 pipeline 仍具有启发式特征，系统整体还不是 fully deterministic orchestration stack。
- 当前 system wrapper 仍依赖显式调用；若退回普通项目模板或普通 handoff 口径，会削弱系统层表达能力。
- [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 仍存在编码异常，影响系统文档面的一致性。
- 在未提交阶段，working tree 对状态判断影响较大，意味着 status refresh 仍然部分依赖即时工作上下文，而不是纯 Git 历史。

## DryRun Contract Fix (sync_skills_to_nongit_project.ps1)

### Before

- DryRun 仍会进入部分分发路径，存在 adapter 写入和目标路径依赖风险。
- DryRun 语义不够严格，不能稳定保证“只预览不执行”。
- 在部分路径下，DryRun 的退出状态可能被非执行分支影响。

### What changed

- 引入统一 DryRun gate `$IsDryRun`，把副作用路径集中隔离。
- robocopy、adapter emit、version file 写入和 stale entry 删除在 DryRun 下只输出计划。
- DryRun 输出统一使用 `[PLAN]`，不再执行实际写入。
- DryRun 正常流程固定返回 exit code `0`。

### Now guarantees

- 不创建 `.codex`、`.agents`、`.github` 目标目录。
- 不写入任何 canonical 或 adapter 文件。
- 不修改已有 adapter / canonical 内容，也不依赖目标路径预先存在。
- 输出计划信息 `[PLAN]`，并保持 exit code = `0`。

### Test coverage

- 已添加回归测试：[tests/test_dryrun_no_side_effects.py](../../tests/test_dryrun_no_side_effects.py)。
- 覆盖空项目场景，以及已有 `.codex/skills` 与 adapter 层的场景。
- 验证范围：无副作用、目录与内容不变、exit code == `0`、stdout 包含 `[PLAN]`。

## Recommended Next Steps

- 把 governance checker 提升到仓库级例行验证流程，减少 distribution drift 的人工发现成本。
- 继续保持 `system-status-update` 与 `system-handoff` 的 wrapper 定位，避免把 system invocation surface 扩张成新的 controller framework。
- 为 router 与 pipeline 补充更稳定的意图提示或别名层，降低启发式误选的系统风险。
- 修复 [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 的编码问题，避免文档层拖累系统治理成熟度。

## Notes

- 本次状态更新按 capability-system 视角组织，重点是 layer maturity 与 readiness，而不是普通项目的功能进度。
- 当前判断反映的是“最近 commit + 当前 working tree”的综合系统状态，而不是仅基于已提交历史生成的业务型周报。
