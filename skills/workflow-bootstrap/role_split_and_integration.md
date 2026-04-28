# Role Split And Integration

## Ownership Boundary

`workflow-bootstrap` defines the workflow shell, role split, and runtime profile guidance. It helps a project decide how work moves between planning, review, implementation, reporting, and final review.

`workflow-bootstrap` does not own or redefine the task package, bounded execution, or execution report protocols. Those protocols remain owned by `chatgpt-handoff-pilot`.

## Canonical Role Chain

The canonical role chain is tool-agnostic:

```text
Drafter -> Reviewer -> Implementer -> Reporter -> Final Reviewer
```

This chain replaces tool-name-first wording such as `Copilot 起草 / Codex 施工` as the canonical expression. Tool names may still appear as adapter examples, but they are not requirements.

## Roles

### `Drafter` 起草者

定位：把一个模糊目标起草为可审阅的任务输入。

核心职责：

- 收敛目标、背景、授权文件、明确不做、验收标准和预期产物。
- 起草 task package、workflow plan 或 bounded scope proposal。
- 标出仍需 Reviewer 判断的假设、风险和维护者确认项。

边界：

- Drafter 可以建议路径和策略，但不能把未经 review 的方案当作已授权执行边界。
- Drafter 应保持 task package 清晰、可执行、可拒绝，而不是把所有上下文堆成第二规则库。

不负责事项：

- 不在未经 review 的情况下直接施工。
- 不重定义 task package / bounded execution / execution report 协议。
- 不把某个具体工具写成必须承担 Drafter 的 canonical requirement。

### `Reviewer` 审包者

定位：在 implementation 前检查任务包是否足够清晰、安全、可执行。

核心职责：

- 检查 scope、authorized files、out of scope、acceptance criteria 和 ownership boundary。
- 判断 task package 是否把 `workflow-bootstrap` 与 `chatgpt-handoff-pilot` 的职责边界写清。
- 在进入 bounded execution 前发现路径漂移、越权授权、协议 owner 混淆或缺失验收标准。

边界：

- Reviewer 是 bounded execution 前的 safety gate：只有任务包边界被审清楚，Implementer 才能按白名单施工。
- Reviewer 可以要求补充或收紧任务包，但不应把 review 变成新一轮无限扩 scope。

不负责事项：

- 不替 Implementer 施工。
- 不把 review 意见改写成新的 execution protocol。
- 不把工具偏好、订阅差异或模型强弱写入 canonical guidance。

### `Implementer` 执行者

定位：按已审阅的 task package 做 bounded execution。

核心职责：

- 先读取任务包，复述理解和边界，再只在授权范围内修改。
- 只实施本轮被授权的文件、目录和行为。
- 执行要求的最小验证；无法验证时记录原因。

边界：

- Implementer 执行的是已审阅边界，不自行扩写授权范围。
- 发现范围外问题时，默认记录为风险或 follow-up，而不是顺手修改。

不负责事项：

- 不重写 task package schema。
- 不替代 Reviewer 或 Final Reviewer。
- 不修改未授权路径、未授权协议层或 deferred runtime surfaces。

### `Reporter` 报告者

定位：把实施结果整理成可验收、可交接的 evidence trail。

核心职责：

- 生成 execution report，记录实际改动、未改内容、验证结果、风险、假设和后续建议。
- 明确说明哪些文件被修改，哪些 out-of-scope 项被有意保留。
- 为 Final Reviewer 提供足够的验收线索。

边界：

- Reporter 只报告本轮 bounded execution 的事实和判断，不替代最终审查。
- Reporter 应记录偏差、阻塞或验证缺口，而不是把未验证内容写成已完成。

不负责事项：

- 不补写新规则来掩盖越界。
- 不把 execution report 当作新的 canonical source of truth。
- 不替代 `chatgpt-handoff-pilot` 对 execution report 协议的 ownership。

### `Final Reviewer` 终审者

定位：在回执之后检查边界、质量、验证和下一步是否可收口。

核心职责：

- 检查实际改动是否只发生在授权范围内。
- 检查 validation 是否真实执行，未运行项是否被说明。
- 检查 role split、protocol ownership、thin-entry boundary 和 out-of-scope 约束是否仍成立。
- 判断是否可以进入 commit / handoff / status closure，或是否需要返回前序角色补充。

边界：

- Final Reviewer 是本轮交付的最终质量与边界检查，不是新的设计扩张阶段。
- Final Reviewer 可以提出 follow-up，但不应把 Phase 2 / Phase 3 内容提前塞入 Phase 1 交付。

不负责事项：

- 不重新发明 task package / bounded execution / execution report 协议。
- 不把工具 adapter、validator、CI 或 runtime pack manifest 当作本轮必须产物。
- 不把单一工具链经验提升为强制 canonical rule。

## Task Package Review As Safety Gate

Task package review is the safety gate before bounded execution because it converts intent into an explicit authorization boundary. Before implementation starts, the Reviewer checks whether the task package clearly states:

- what may be changed;
- what must not be changed;
- which files or directories are authorized;
- which protocol owns task packages, bounded execution, and execution reports;
- which validation or acceptance checks define completion.

Without this gate, the Implementer can accidentally treat a draft, preference, or tool-specific habit as permission to modify broader surfaces. With this gate, bounded execution starts from a reviewed boundary instead of an implicit conversation trail.

## Same-Tool Multi-Role Execution

The same tool may perform multiple roles in one workflow. For example, one tool may draft a task package, review it, implement it, and report results when the task is small or no second tool is available.

When one tool performs multiple roles, each phase switch must be explicit. The agent should state the active role and transition, such as:

```text
Drafter phase complete. Switching to Reviewer phase to check scope before implementation.
Reviewer phase complete. Switching to Implementer phase for bounded execution.
Implementation complete. Switching to Reporter phase for execution report.
```

This prevents "same tool continued working" from becoming implicit, unbounded execution.

## Adapter Examples, Not Requirements

Specific tools can be mapped to roles as local adapter examples:

- `Copilot` as a Drafter example.
- `ChatGPT` as a Reviewer or Final Reviewer example.
- `Codex` or `Cline` as Implementer / Reporter examples.
- `DeepSeek` as a model backend example when a local tool routes through it.

These are examples only. The canonical guidance is the role chain, not the tool list. Projects may choose different tools, combine roles in one tool, or insert human review, as long as role boundaries and stage transitions stay explicit.

## Integration With `chatgpt-handoff-pilot`

`workflow-bootstrap` and `chatgpt-handoff-pilot` integrate as separate layers:

1. `workflow-bootstrap` defines the workflow shell, role split, and runtime profile guidance.
2. Drafter prepares a task package using the protocol owned by `chatgpt-handoff-pilot`.
3. Reviewer checks the task package before implementation as the bounded-execution safety gate.
4. Implementer performs bounded execution under the reviewed task package.
5. Reporter writes the execution report using the protocol owned by `chatgpt-handoff-pilot`.
6. Final Reviewer checks boundary adherence, validation, and closure readiness.

In short: `workflow-bootstrap` explains how roles coordinate; `chatgpt-handoff-pilot` owns the task package, bounded execution, and execution report protocols.

## Thin Entry Guidance

Future project-side entries such as `AGENTS.md`, `.github/copilot-instructions.md`, or other runtime-pack surfaces should stay thin:

- Route readers to canonical guidance instead of copying it.
- Keep tool-specific wording as adapter examples, not requirements.
- Avoid turning project-side entries into a second rulebook.
- Keep task package / bounded execution / execution report protocol details pointed to `chatgpt-handoff-pilot`.
