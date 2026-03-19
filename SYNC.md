# SYNC

## 本仓库的角色

- `D:\dev\codex-skill-hub` 是 `skill-hub` 主仓（SSOT）。
- 所有 skill 的正式演进、治理和版本基线都应以本仓库为准。

## 与业务项目的关系

- 业务项目中的 `.codex/skills` 只是运行副本，用于消费和验证 skill。
- 不要长期在业务项目副本中开发 skill。
- 若在业务项目中做了临时调整，应尽快回收并合并到本主仓。

## 双机同步策略

- 家里/公司之间通过 `git bundle` 同步。
- 每次同步前必须先 `commit`，避免未提交内容丢失或难以合并。
- 不要在两台机器同时并行修改同一批未同步内容。
- 同步时应以最近一次已提交且已确认的状态为交换单位。

## 标准操作示例

### 导出

```powershell
git bundle create ..\codex-skill-hub.bundle --all
```

### 新机器恢复

```powershell
git clone codex-skill-hub.bundle codex-skill-hub
```

### 已有仓库更新

```powershell
git fetch ..\codex-skill-hub.bundle
git merge FETCH_HEAD
```
