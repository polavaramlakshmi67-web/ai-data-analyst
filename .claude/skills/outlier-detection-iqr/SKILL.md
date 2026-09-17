---
name: outlier-detection-iqr
description: Detect univariate outliers using the interquartile range method.
---

# Outlier Detection Iqr

Detect univariate outliers using the interquartile range method.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: detect univariate outliers using the interquartile range method.

## Procedure
- Flag points beyond Q1 - 1.5*IQR or Q3 + 1.5*IQR.
- Use a wider multiplier (3.0) for 'extreme outlier' flagging vs. 1.5 for 'mild'.
- Always visualize flagged points before removing them.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
