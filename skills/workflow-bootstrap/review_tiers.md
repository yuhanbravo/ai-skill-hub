# Review Tiers

Status: advisory guidance for Reviewer-side task-package review.

This supporting asset helps a Reviewer choose the review strength for a task package before bounded execution. The tiers are guidance for human or agent judgment; they are not CI enforcement, not a validator, not an automatic stop rule, and not a replacement for the `chatgpt-handoff-pilot` task package, bounded execution, or execution report protocol.

`workflow-bootstrap` defines the workflow shell, role split, runtime profile, and review tier guidance. `chatgpt-handoff-pilot` continues to own task package, bounded execution, and execution report protocols.

## Tier Selection

Use the lowest tier that still gives the task package enough scrutiny for its risk. Escalate when the task touches canonical guidance, cross-project rules, project-side runtime surfaces, or any wording that could be mistaken for protocol ownership or automation authorization.

Runtime pack design and automation / validator candidates are listed below only as classification examples for `Heavy Review`. They do not authorize this Phase 2 work to design or implement runtime packs, automation, validators, scripts, tests, or CI.

## Light Review

中文定位：低风险、局部、文档型的小范围审包，用于确认任务边界足够清楚且不会影响 canonical protocol ownership。

适用场景：

- README 小更新、错字修正、链接或索引更新。
- 单文件非核心文档补充，且不改变 workflow role、protocol boundary 或 runtime profile。
- 已有内容的轻量澄清，授权文件很少，out-of-scope 明确。

核心检查项：

- Scope 是否单一且没有顺手扩展。
- Authorized files 是否窄且与目标直接相关。
- Out of scope 是否排除协议、automation、CI、validator、runtime pack 等越界方向。
- 是否没有把 tool-specific preference 写成 canonical requirement。

Second role / second tool review 建议：通常不需要；若文本触及 canonical skill、protocol ownership 或跨项目规则，应升级到 `Standard Review` 或 `Heavy Review`。

不适用场景：

- 修改 canonical skill 的核心职责、约束或执行流程。
- 调整 `workflow-bootstrap` 与 `chatgpt-handoff-pilot` 的 ownership boundary。
- 引入 project adapter、runtime pack、automation、validator 或 CI 相关内容。

典型例子：

- 修正 README 中一个过期链接。
- 给单个非核心文档增加导航索引。
- 调整一处不改变含义的文档措辞。

## Standard Review

中文定位：中等风险的常规审包，用于检查 workflow supporting asset、薄入口、project adapter 示例或 handoff/status 小更新是否保持边界清楚。

适用场景：

- 更新 workflow supporting asset，但不改变 canonical protocol ownership。
- 新增或调整 project adapter、`AGENTS.md`、handoff/status 小更新的说明。
- 修改 invocation examples 或 role guidance 的局部文字。
- 需要确认 `tasks/`、`docs/HANDOFF.md`、status surfaces 或 archive 的 evidence boundary 是否仍保守。

核心检查项：

- `workflow-bootstrap` 是否仍只定义 workflow shell、role split、runtime profile 和 review tier guidance。
- `chatgpt-handoff-pilot` 是否仍拥有 task package、bounded execution 和 execution report protocols。
- Thin entry 是否只做发现与回指，没有复制 canonical detail。
- 适用场景、授权文件、验收标准和 validation plan 是否可执行。
- 是否没有把 advisory guidance 写成 automation or enforcement behavior。

Second role / second tool review 建议：建议在范围较宽、涉及多个 supporting assets、或需要判断 ownership wording 时安排 second role review；不一定需要独立工具。

不适用场景：

- canonical skill 核心规则重写。
- 跨项目规则或 runtime pack design。
- automation / validator candidates 或任何可能被理解为 tooling rollout 的内容。

典型例子：

- 给 `workflow-bootstrap` 的 supporting asset 增加一个边界说明。
- 给 `AGENTS.md` 或 invocation example 增加薄入口式回指。
- 调整 handoff/status 小更新的 evidence placement wording。

## Heavy Review

中文定位：高风险、canonical 或跨项目影响的深度审包，用于防止协议 owner 混淆、范围漂移、自动化授权误读或 runtime-pack 阶段提前进入。

适用场景：

- canonical skill 修改，包括核心原则、执行流程、约束、role responsibilities 或 protocol boundary。
- 跨项目规则、project-side runtime surfaces、runtime pack design。
- automation / validator candidates，或任何可能被误读为 scripts、tests、CI、hooks、validators 的实现授权。
- 大范围文档重组、多个 canonical assets 同时变更，或涉及 `workflow-bootstrap` 与 `chatgpt-handoff-pilot` 的边界判断。

核心检查项：

- Scope 是否明确排除 Phase 3 runtime pack work、tool adapters、automation、validators、scripts、tests、CI 和 hooks。
- Authorized files 是否足够窄，是否没有开放未授权目录。
- Out of scope 是否能约束 Implementer，不会让 examples 变成 implementation permission。
- Acceptance criteria 是否可执行、可验证，且不会鼓励跳过必要 review。
- Ownership boundary 是否清楚：`workflow-bootstrap` explains coordination; `chatgpt-handoff-pilot` owns handoff protocols.
- Runtime pack design and automation / validator candidates 是否只作为分类示例，而不是本轮设计或实现对象。

Second role / second tool review 建议：强烈建议 second role review；对于 canonical skill 修改、跨项目规则或 runtime pack / automation 分类内容，建议由独立 reviewer 或另一工具做最终边界检查。

不适用场景：

- 单纯错字、链接、索引或非核心文档小修。
- 只影响一个低风险 supporting note 且不触及 ownership、runtime profile 或 future runtime surface 的变更。

典型例子：

- 修改 `workflow-bootstrap` 的 role chain 或 role responsibility。
- 起草跨项目 `AGENTS.md` thin-entry policy。
- 审查涉及 runtime pack design 的 task package，并确认它没有把 Phase 3 工作提前授权到当前阶段。
- 审查 automation / validator candidate wording，并确认它只是未来候选分类，不是当前实现范围。
