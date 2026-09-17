---
name: model-training-sklearn
description: Train baseline and improved models with correct evaluation splits.
---

# Model Training Sklearn

Train baseline and improved models with correct evaluation splits.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: train baseline and improved models with correct evaluation splits.

## Procedure
- Always start with a simple baseline (mean/majority-class) to contextualize later scores.
- Split data before any preprocessing that learns from the data (fit scalers on train only).
- Use stratified splits for imbalanced classification targets.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
