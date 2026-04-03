# Skill Hub Status

- Updated at: `2026-04-03`
- Scope: `ai-skill-hub`
- Method: `system-status-update` wrapper over `update-project-status`
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, working tree, `skills/`, distribution surfaces, governance assets, `tools/`, `tests/`

## Current Status

`ai-skill-hub` 当前处于 `Phase 3 - Controlled System`：它已经不再只是 skill 集合，而是一个具备 canonical source、distribution surfaces、局部治理能力、显式文档分层、bridge 引用边界可见性和可重复工具链的 capability system。

- Overall maturity: `evolving`
- Stable core: canonical skill layer 已形成稳定事实源
- Main direction: 从“可发现、可调用”继续推进到“可分发、可校验、可控漂移、可标准化系统调用与文档分层治理”的系统阶段

## Layer Status

### Canonical Skill Layer (`skills/`)

- Status: `stable`
- Current shape: canonical source 维持在 `10` 个正式 skill 上，覆盖 `template / audit / project / governance / system` 五类能力，并补齐了 system-level status 与 handoff wrapper 入口；同时 `SKILL.md` 已进一步收口为 execution-focused contract，由 `README / prompts / examples / templates` 分担说明与交换资产。
- Maturity judgment: canonical layer 继续保持单一事实源；新引入的 `system-status-update` 与 `system-handoff` 通过 wrapper 方式复用 canonical skill，没有制造第二套实现或新的 source-of-truth 歧义；skill 文档职责边界也比上一阶段更清晰。

### Distribution Layer (`.codex / .agents / .github`)

- Status: `evolving`
- Current shape: hub 内 discovery layer 已覆盖新的 system wrapper skills，项目侧 distribution 继续以 `.codex/skills` 为内容落点、`.agents/.github` 为 project-local adapter surfaces，并新增了 `Targets` 选择以控制 rollout scope。
- Maturity judgment: distribution 已从“能下发 skill 内容”推进到“下发后仍保持 multi-AI discoverability 且可选择 rollout layer”的阶段；但这一层仍主要依赖本地工具与脚本执行，不属于强约束治理。

### Governance Layer (consistency checker)

- Status: `evolving`
- Current shape: governance 已从“结构约定 + 人工观察”推进到“脚本辅助漂移检测 + 关键回归覆盖 + 文档层角色冻结”，能够对 `.codex/skills`、`.agents/skills`、`.github/skills` 三层关系做只读一致性检查，并锁定 DryRun 无副作用、adapter 引用正确性、re-seed 前目标分类，以及 `AI / Human / Bridge` 三层文档中的 active-source 与 mirror 关系；本轮进一步把 repository-governance 文档收口到 `docs/governance/`，完成 `COMMIT_CONVENTION.md` 的 canonical 路径迁移，并在 `skill-governance` 下落地同一套 commit message 校验规则资产；当前 bridge-layer 路径引用已经完成从局部审计到全仓审计的收口，未发现 markdown、脚本或配置对 bridge mirror 路径的运行时消费。
- Maturity judgment: 当前治理能力已经能发现 missing adapter、orphan adapter、wrong reference，以及“哪些项目适合进入 clean re-seed 流程”这一类 rollout 前问题；当前还具备了 repository-local commit message 校验能力，并把 commit policy、validator 规则资产和 regression coverage 收口到同一治理面；但这部分能力仍属于本地脚本、hook 安装与文档约束辅助，不是 CI 级 enforcement。

### Tooling Layer (sync / tools)

- Status: `evolving`
- Current shape: tooling 已覆盖 canonical sync、project-local adapter emit、metadata build、router、pipeline、本地 governance check，以及 `sync_skills_to_nongit_project.ps1` 的 target-scoped rollout 与无副作用 DryRun contract；同时新增了 `audit_reseed_targets.ps1`，把 clean re-seed 前的批量预审计收口为独立只读工具，并能识别 hub repository 以避免把 `ai-skill-hub` 本体误当成普通消费项目；本地 commit 自动校验则通过版本化 `.githooks/commit-msg` 加 `tools/install_git_hooks.ps1` 启用，`export_bundle.ps1` 的 auto-commit 也已复用同一套 commit validator。
- Maturity judgment: 工具链已经能够把多 AI capability system 的维护工作从手工操作推进到可重复流程，并开始支持更可控的分发边界与 rollout 前分流判断；commit governance 这一层也已经具备统一校验入口，但新的 clone / worktree 仍需手动安装一次 hook，因此调度、发布和治理仍是“可用但非完全受控”的状态。

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
- Preflight audit capability: 系统现在具备独立的 re-seed 预审计工具，可批量判断项目是 `already_seeded`、`ready_for_reseed`、`risky_manual_review`、`missing_config`、`no_skill_structure`、`inaccessible` 还是 `hub_repository`。
- Hub boundary awareness: 工具层现在显式识别 `ai-skill-hub` 本体属于 hub repository，而不是普通 clean re-seed 目标，从而减少把系统仓库误送入 rollout 流程的风险。
- Documentation layering capability: 系统现在具备显式的 AI / Human / Bridge 三层文档架构，并通过总导航文档收口各层入口。
- Bridge continuity capability: handoff、status、skill index 与任务交换模板现在已经显式区分 active source 与 bridge-facing mirror/copy，降低了后续维护时的语义歧义。
- Bridge reference audit capability: 系统现在可以显式枚举 bridge-layer 路径引用面，并确认全仓范围内未发现脚本、配置或运行时对 bridge mirror 路径的激活依赖。
- Repository-wide bridge audit capability: 系统现在能够把 bridge 命中区分为直接路径引用、角色说明、mirror/ownership 声明和 compatibility/navigation 语句，并确认当前残留主要是语义层或自说明层，而不是需要立刻迁移的路径依赖。
- Protocol boundary capability: `EXECUTION_PROTOCOL`、`INVOCATION_PROTOCOL`、`DISCOVERY_AND_INVOCATION` 的职责边界与 `AI_USAGE` 的 compatibility 定位已经显式冻结，减少了 AI 规则面与入口面混写的风险。
- Commit governance capability: 系统现在已把 repository-governance 文档 canonical home 收口到 `docs/governance/`，并具备 `skill-governance` 规则资产、`.githooks/commit-msg` 本地自动校验入口，以及 `export_bundle.ps1` auto-commit 对同一 validator 的复用路径。

## Risks / Gaps

- Canonical layer 已稳定，但 distribution 和 governance 仍依赖本地执行路径，尚未形成仓库级强制校验。
- Routing 与 pipeline 仍具有启发式特征，系统整体还不是 fully deterministic orchestration stack。
- 当前 system wrapper 仍依赖显式调用；若退回普通项目模板或普通 handoff 口径，会削弱系统层表达能力。
- [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 仍存在编码异常，影响系统文档面的一致性。
- 在未提交阶段，working tree 对状态判断影响较大，意味着 status refresh 仍然部分依赖即时工作上下文，而不是纯 Git 历史。
- hub self-detection 目前刻意保持保守，只在强信号足够明确时才判为 `hub_repository`；这降低了误伤普通项目的概率，但也意味着未来可能存在“应识别但未识别”的漏判空间。
- bridge 层目前仍是“active source + mirror/copy”双份承载模型；虽然全仓审计已经确认没有 direct bridge-path dependency，但 mirror/copy 仍缺少自动同步或仓库级一致性检查来防止后续漂移。
- `AI_USAGE.md` 已切换到根目录 `SKILLS_INDEX.md` 作为 quick index；后续若继续收缩 bridge-facing copy，应保持兼容入口与 active source 一致，避免重新引入断链。
- 当前剩余的 bridge 相关命中主要分布在 `docs/bridge/` 自说明、状态/交接历史记录，以及 active-source vs mirror 的架构说明中；若要继续收缩，应通过后续正常刷新逐步改写，而不是一次性“清零 bridge 痕迹”。
- `docs/ai` 三份协议文档目前已经冻结职责边界，但其中仍有来自历史镜像和模板资产的延续性内容，后续若要继续收口，应先做引用面审计而不是直接路径切换。
- commit hook 不是天然随 clone / worktree 自动启用；新的 clone / worktree 仍需手动运行一次 `tools/install_git_hooks.ps1`。
- 当前 commit body 校验仍保持轻量描述性约束；是否继续收紧，应以后续真实使用反馈为准，而不是先行扩张规则面。

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
- 若后续进入更大规模 rollout，可继续迭代 re-seed 审计规则与报告格式，但应保持“先审计、再 DryRun、再分发”的只读前置模式，而不是把审计器扩展成执行器。
- 在不替换当前活跃路径的前提下，为 bridge mirror/copy 增加轻量一致性检查或维护清单，进一步降低文档双份承载的长期漂移风险。
- 若后续继续清理 bridge 兼容入口，优先保持 `AI_USAGE.md -> SKILLS_INDEX.md` 这类纯导航引用指向 active source，避免重新引入对 mirror 页的直接依赖。
- 若后续进入下一阶段文档治理，应继续把 bridge 命中区分为路径依赖、历史记录和层级语义，再决定是否收缩 mirror 或切换路径所有权，而不是直接把 bridge 层升级为新的活跃源。

## Notes

- 本次状态更新按 capability-system 视角组织，重点是 layer maturity 与 readiness，而不是普通项目的功能进度。
- 当前判断反映的是“最近 commit + 当前 working tree”的综合系统状态，而不是仅基于已提交历史生成的业务型周报。
- 本次刷新已吸收 bridge 引用面审计结果：当前活动文档中已不再保留对 bridge mirror 路径的直接依赖，且全仓范围内未发现脚本或配置级激活依赖。

