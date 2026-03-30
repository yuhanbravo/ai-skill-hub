# Skill Hub Status

- Updated at: `2026-03-29 23:10:00`
- Scope: `ai-skill-hub`
- Method: `update-project-status` dry-run analysis + working tree review
- Config: `.codex/skill-config/update-project-status.json`
- Data sources: Git history, unstaged changes, `skills/`, `docs/`, `tools/`, `tests/`

## Current Status

`ai-skill-hub` 当前已经从“技能仓库存放区”推进到“可治理、可发现、可调用、可编排的 skill engineering 项目”。

- Skill coverage: `7/7` canonical skills 已标准化到 `README.md + SKILL.md + metadata` 主轴，且覆盖 `template / audit / project / governance` 四类能力。
- Adapter coverage: `7/7` canonical skills 已具备 `.agents/skills/` 与 `.github/skills/` 入口，跨 AI 发现层已成形。
- Invocation readiness: 已具备统一调用协议、每个 skill 的 `Invocation` section、`skills_index.json`、flat adapter summaries，以及基础自动路由与 pipeline 编排工具。
- Governance readiness: 已具备 skill 模板、结构校验、索引生成和主索引文档，但尚未进入 CI 级别的漂移防护。
- Automation readiness: 已具备 metadata generator、skill router、skill pipeline、结构测试和路由测试，但调度策略仍是启发式实现。

## Recent Progress

本轮迭代的推进重点，不是单个 skill 内容扩展，而是 skill-hub 的整体工程化能力提升。

- 完成 canonical skill frontmatter 统一，形成 `name + description + metadata.triggers + metadata.side_effects` 的稳定基线。
- 为全部 canonical skills 补齐 `Invocation` section，并引入统一调用协议，降低“可见但不可调用”的落差。
- 增加 `.agents/skills/`、`.github/skills/`、`AI_USAGE.md`、`SKILLS_INDEX.md` 和 `skills_index.json`，把多 AI 兼容层从隐式约定变成显式结构。
- 增加 `tools/generate_skill_metadata.py` 与 `tests/test_skill_structure.py`，把元数据生成和结构验证纳入自动化。
- 完成 Phase 3 的轻量调度能力，新增 `tools/skill_router.py`、`tools/skill_pipeline.py` 和 `tests/test_skill_router.py`，支持单 skill 自动选择与多 skill 顺序编排。

## Key Changes

### 1. Skill structure standardization

- [README.md](../../README.md) 已明确 `skills/` 为唯一事实源，并补充 adapter layer 说明。
- [skills/SKILL_TEMPLATE.md](../../skills/SKILL_TEMPLATE.md) 现在定义了 metadata 与 Invocation 模板。
- `7` 个 canonical `SKILL.md` 已全部具备统一 frontmatter 与调用示例。

### 2. Multi-AI compatibility layer

- `.agents/skills/<skill>/SKILL.md` 提供目录型发现入口。
- `.agents/skills/<skill>.md` 提供 flat discovery 入口。
- `.github/skills/<skill>.md` 提供 Copilot fallback 入口。
- [AI_USAGE.md](../../AI_USAGE.md) 和 [SKILLS_INDEX.md](../../SKILLS_INDEX.md) 负责统一解释层。

### 3. Invocation and metadata readiness

- [skills/_protocol/skill_invocation.md](../../skills/_protocol/skill_invocation.md) 定义统一输入输出契约。
- [skills_index.json](../../skills_index.json) 已成为轻量运行时索引。
- `metadata.triggers` 与 `metadata.side_effects` 已可被索引器、路由器和下游 AI 工具消费。

### 4. Tests and automation

- [tools/generate_skill_metadata.py](../../tools/generate_skill_metadata.py) 负责生成机器可读索引和 flat adapter summaries。
- [tests/test_skill_structure.py](../../tests/test_skill_structure.py) 覆盖 canonical skill 结构完整性。
- [tools/skill_router.py](../../tools/skill_router.py) 与 [tools/skill_pipeline.py](../../tools/skill_pipeline.py) 提供 Phase 3 的调度层。
- [tests/test_skill_router.py](../../tests/test_skill_router.py) 已验证英文路由、中文复合任务和 pipeline 编排。

## Risks / Gaps

- 调度仍基于 trigger 和关键词启发式，中文短句与模糊任务仍存在误选风险。
- 当前 `update-project-status` 自带脚本模板仍偏普通项目视角，不能直接表达 skill coverage、adapter coverage 和 governance readiness，需要 repo-specific config 或自定义状态模板。
- 结构验证与 metadata 生成尚未接入 CI，adapter 层和 canonical 层仍存在后续漂移的可能。
- [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 当前存在明显编码异常，已偏离可持续文档状态。
- Git 历史未完全反映本轮工作重点，当前状态判断高度依赖 working tree；在未提交阶段，这会削弱仅基于 commit 的自动状态脚本准确度。

## Recommended Next Steps

- 把 metadata generation 与结构测试接入仓库级 CI 或任务系统，降低人工回归成本。
- 为 router 增加 repo-generated aliases 或可配置 intent hints，减少中文任务和短任务的平局命中。
- 增加 adapter drift check，确保 `.agents/`、`.github/` 与 canonical metadata 始终一致。
- 为 skill-hub 的状态更新保留专用模板，不再直接复用普通项目的 `docs/status.md` 风格。
- 修复 [docs/WORKSPACE_DIRECTORY_MAP.zh-CN.md](../WORKSPACE_DIRECTORY_MAP.zh-CN.md) 的编码与可读性问题，避免它成为治理盲点。

## Notes

- 本次状态更新优先采用 dry-run 思路，没有执行外部同步，也没有安装 post-commit hook。
- 当前文档反映的是“最近 commit + 当前 working tree”的综合状态，而不是仅依据已提交历史生成的业务型周报。
