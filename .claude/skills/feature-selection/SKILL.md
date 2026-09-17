---
name: feature-selection
description: Select the most predictive, non-redundant features for a model.
---

# Feature Selection

Select the most predictive, non-redundant features for a model.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: select the most predictive, non-redundant features for a model.

## Procedure
- Remove near-zero-variance and highly collinear features before modeling.
- Prefer model-based importance (permutation importance) over raw correlation for selection.
- Re-validate feature importance on a held-out set, not training data.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
