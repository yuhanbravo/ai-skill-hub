# 任务包：Copilot 主控 / Codex 施工工作流（Canonical 最小落地）

## 任务标识

- task id: `WF-CANONICAL-BOOTSTRAP-V0`
- 名称：Copilot 主控 / Codex 施工工作流最小落地
- 阶段：Phase 0 + Phase 1（最小实现）
- 提交方：Planner
- 日期：2026-04-21

## 背景

当前仓库 `ai-skill-hub` 已具备 canonical skill 层、adapter 层和分发工具层。
本任务的目标不是新建平行 workflow 母库，而是在现有母库内补齐一条清晰的“Copilot 主控 / Codex 施工”默认链路，并保持后续可下发 runtime pack 到项目仓库。

已确认前提：

1. `ai-skill-hub` 继续作为 canonical workflow / skill 母库。
2. 保持 canonical layer 与 runtime pack 的边界分离。
3. 优先复用已有 skills：
   - `chatgpt-handoff-pilot`
   - `project-takeover`
   - `update-project-status`
   - `documentation-governance`
   - `file-structure-check`
4. `chatgpt-handoff-pilot` 定位为协议层（task package / bounded execution / execution report），不单独承担完整 runtime 配置。

## 本次目标

在不改动现有 sync/export/import 工具逻辑、不做大规模模板铺设的前提下，完成 workflow 的 canonical 最小落地：

1. 新增一个中性 workflow/bootstrap canonical skill（最小内容）。
2. 明确该 skill 与 `chatgpt-handoff-pilot` 的职责边界。
3. 给出 future runtime pack 的最小文件清单（文档化，不做全量实现）。
4. 保持 adapter/distribution 一致性可校验。

## 本次范围（In Scope）

- 允许新增 1 个 canonical skill 目录（workflow/bootstrap 类，最小骨架）。
- 允许新增或更新少量文档，用于记录：
  - Copilot 主控 / Codex 施工链路
  - runtime pack 最小文件清单
  - planner / implementer / reviewer 分工与 bounded execution 规则
- 允许新增对应 `.agents` / `.github` adapter 入口（遵循现有薄封装规则）。
- 允许更新索引（`SKILLS_INDEX.md`、必要时 `skills_index.json`）以纳入新 skill。

## 明确不做（Out of Scope）

- 不做 runtime pack 全量模板落地（例如一次性创建完整 `.github/instructions`、`.github/agents` 体系）。
- 不改动既有 canonical skills 的核心执行契约。
- 不改动 `tools/sync_skills_to_nongit_project.ps1`、`tools/export_bundle.ps1`、`tools/import_bundle.ps1` 等分发逻辑。
- 不做 repo-wide rename、目录大迁移、跨层重构。
- 不引入 controller 化 orchestration 框架。

## 授权文件与目录（Authorized Files / Areas）

- `skills/`（仅新增 workflow/bootstrap skill 子目录）
- `.agents/skills/`（仅新增对应薄封装入口）
- `.github/skills/`（仅新增对应兼容入口）
- `SKILLS_INDEX.md`
- `skills_index.json`（如通过既有脚本生成）
- `tasks/`（可补充 execution report）

未在以上白名单内的路径，默认无权限修改。

## 期望交付（Expected Deliverables）

1. 新 canonical skill（建议名）：`workflow-bootstrap`
2. 新 skill 的 `SKILL.md`（执行向）与 `README.md`（说明向）
3. 可复用模板（最小集，放在新 skill 内）：
   - runtime pack 清单模板（Markdown）
   - role split / bounded execution 说明模板（Markdown）
4. 对应 adapter 入口：
   - `.agents/skills/workflow-bootstrap/SKILL.md`
   - `.agents/skills/workflow-bootstrap.md`
   - `.github/skills/workflow-bootstrap.md`
5. 索引更新：`SKILLS_INDEX.md`（以及必要的 `skills_index.json`）
6. execution report（单独文档或回执段落）

## 执行规则（Execution Rules）

必须遵循 `chatgpt-handoff-pilot` 的 bounded execution 风格：

1. 动手前先复述：目标、范围、明确不做、将触及文件。
2. 仅在授权目录内修改。
3. 不顺手修复范围外问题；发现后单列为风险或后续建议。
4. 若遇到命名/边界不确定项，先记录假设并采用最保守实现。
5. 全程保持 canonical source-of-truth 原则：`skills/` 为唯一权威层。

## 验证与验收（Validation / Acceptance）

至少完成以下检查并在回执中报告结果：

1. 结构检查：新增 skill 目录满足仓库 skill 结构要求（`SKILL.md` + `README.md`）。
2. adapter 合规：
   - `python tools/check_adapter_consistency.py --mode hub`
3. 本地最小验证入口（建议）：
   - `powershell.exe -NoProfile -ExecutionPolicy Bypass -File tools\run_local_checks.ps1 -Checks governance`
4. 索引可发现：新 skill 出现在 `SKILLS_INDEX.md`，且 adapter 路径可追溯到 canonical。

验收通过标准：

- 新 skill 可被发现（canonical + adapters + index）。
- 未破坏现有 hub/consumer adapter contract 边界。
- 文档明确了 workflow 链路与 runtime pack 最小清单，但未越界实现全量 runtime pack。

## 执行回执要求（Execution Report Requirements）

执行完成后必须输出结构化回执，至少包含：

1. 本次改了什么。
2. 本次没改什么（尤其是 out-of-scope 项）。
3. 实际运行了哪些验证命令及结果摘要。
4. 当前阻塞与风险。
5. 下一步最小建议动作（面向下一阶段 runtime pack template 落地）。

## 补充上下文

- 关键参考：
  - `README.md`
  - `SKILLS_INDEX.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `docs/ai/DISCOVERY_AND_INVOCATION.md`
  - `docs/governance/adapter_governance.md`
  - `docs/governance/documentation_status_coordination.md`
