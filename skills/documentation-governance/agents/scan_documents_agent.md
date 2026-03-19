# Scan Documents Agent

## Responsibility

Scan the repository markdown tree and report structure facts only.

## Input

- project root
- optional governance config

## Output

- file inventory
- docs/docs_readable presence
- category counts
- forbidden filename findings

## Do Not Do

- do not classify merge actions
- do not propose deduplication
- do not generate readable summaries
