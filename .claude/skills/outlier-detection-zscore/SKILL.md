---
name: outlier-detection-zscore
description: Detect outliers using z-score or modified z-score (MAD-based) methods.
---

# Outlier Detection Zscore

Detect outliers using z-score or modified z-score (MAD-based) methods.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: detect outliers using z-score or modified z-score (MAD-based) methods.

## Procedure
- Use standard z-score only when the variable is roughly normal.
- Prefer the MAD-based modified z-score for skewed or heavy-tailed data.
- State the threshold used (commonly |z| > 3) explicitly in the output.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
