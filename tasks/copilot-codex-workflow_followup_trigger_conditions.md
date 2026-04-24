# Follow-up Trigger Conditions：workflow-bootstrap 后续施工触发条件

## 文档标识

- doc id: `WF-FOLLOWUP-TRIGGER-CONDITIONS-V1`
- 主题：workflow-bootstrap workstream 后续施工触发条件
- 适用范围：`Copilot 主控 / Codex 施工` 这条 workflow-bootstrap 主线
- 当前状态基线：
  - single-repo implementation pilot 已完成
  - canonical path calibration 已完成
  - 当前不进入 rollout-readiness / distribution-readiness

---

## 1. 文档目的

本文件用于回答一个问题：

> 在当前 workstream 已完成 single-repo pilot 与 canonical path calibration 的前提下，  
> 未来什么情况下才值得重新开启下一轮施工？

本文件的作用不是开启新 phase，  
而是明确：
- 哪些情况构成有效 trigger
- 哪些情况不足以触发新施工
- 一旦触发，应进入哪一类后续 task package

---

## 2. 当前基线结论

截至当前阶段，已形成以下稳定结论：

1. `AGENTS.md` 是当前 project-side 最薄主入口。
2. `.github/copilot-instructions.md` 是 Copilot-specific thin adapter。
3. canonical guidance 必须保持优先级。
4. project-side 入口文件不得演化为第二规则库。
5. 当前 repo 不应将 `<project-local-canonical-skill-path>` 硬实体化。
6. 在仓库尚不存在独立 project-local canonical payload artifact 的前提下，受控占位比伪真实路径更稳。
7. 当前只完成了 single-repo pilot，不代表已具备 multi-repo rollout 条件。

因此，默认状态应为：

## 默认状态
**暂停主动推进，不开启新 phase。**

---

## 3. 有效触发条件（Valid Triggers）

只有满足以下条件之一，才值得重新开启下一轮施工。

### Trigger A：出现明确的 project-local canonical payload artifact

#### 定义
当前或后续 repo 中，出现一个明确、稳定、由维护者确认的 project-local canonical payload artifact，  
它满足以下条件中的大部分：

- 不是临时占位
- 不是聊天中口头假设
- 有明确路径
- 有明确维护责任
- 可被 project-side entrypoints 稳定回指
- 不会与 canonical guidance 的 source-of-truth 关系冲突

#### 触发后建议动作
开启一个新的小范围 task package，主题建议为：

- `project-local canonical path materialization review`
  或
- `canonical path re-evaluation after local payload availability`

#### 该 task package 的核心问题
- 当前 `<project-local-canonical-skill-path>` 是否可从受控占位升级为真实路径
- 升级后是否会削弱 canonical guidance 的优先级
- 升级后是否会诱发第二规则库风险

---

### Trigger B：需要验证第二种 consumer repo 类型

#### 定义
当前 single-repo pilot 结论需要跨 repo 类型验证。  
例如未来要验证的 repo 与当前 pilot 有明显差异：

- repo 结构差异较大
- 文档层次差异较大
- 是否有 `.github/` 基础设施差异较大
- 是否更偏脚本型 / 服务型 / 数据型 / 混合型
- 维护者使用方式不同，可能影响入口文件薄度与路径回指方式

#### 触发后建议动作
开启新的 validation / pilot task package，主题建议为：

- `second consumer repo type validation sketch`
  或
- `alternate consumer repo implementation pilot`

#### 该 task package 的核心问题
- 当前 entrypoint pair 是否仍成立
- `.github/copilot-instructions.md` 的薄适配边界是否仍够用
- canonical path 的受控占位策略是否仍成立
- 是否需要 repo-type specific adjustment

---

## 4. 不构成触发条件的情况（Non-Triggers）

以下情况**不足以**触发新一轮施工：

1. 只是觉得当前链路“已经挺完整，想继续推进”
2. 想提前准备 rollout，但没有新证据
3. 想先把 `.github/instructions/*.instructions.md` 或 `.github/agents/*.agent.md` 补出来
4. 想把当前 pilot 结果包装成通用模板定稿
5. 没有新的 canonical payload artifact
6. 没有新的 repo 类型验证需求
7. 只是为了让项目“看起来更完整”

这些情况都不应触发新的 phase。

---

## 5. 条件触发后的推荐动作映射

| Trigger | 推荐下一步 | 不应直接做什么 |
|---|---|---|
| Trigger A：出现明确 project-local canonical payload artifact | 开一个小范围 path materialization review / calibration task package | 不应直接进入 rollout |
| Trigger B：需要验证第二种 repo 类型 | 开一个新的 validation sketch 或 implementation pilot task package | 不应直接做 multi-repo distribution |

---

## 6. 当前建议状态

### 推荐状态
**条件触发型暂停态（trigger-gated pause）**

即：

- 当前 workstream 不主动推进新 phase
- 未来是否继续，只取决于 trigger 是否出现
- 若未出现 trigger，则保持当前结论不动

---

## 7. 后续引用方式

未来若需要开启下一轮施工，建议新 task package 在前置输入中引用本文件，并显式回答：

1. 本轮是由哪个 trigger 触发的
2. 触发证据是什么
3. 为什么这次不是无触发推进
4. 为什么当前边界允许重新进入施工

---

## 8. 一句话总结

**当前链路已完成 single-repo pilot 与 canonical path calibration；后续默认暂停，只有在出现明确的 project-local canonical payload artifact，或确有第二种 consumer repo 类型验证需求时，才重新开启施工。**