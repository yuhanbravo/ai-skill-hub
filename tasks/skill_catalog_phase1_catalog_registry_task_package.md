# Skill Catalog / Template Registry Phase 1 Task Package

- Task status: proposed / ready for review before implementation
- Task type: bounded documentation-only implementation package (Phase 1)

## 1) Objective

在不改变现有 canonical skill 内容与分层边界的前提下，完成最小入口治理实施：

- 新增 `docs/SKILL_CATALOG.md`
- 新增 `docs/TEMPLATE_REGISTRY.md`
- 新增 `tasks/skill_catalog_phase1_catalog_registry_execution_report.md`

目标是建立集中索引，而不是迁移或重写内容。

## 2) Allowed changes for Phase 1

Phase 1 仅允许：

1. Create `docs/SKILL_CATALOG.md`
2. Create `docs/TEMPLATE_REGISTRY.md`
3. Create `tasks/skill_catalog_phase1_catalog_registry_execution_report.md`

除以上三项外，不授权其他文件改动。

## 3) Explicitly forbidden changes for Phase 1

Phase 1 明确禁止：

- 修改任何现有 `skills/**` 内容
- 修改任何现有 `.agents/skills/**` 内容
- 修改任何现有 `.github/skills/**` 内容
- 修改 `docs/bridge/**`
- 修改 `docs/HANDOFF.md`
- 修改 `docs/status/**`
- 迁移 templates 到新目录
- 重命名目录
- 复制完整 `SKILL.md` 正文到 catalog/registry
- 将 `tasks/` 历史 pattern 直接提升为 canonical templates

## 4) Required catalog fields (`docs/SKILL_CATALOG.md`)

每个 skill 条目至少包含：

- `skill path`
- `short purpose`
- `owner / category`
- `canonical status`
- `intended use case`
- `related skills`
- `side-effect level`

## 5) Required registry fields (`docs/TEMPLATE_REGISTRY.md`)

每个 asset 条目至少包含：

- `asset path`
- `asset type`（`template` / `snippet` / `prompt` / `example` / `candidate`）
- `owner skill`
- `canonical status`
- `intended use case`
- `source surface`
- `side-effect level`
- `notes`

## 6) Historical tasks handling

- `tasks/` 下资产可被列为 `historical` / `candidate`。
- 任何 candidate 不得在 Phase 1 自动变为 canonical。
- candidate → canonical promotion 必须通过后续独立 task（显式审批与边界说明）。

## 7) Validation checklist

实施 Phase 1 时，必须满足：

1. 仅创建授权的三个新文件。
2. 无任何现有文件被修改。
3. PR 1 中不得创建 `docs/SKILL_CATALOG.md`。
4. PR 1 中不得创建 `docs/TEMPLATE_REGISTRY.md`。
5. 不复制 canonical `SKILL.md` 正文。
6. bridge / adapter / tasks 边界在索引中保持显式。
7. `git diff --check` 通过。

## 8) Expected execution report format (for Phase 1)

`tasks/skill_catalog_phase1_catalog_registry_execution_report.md` 预期至少包含：

- `files created`
- `files intentionally untouched`
- `catalog coverage summary`
- `registry coverage summary`
- `boundary checks`
- `validation commands`
- `risks / follow-ups`

## 9) Boundary reminders

- `skills/` 是 skill 内容唯一 canonical source。
- `.agents/skills/` 与 `.github/skills/` 仅 discovery surfaces。
- `docs/bridge/` 是 mirror/reference，不是 active source。
- `tasks/` 是历史证据层，不自动获得 canonical 权限。
- `docs/HANDOFF.md` 与 `docs/status/` 是 state snapshots，不是模板主入口。

