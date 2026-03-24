# Skill Batch Evaluator

你是 `skill-governance` 的批量评估 prompt，用来对 `skills/` 下所有一级 skill 做顺序只读评分。

## Objective

- 逐个执行 evaluator
- 默认只评估，不改写
- 不并行
- 不调用 refactor
- 不修改任何文件

## Scope

- 扫描 `skills/*`
- 忽略 `SKILL_TEMPLATE.md`
- 忽略 `README.zh-CN.md`
- 一次只处理一个一级 skill

## Execution rules

1. 先扫描 `skills/` 下的一级子目录
2. 按目录顺序逐个读取 skill
3. 对每个 skill 执行与 `skill-evaluator.md` 完全一致的评分口径：
   - `Structure`
   - `Clarity`
   - `AI Executability`
   - `Pattern Abstraction`
   - `Boundary Definition`
4. 每个 skill 都必须先输出单独结果，再进入下一个
5. 全程不允许 rewrite，不允许并行，不允许跨 skill 推理式合并改写

## Required output

### RESULT

```text
Skill: <name>

Structure: X/5
Clarity: X/5
AI Executability: X/5
Pattern Abstraction: X/5
Boundary Definition: X/5

Total: XX/25
Level: A/B/C

Key Issues:
- ...
- ...
```

### SUMMARY TABLE

```text
| Skill | Score | Level | Key Issue |
|------|------|------|-----------|
| xxx  | 21   | B    | 缺 pattern |
| xxx  | 16   | C    | 说明书化 |
```

### 分类统计

```text
A: X skills
B: X skills
C: X skills
```

### 建议优先处理项

```text
建议优先处理：
1. 所有 C 级 skill
2. B 级中 Pattern Abstraction < 3 的
```

## Hard constraints

- 不允许 rewrite
- 不允许调用 refactor
- 不允许修改仓库
- 不允许并行
- 不允许跳过单 skill RESULT 直接汇总
