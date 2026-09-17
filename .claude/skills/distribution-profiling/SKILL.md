---
name: distribution-profiling
description: Characterize the shape, skew, and spread of numeric variables.
---

# Distribution Profiling

Characterize the shape, skew, and spread of numeric variables.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: characterize the shape, skew, and spread of numeric variables.

## Procedure
- Report skewness/kurtosis alongside a histogram or KDE description.
- Run a normality test (Shapiro-Wilk for small n, D'Agostino for larger n).
- Recommend a transformation (log, Box-Cox) when skew is severe.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
