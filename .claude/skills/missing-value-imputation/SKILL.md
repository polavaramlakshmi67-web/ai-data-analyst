---
name: missing-value-imputation
description: Choose and apply an appropriate missing-value imputation strategy.
---

# Missing Value Imputation

Choose and apply an appropriate missing-value imputation strategy.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: choose and apply an appropriate missing-value imputation strategy.

## Procedure
- Quantify missingness per column before choosing a method.
- Prefer model-based or group-mean imputation over global-mean when subgroups differ meaningfully.
- Never impute the target variable in a supervised learning setup.
- Always flag which rows/columns were imputed for downstream transparency.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
