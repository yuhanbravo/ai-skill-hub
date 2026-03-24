# Skill Invocation

该 prompt 定义一个统一的 skill 调用协议，用于在 skill-hub 中调用任意 skill。

## Goal

提供统一接口，稳定执行以下流程：

```text
select skill -> pass parameters -> execute -> return structured result
```

对应中文：

```text
选择 skill -> 传入参数 -> 执行 -> 输出结构化结果
```

## Invocation Pattern

所有 skill 调用必须符合以下任一形式：

```text
Use <skill-name> on <target>
with <parameters>
```

或：

```text
使用 <skill-name> 处理 <target>
参数：<parameters>
```

## Core Fields

### 1. Skill（必须）

```text
skill: <skill-name>
```

例如：

```text
skill: skill-governance
skill: project-takeover
skill: file-structure-check
```

### 2. Target（必须）

```text
target: <path / object / context>
```

例如：

```text
target: skills/project-takeover
target: skills/
target: current project
```

### 3. Parameters（可选）

使用 `key=value`：

```text
rewrite=true / false
mode=single / batch
level=strict / normal
```

## Invocation Templates

### 1. 单 skill 评估（默认安全模式）

```text
Use skill-governance on skills/project-takeover
rewrite=false
```

```text
使用 skill-governance 评估 skills/project-takeover
rewrite=false
```

### 2. 受控重写（必须显式授权）

```text
Use skill-governance on skills/project-takeover
rewrite=true
```

```text
使用 skill-governance 重写 skills/project-takeover
rewrite=true
```

### 3. 表达层收口（refinement）

```text
Use skill-refinement on skills/skill-governance
```

```text
使用 skill-refinement 优化 skills/skill-governance
```

### 4. 批量扫描（只读）

```text
Use skill-batch-evaluator on skills/
```

```text
使用 skill-batch-evaluator 扫描 skills/
```

### 5. Project 型 skill（takeover）

```text
Use project-takeover on current project
```

```text
使用 project-takeover 接管当前项目
```

### 6. Tool 型 skill（audit）

```text
Use file-structure-check on project-root
```

```text
使用 file-structure-check 检查项目结构
```

## Safety Rules

默认规则：

```text
rewrite=false
```

只有显式设置：

```text
rewrite=true
```

才允许修改。

### One Skill at a Time

```text
一次只允许调用一个 skill
```

### No Implicit Behavior

- 不允许隐式 rewrite
- 不允许跨 skill 执行
- 不允许自动推断参数

## Execution Semantics

不同类型 skill 的行为：

### Pattern Skill

```text
Input -> Process -> Output
```

### Project Skill

```text
scan -> understand -> structure -> output
```

### Tool Skill

```text
audit -> report -> fix(optional)
```

### Governance Skill

```text
evaluate -> diagnose -> decide -> refactor(optional)
```

## Output Expectation

所有 skill 必须输出结构化结果，例如：

- `SCORECARD`
- `REPORT`
- `SUMMARY`
- `CHANGELOG`
- `RISK_CHECK`

## Examples

### 示例 1：评估 skill

```text
Use skill-governance on skills/file-structure-check
rewrite=false
```

### 示例 2：重写 skill

```text
Use skill-governance on skills/financial-data-project-migration
rewrite=true
```

### 示例 3：批量扫描

```text
Use skill-batch-evaluator on skills/
```

## Summary

This prompt defines:

- a unified invocation interface
- a safe execution model
- a consistent skill calling language

该 prompt 定义了：

- 统一调用接口
- 安全执行模型
- 一致的 skill 调用语言
