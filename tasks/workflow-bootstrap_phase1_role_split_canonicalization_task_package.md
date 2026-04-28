# 任务包：workflow-bootstrap Phase 1 Role Split Canonicalization

## 任务标识

- task id: `WF-BOOTSTRAP-PHASE1-ROLE-SPLIT-CANONICALIZATION-V1`
- 名称：workflow-bootstrap Phase 1 / Role Split Canonicalization
- 阶段：`Phase 1`
- 提交方：Drafter
- 日期：`2026-04-28`
- 前置输入：
  - `skills/workflow-bootstrap/SKILL.md`
  - `skills/workflow-bootstrap/role_split_and_integration.md`
  - `skills/workflow-bootstrap/examples/invocation_examples.md`
  - `skills/chatgpt-handoff-pilot/SKILL.md`
  - `tasks/copilot-codex-workflow_task_package_v1.md`
  - `tasks/copilot-codex-workflow_phase3d_canonical_path_calibration_task_package.md`
  - `docs/design/workflow-bootstrap-role-protocol-blueprint.md`

---

## Scope Restatement

本轮只做 `workflow-bootstrap` 的 Phase 1：`Role Split Canonicalization`。

目标是把当前偏工具名驱动的默认协作表述：

```text
Copilot 起草 / Codex 施工
```

抽象为工具无关的角色协议表述：

```text
Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer
```

本轮只在 `workflow-bootstrap` 文档层完成该抽象与边界说明，不扩大 execution protocol，不替代 `chatgpt-handoff-pilot`，也不把当前工具分工写成新的 canonical requirement。

本轮应明确：

1. `workflow-bootstrap` 负责 workflow shell / role split / runtime profile guidance。
2. task package / bounded execution / execution report 协议仍由 `chatgpt-handoff-pilot` 负责。
3. role-based handoff 是 tool-agnostic 的。
4. review before implementation 是 bounded execution 的 safety gate。
5. 同一工具可承担多个角色，但必须显式阶段切换。

---

## Background

Phase 0 已完成或基本完成，其目标是把 non-git / low-git pilot 中已经验证的通用经验保守吸收到 `workflow-bootstrap`，但不复制项目侧事实。

Phase 0 已形成的关键基线包括：

- `non_git_runtime_profile.md` 已建立为 supporting asset。
- `examples/invocation_examples.md` 已补充 non-git / low-git handoff 示例。
- `SKILL.md` 已补充 supporting asset 回指和边界说明。
- `tasks/` 已被写成 preferred project-local evidence path，而不是 mandatory global path。
- `archive/` 已明确保持 historical / inactive。
- handoff / status 只做 minimal closure，不作为 per-task trace log。
- `workflow-bootstrap` 只负责 workflow shell / role split / runtime profile guidance。
- `chatgpt-handoff-pilot` 继续作为 task package / bounded execution / execution report 协议 owner。

当前 `skills/workflow-bootstrap/role_split_and_integration.md` 仍主要围绕：

```text
planner -> implementer -> reviewer
```

以及：

```text
Copilot 主控 / Codex 施工
```

这足以表达最小默认链路，但还没有把角色协议进一步 canonicalize 为可迁移、可适配、与具体工具解耦的 role chain。

Phase 1 的任务不是抛弃当前经验，而是把这些经验上提为更稳定的角色定义，同时继续保留工具示例只作为 adapter examples 出现。

---

## Target Files

优先目标文件：

- `skills/workflow-bootstrap/role_split_and_integration.md`

允许做最小补充或回指的文件：

- `skills/workflow-bootstrap/SKILL.md`
- `skills/workflow-bootstrap/examples/invocation_examples.md`

本轮执行回执落点：

- `tasks/workflow-bootstrap_phase1_role_split_canonicalization_execution_report.md`

---

## Authorized Files

本轮仅授权修改以下文件：

- `skills/workflow-bootstrap/role_split_and_integration.md`
- `skills/workflow-bootstrap/SKILL.md`（仅允许最小回指，不复制 supporting asset 正文）
- `skills/workflow-bootstrap/examples/invocation_examples.md`（仅允许增加一个短例）
- `tasks/workflow-bootstrap_phase1_role_split_canonicalization_execution_report.md`（执行完成后新增）

本任务包文件可保留于：

- `tasks/workflow-bootstrap_phase1_role_split_canonicalization_task_package.md`

除上述路径外，默认无权修改其他文件或目录。

---

## Out of Scope

本轮明确不做以下事项：

- 不修改 `chatgpt-handoff-pilot`。
- 不重定义 task package / bounded execution / execution report schema。
- 不创建 `tool_adapters/` 或其他新的 adapter surface。
- 不新增 validator / scripts / tests / CI。
- 不新增 `.github/instructions/`。
- 不新增 `.github/agents/`。
- 不把 `Copilot / Codex` 固定分工写成 canonical rule。
- 不把订阅差异、模型强弱或工具偏好写入 canonical guidance。
- 不把 `tasks/` 写成所有项目的强制全局路径。
- 不进入 Phase 2 review tier guidance。
- 不进入 Phase 3 runtime pack manifest。
- 不进入 tool adapter 或 validator 设计。
- 不修改 `README.md`、`docs/HANDOFF.md`、scripts、tests 或 skill-hub status surfaces。

---

## Required Content

`skills/workflow-bootstrap/role_split_and_integration.md` 至少应新增或重组出以下内容：

1. 一个明确的 `role chain`，使用工具无关表述：

   ```text
   Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer
   ```

2. 每个 role 的中文定位、核心职责、边界和不负责事项：
   - `Drafter`
   - `Reviewer`
   - `Implementer`
   - `Reporter`
   - `Final Reviewer`

3. 明确解释 `task package review` 为什么是 bounded execution 的 safety gate。

4. 明确说明同一工具可以承担多个角色，但必须做显式阶段切换，不能把“同一工具连续操作”写成隐式无边界执行。

5. 明确说明 `Copilot`、`Codex`、`ChatGPT`、`Cline`、`DeepSeek` 等仅作为 adapter examples，而不是 canonical requirements。

6. 明确说明 `workflow-bootstrap` 只定义 workflow shell / role split / runtime profile guidance。

7. 明确说明 task package / bounded execution / execution report 协议仍归 `chatgpt-handoff-pilot`。

如需最小补充：

- `skills/workflow-bootstrap/SKILL.md` 可增加一句回指，例如：

  ```text
  For role-based workflow handoff, see role_split_and_integration.md.
  ```

- `skills/workflow-bootstrap/examples/invocation_examples.md` 可增加一个短例，例如：

  ```text
  Example: Move from tool-name workflow to role-based handoff
  ```

但这两处补充必须保持最小，不得复制大段 supporting asset 内容。

---

## Acceptance Criteria

本轮完成后必须满足以下条件：

1. role split 已被表述为 tool-agnostic 的 canonical guidance。
2. 当前工具名只作为 examples 出现，不成为 requirements。
3. `review before implementation` 被定义为 safety gate。
4. 同一工具多角色执行时，需要显式阶段切换。
5. `workflow-bootstrap` 仍只定义 workflow shell / role split / runtime profile。
6. `chatgpt-handoff-pilot` 仍是 task package / bounded execution / execution report 协议 owner。
7. 改动范围保持在 `workflow-bootstrap` 文档面。
8. 未触发 scripts / tests / CI / adapter governance 的额外施工。

---

## Validation Plan

实施侧完成文档改动后，至少执行以下验证：

1. 内容边界检查：确认新增内容没有把 `workflow-bootstrap` 写成 execution protocol owner。
2. ownership 检查：确认 `chatgpt-handoff-pilot` 仍被明确写为 task package / bounded execution / execution report 协议 owner。
3. tool-agnostic 检查：确认 `Copilot / Codex / ChatGPT / Cline / DeepSeek` 若被提及，均以 example / adapter example 出现，而非 canonical requirement。
4. role-chain 检查：确认 `Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer` 已在主目标文件中出现且有职责边界说明。
5. explicit stage-switch 检查：确认同一工具多角色执行时的显式阶段切换已被写明。
6. scope 检查：确认没有越权修改 `chatgpt-handoff-pilot`、tests、scripts、CI、`.github/instructions/`、`.github/agents/` 或其他未授权路径。

若环境允许，可补充最小文本检查；若无自动化验证，则至少在 execution report 中报告上述人工检查结果。

---

## Execution Report Requirement

执行完成后必须新增：

- `tasks/workflow-bootstrap_phase1_role_split_canonicalization_execution_report.md`

该 execution report 至少包含：

1. 本次改了什么。
2. 本次没改什么。
3. 实际验证了什么。
4. 是否发现越界风险或表达歧义。
5. 是否需要后续最小 follow-up。

如果本轮只完成主目标文件而未修改 `SKILL.md` 或 `examples/invocation_examples.md`，也必须在 report 中显式写明这是有意保持最小改动，而不是遗漏。

---

## Recommended Commit Message

```text
docs(workflow-bootstrap): add role split integration guidance
```

---

## Execution Notes

执行侧应遵循以下顺序：

1. 先读取本任务包并复述边界。
2. 先改 `skills/workflow-bootstrap/role_split_and_integration.md`，把 role-based canonicalization 做完整。
3. 仅在确有必要时，对 `SKILL.md` 或 `examples/invocation_examples.md` 做最小回指或短例补充。
4. 完成后执行最小验证。
5. 最后输出 execution report。

本轮是 `workflow-bootstrap` 的文档型 bounded execution，不是协议扩张轮次，也不是工具适配层扩建轮次。
