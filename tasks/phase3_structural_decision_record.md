# Phase 3 Structural Decision Record (ADR Style)

日期：2026-04-21  
范围：Planning-only（不实施重构）

## 0) Brief Repo Understanding

该仓库是多 AI skill hub，存在 canonical（`skills/`）、adapter（`.agents/skills/`）、fallback（`.github/skills/`）与多受众文档层（`docs/ai`、`docs/human`、`docs/bridge`）。
本次评估需优先保证层边界稳定，避免在治理基础未稳时做高破坏结构变更。

## 1) Identified Issues

1. Bridge 全量镜像的长期维护成本与漂移风险需要定量判断。  
2. Router/Pipeline 在跨 agent 场景下可能缺少一致性约束，导致行为不够确定。  
3. 若直接进入“自动生成一切”或“强化编排”，有过度工程化风险。

---

## ADR-01: Bridge Mirror Strategy

### Context

需要在以下选项中做决策：
- A. 保留 bridge 全量镜像
- B. 改为自动生成镜像
- C. 改为部分镜像（规则化）

### Options Analysis

#### A. 保留全量镜像
- 收益：阅读路径直接、桥接内容完整可见
- 风险：重复内容维护压力高，易出现 doc drift
- 回滚复杂度：低（维持现状）

#### B. 自动生成镜像
- 收益：理论上最小漂移、可规模化
- 风险：生成链/规则复杂，治理不稳定期容易产生“系统先于治理”
- 回滚复杂度：中高（需要撤销生成流程和约束）

#### C. 部分镜像（规则化）
- 收益：降低重复与维护量，同时保留关键桥接可读性
- 风险：需要定义“必须镜像清单”与同步责任
- 回滚复杂度：中（可逐目录恢复）

### Decision

**决策：选择 C（部分镜像 + 规则化），并将 B（自动生成）设为 later。**

### Why Now

- 与“低风险增量优先”一致。
- 能在不引入复杂生成链的前提下显著降低漂移。

### Consequences

- 正向：可维护性提升、避免一次性重构。
- 负向：前期需要制定 mirror 白名单/准入规则。

### Rollback Path

1. 保留现有 bridge 历史文件索引；
2. 若部分镜像效果不佳，按目录回退至“人工全量镜像”；
3. 停止新增规则门禁，仅保留人工审阅同步。

### Trigger Conditions (for moving to auto-generation later)

仅当满足以下条件再考虑自动生成：
- 两个连续迭代周期内镜像规则稳定；
- adapter/canonical 变更频率与模式可被稳定抽象；
- 已有最小验证脚本可检测镜像失配。

---

## ADR-02: Deterministic Policy Layer for Router/Pipeline

### Context

目标是提高跨 agent 执行的一致性与可审计性，但明确不走 controller 化。

### Options Analysis

#### A. 维持现状
- 收益：零迁移成本
- 风险：策略分散，执行口径可能不一致
- 回滚复杂度：无

#### B. 轻量确定性策略层（非 controller）
- 收益：规则声明化、审计友好、保留现有流水线结构
- 风险：需要梳理最小策略集合与冲突优先级
- 回滚复杂度：低中（可关闭策略层，退回原流程）

#### C. 强策略编排（接近 controller）
- 收益：高度统一
- 风险：架构侵入大，偏离本阶段“避免过早重构”目标
- 回滚复杂度：高

### Decision

**决策：选择 B（轻量确定性策略层），明确排除 C（当前阶段不做）。**

### Policy Layer Boundary (Non-controller)

- 仅提供“规则判定与执行前校验”；
- 不接管业务编排与状态机；
- 不引入中心化控制平面；
- 保持 router/pipeline 主体流程不变。

### Consequences

- 正向：提升一致性和可追溯性，迁移成本可控。
- 负向：需要维护规则版本与优先级说明。

### Rollback Path

1. 策略层通过特性开关可停用；
2. 回退至原 router/pipeline 直连路径；
3. 保留规则文档用于复盘，不影响运行主流程。

### Trigger Conditions (for stronger layer)

仅当满足以下条件再评估增强：
- 已验证轻量策略层覆盖主要冲突场景；
- 回归检查显示一致性收益稳定；
- 治理文档和角色分工稳定至少 2 个周期。

---

## 3) Migration / No-Migration Conclusion Matrix

| 主题 | Now | Later | Not-Now |
|---|---|---|---|
| Bridge 镜像策略 | 部分镜像 + 规则化 | 自动生成镜像 | 继续无约束全量扩张 |
| Router/Pipeline 策略 | 轻量确定性策略层（非 controller） | 视触发条件评估增强 | controller 化改造 |

## 4) Recommendation Summary

### Low-risk / High-value（建议现在做）
1. 产出并评审上述两份 ADR（本文件即初版）。
2. 定义 bridge 部分镜像白名单规则。
3. 定义 router/pipeline 轻量策略层最小规则集与优先级。

### Medium-scope Governance（建议下一阶段）
1. 建立镜像失配最小检查脚本（仅校验，不自动重写）。
2. 给策略层增加版本化与变更日志约束。

### High-disruption Structural Change（当前不建议）
1. bridge 全量自动生成全面接管。
2. router/pipeline 进入 controller 化架构。

## 5) Risks and Open Questions

- 风险：规则定义过粗导致执行歧义。  
  缓解：先最小规则集 + 例外清单。
- 风险：局部优化引发跨层不一致。  
  缓解：每次调整需映射 canonical/adapter/bridge 影响面。
- 待确认：当前变更频率是否已足够支撑自动生成 ROI。
