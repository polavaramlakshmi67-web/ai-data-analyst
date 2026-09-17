---
name: correlation-analysis
description: Compute and interpret pairwise correlations between variables.
---

# Correlation Analysis

Compute and interpret pairwise correlations between variables.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: compute and interpret pairwise correlations between variables.

## Procedure
- Use Pearson for linear relationships, Spearman for monotonic/non-normal ones.
- Flag multicollinearity (|r| > 0.8) before it goes into a model.
- Always state correlation is not causation in the summary.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
