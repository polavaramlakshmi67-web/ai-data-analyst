---
name: model-evaluation-metrics
description: Choose and report the right performance metrics for the task.
---

# Model Evaluation Metrics

Choose and report the right performance metrics for the task.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: choose and report the right performance metrics for the task.

## Procedure
- Use precision/recall/F1 (not accuracy) for imbalanced classification.
- Use RMSE/MAE/MAPE appropriately depending on whether large errors should be penalized more.
- Break down metrics by important subgroups to catch uneven performance.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
