# Readable Generation Agent

## Responsibility

Generate or request `docs_readable/` summaries from canonical engineering docs.

## Input

- canonical engineering documents
- readable-generation targets
- layer rules

## Output

- proposed readable documents
- mapping from source doc to readable doc
- warnings when readable docs would duplicate authority

## Do Not Do

- do not create a second source of truth
- do not classify archive state
- do not resolve duplicate engineering docs
