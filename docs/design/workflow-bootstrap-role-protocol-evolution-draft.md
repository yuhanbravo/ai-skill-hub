# Workflow Bootstrap Future Evolution Draft

Status: Draft  
Scope: workflow-bootstrap / non-git workflow / role-based AI collaboration  
Source: Derivative_Data non-git workflow pilot and follow-up discussion

## 1. 背景

当前工作流最初采用的是：

```text
Copilot 主控 / 出 task package
Codex 按 task package 做 bounded execution
execution report 作为主留痕
handoff / status 做最小增量收口
```

在 Derivative_Data non-git / low-git 项目中，该模式已经完成一轮较完整的 project-side pilot。试跑结果证明：

- `tasks/` 可以作为 non-git 项目的 per-task 主留痕路径；
- task package / execution report 成对落盘有助于替代部分 Git history；
- execution report 可以承担 primary per-task evidence trail；
- handoff / status 不应成为 per-task trace log，只做 minimal closure；
- `archive/` 应保持 historical / inactive，不作为 active workflow line；
- `AGENTS.md` 适合作为 project-side master thin entry；
- `.github/copilot-instructions.md` 适合作为 Copilot-specific thin adapter；
- `.github/copilot-instructions.zh-CN.md` 可以作为 translated mirror，而不是第二规则库；
- `tasks/README.md` 可以作为轻量索引，帮助人类和 AI agent 快速理解多轮任务链。

本轮 pilot 的 review memo 已经明确区分：

- strong candidates；
- review candidates；
- project-local only；

因此下一步应在 ai-skill-hub 中保守吸收 workflow-bootstrap 的通用经验，而不是复制 Derivative_Data 的项目事实。

## 2. 当前工作流的有效部分

当前模式中最值得保留的，不是某个具体工具组合，而是下面这条角色链：

```text
Drafter
  ↓
Reviewer
  ↓
Implementer
  ↓
Reporter
  ↓
Final Reviewer
```

对应到当前工具实践中，大致是：

| 角色 | 当前默认工具 | 说明 |
|---|---|---|
| Drafter | Copilot | 利用 VS Code / 项目上下文生成 task package draft |
| Reviewer | ChatGPT / Codex | 审查 task package 的路径、scope、authorized files、out of scope 和验收标准 |
| Implementer | Codex | 按审过的 task package 做 bounded execution |
| Reporter | Codex | 生成 execution report，作为 per-task evidence |
| Final Reviewer | ChatGPT / Copilot / 人类维护者 | 检查是否越界、是否符合初始目标、是否需要 handoff/status 最小收口 |

这个抽象比“Copilot 主控 / Codex 施工”更稳，因为它不依赖某个工具长期保持同样能力或订阅条件。

## 3. 为什么不能完全省略审包

即使未来 Copilot 也接入更强模型，也不建议完全取消 task package review。

原因是：

```text
task package = 执行授权文件
```

它不仅是计划文本，还是施工边界。  
一旦 task package 中出现路径不准、授权文件过宽、execution report 路径不清、future target 被写成 current fact 等问题，后续强模型也可能在错误授权下施工。

因此，审包不应被理解为“因为 Copilot 弱才需要”，而应被理解为 bounded execution 的安全阀。

推荐长期原则：

```text
For important bounded execution, the task package should be reviewed before implementation.
The drafter and implementer may be different tools, or the same tool acting in different roles.
```

中文口径：

```text
对重要 bounded execution，task package 应在施工前经过审阅。
起草者和执行者可以是不同工具，也可以是同一工具在不同角色下完成。
```

## 4. 审包分级机制

未来不需要每次都重审包，可以根据任务风险分级。

### 4.1 极轻审包

适用场景：

- README 小更新；
- `tasks/README.md` 追加索引；
- 单文件文档同步；
- 非 canonical 的轻量导航补充。

检查项：

```text
1. Authorized Files 是否为完整路径
2. Execution report 是否落在 tasks/
3. Out of Scope 是否清楚
4. 是否没有代码 / 自动化 / CI 越界
5. task package / execution report 是否成对
```

### 4.2 标准审包

适用场景：

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `.github/copilot-instructions.zh-CN.md`
- workflow-bootstrap supporting assets
- handoff/status 边界调整

检查项：

```text
1. 路径是否完整
2. 授权文件是否足够窄
3. workflow-bootstrap / chatgpt-handoff-pilot 边界是否清楚
4. project-side entry 是否可能变成第二规则库
5. handoff/status 是否只做 minimal closure
6. archive 是否没有成为 active workflow line
```

### 4.3 重审包

适用场景：

- ai-skill-hub canonical skill 修改；
- 从项目端回灌 workflow-bootstrap；
- runtime pack 设计；
- validator / automation / CI 候选；
- 跨项目推广规则。

检查项：

```text
1. 是否只吸收 generalized workflow guidance
2. 是否排除了 project-local facts
3. 是否保持 chatgpt-handoff-pilot schema 不被 workflow-bootstrap 重定义
4. 是否避免把 non-git profile 写成所有项目强制规则
5. 是否避免过早引入 validator / automation / CI
```

## 5. 工具无关的角色协议

未来 workflow-bootstrap 不应被具体工具名绑死，而应以角色协议为核心。

推荐抽象：

```text
Drafter → Reviewer → Implementer → Reporter → Final Reviewer
```

工具只是 adapter。

### 当前工具映射

```text
Copilot = drafter
ChatGPT / Codex = reviewer
Codex = implementer + reporter
ChatGPT / Copilot = final reviewer
```

### 如果 Copilot 后续升级为更强模型

```text
Copilot = drafter + light reviewer
Codex = implementer + reporter
ChatGPT = selective reviewer
```

这时审包可以变轻，但不建议完全取消。

### 如果以后不再订阅 Copilot

```text
Codex = drafter + reviewer
Cline + DeepSeek = local implementer
Codex / ChatGPT = final reviewer
```

### 如果以后不再订阅 Codex

```text
Copilot / ChatGPT = drafter + reviewer
Cline + DeepSeek = local implementer + reporter
ChatGPT / 人类维护者 = final reviewer
```

### 如果只有一个强工具

也可以使用同一个工具分角色执行：

```text
1. Draft task package
2. Review task package with checklist
3. Execute only after review
4. Write execution report
5. Final self-audit
```

关键不是工具数量，而是阶段切换。

## 6. 稳定协议层与工具适配层

未来 workflow-bootstrap 可以拆成两层。

### 6.1 稳定协议层

不随工具变化：

```text
task package
authorized files
out of scope
acceptance criteria
bounded execution
execution report
handoff/status minimal closure
tasks/ as per-task trace
archive as inactive history
```

### 6.2 工具适配层

随订阅、模型、IDE 变化：

```text
Copilot adapter
Codex adapter
Cline adapter
DeepSeek adapter
ChatGPT adapter
```

未来可以考虑在 workflow-bootstrap 中增加类似结构：

```text
skills/workflow-bootstrap/
  SKILL.md
  non_git_runtime_profile.md
  role_split_and_integration.md
  runtime_pack_minimal_manifest.md
  examples/invocation_examples.md
  tool_adapters/
    copilot_as_drafter.md
    codex_as_reviewer_executor.md
    cline_as_local_implementer.md
    deepseek_as_model_backend.md
```

但这不是当前阶段的优先事项。当前优先事项仍然是先吸收 non-git runtime profile 的 strong candidates。

## 7. 当前阶段不应立刻做的事

以下事项应暂缓：

```text
1. 把 Copilot / Codex 的当前订阅能力差异写进 canonical
2. 创建 .github/instructions/
3. 创建 .github/agents/
4. 新增 validator / automation / CI
5. 把 Derivative_Data 的项目命令、环境、业务目录写成通用规则
6. 把 non-git runtime profile 写成所有项目强制规则
7. 直接把 Cline / DeepSeek 适配层写入 workflow-bootstrap
```

这些都可以作为未来 evolution candidate，但不应干扰下一轮 ai-skill-hub 的保守吸收任务。

## 8. 推荐的短期行动

短期仍按当前实践执行，但在措辞上做微调。

从：

```text
Copilot 主控 / Codex 施工
```

调整为：

```text
Copilot 起草 task package
ChatGPT / Codex 审包
Codex 按审过的 task package 施工
execution report 留痕
ChatGPT / Copilot / 人类维护者复核
```

这已经反映最近几轮真实经验：  
Copilot 适合起草和整理上下文，但 task package 在进入施工前需要经过路径与边界审阅。

## 9. 推荐的中期行动

在 ai-skill-hub 中先完成：

```text
review_and_absorb_non_git_runtime_profile_candidates
```

优先吸收：

- non-git / low-git runtime profile；
- `tasks/` primary trace convention；
- task package / execution report pairing；
- execution report as primary per-task evidence trail；
- handoff/status minimal closure；
- archive non-active boundary；
- workflow-bootstrap 与 chatgpt-handoff-pilot 的协议边界；
- invocation examples 中的 handoff framing。

暂不吸收：

- 工具订阅差异；
- Cline / DeepSeek adapter；
- validator / automation / CI；
- `.github/instructions/` / `.github/agents/` rollout。

## 10. 推荐的后续单独任务

等 non-git runtime profile 被吸收后，再单独开一轮：

```text
refine_workflow_role_split_for_drafter_reviewer_executor
```

目标：

- 将 `Copilot planner / Codex implementer` 的工具绑定表述，逐步升级为 role-based 表述；
- 增加 task package review 作为 bounded execution 的推荐步骤；
- 明确 drafter / reviewer / implementer 可以是不同工具，也可以是同一工具的不同角色；
- 不把任何特定订阅组合写成 canonical 规则。

可能修改文件：

```text
skills/workflow-bootstrap/role_split_and_integration.md
skills/workflow-bootstrap/examples/invocation_examples.md
skills/workflow-bootstrap/README.md
skills/workflow-bootstrap/SKILL.md
```

## 11. 长期演进方向

长期目标不是维护一条固定的 “Copilot + Codex” 工作流，而是形成：

```text
Role protocol + Tool adapter layer
```

也就是：

```text
稳定角色协议：
Drafter / Reviewer / Implementer / Reporter / Final Reviewer

稳定证据协议：
Task package / Execution report / Handoff minimal closure / tasks index

可替换工具映射：
Copilot / Codex / ChatGPT / Cline / DeepSeek / future tools
```

这样无论未来订阅、模型、IDE 工具如何变化，核心 workflow 不需要重写，只需要调整工具适配层。

## 12. 当前推荐结论

当前应采用：

```text
行为先调整，制度后固化
```

具体来说：

1. 实际操作中立即采用“Copilot 起草、Codex/ChatGPT 审包、Codex 施工”；
2. ai-skill-hub 下一轮先吸收 non-git runtime profile strong candidates；
3. 暂不把工具订阅差异写入 canonical；
4. 后续单独开一轮 role-split refinement；
5. 长期将 workflow-bootstrap 从工具名驱动升级为角色协议驱动。

一句话总结：

```text
审包步骤不应依赖某个模型弱不弱，而应作为 bounded execution 的安全阀保留；
真正该进化的是把 workflow 从 “Copilot/Codex 固定搭配”
升级成 “角色协议 + 工具适配层”。
```
