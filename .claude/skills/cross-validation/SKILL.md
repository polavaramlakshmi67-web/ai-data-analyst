---
name: cross-validation
description: Set up cross-validation correctly for the data structure at hand.
---

# Cross Validation

Set up cross-validation correctly for the data structure at hand.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: set up cross-validation correctly for the data structure at hand.

## Procedure
- Use k-fold for i.i.d. tabular data; use time-series split (no shuffling) for temporal data.
- Use grouped CV when rows from the same entity must not leak across folds.
- Report the mean and spread (std) of CV scores, not just the mean.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
