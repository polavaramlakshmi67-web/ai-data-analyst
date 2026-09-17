---
name: hyperparameter-tuning
description: Tune model hyperparameters without overfitting to the validation set.
---

# Hyperparameter Tuning

Tune model hyperparameters without overfitting to the validation set.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: tune model hyperparameters without overfitting to the validation set.

## Procedure
- Use cross-validation, not a single validation split, when the dataset is small.
- Search a reasonably bounded grid/random space; log every trial for reproducibility.
- Reserve a final untouched test set that is never used during tuning.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
