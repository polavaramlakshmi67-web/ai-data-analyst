---
name: feature-engineering-patterns
description: Create informative model features without introducing leakage.
---

# Feature Engineering Patterns

Create informative model features without introducing leakage.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: create informative model features without introducing leakage.

## Procedure
- Derive time-based features (day-of-week, recency) explicitly rather than leaving raw timestamps.
- Check that no feature encodes information from the future relative to the prediction point.
- Cap/encode rare categorical levels ('other' bucket) to avoid overfitting on sparse categories.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
