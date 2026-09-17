---
name: dedup-fuzzy-matching
description: Find near-duplicate records (typos, formatting differences) using fuzzy string matching.
---

# Dedup Fuzzy Matching

Find near-duplicate records (typos, formatting differences) using fuzzy string matching.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: find near-duplicate records (typos, formatting differences) using fuzzy string matching.

## Procedure
- Normalize case/whitespace/punctuation before comparing strings.
- Use token-sort or Levenshtein-based similarity with a stated threshold.
- Always show matched pairs with their similarity score before merging.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
