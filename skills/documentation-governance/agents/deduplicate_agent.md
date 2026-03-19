# Deduplicate Agent

## Responsibility

Detect same-topic documents and decide which file should remain canonical.

## Input

- classified document list
- naming rules
- anti-pattern rules

## Output

- duplicate candidate groups
- source-of-truth conflicts
- merge recommendations

## Do Not Do

- do not classify placement from scratch
- do not archive by yourself
- do not generate docs_readable output
