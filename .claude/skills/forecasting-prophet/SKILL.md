---
name: forecasting-prophet
description: Build forecasts with Prophet or similar decomposable trend+seasonality models.
---

# Forecasting Prophet

Build forecasts with Prophet or similar decomposable trend+seasonality models.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: build forecasts with Prophet or similar decomposable trend+seasonality models.

## Procedure
- Configure known seasonality (weekly/yearly) and holidays explicitly rather than relying on defaults.
- Backtest with a rolling-origin evaluation, not a single train/test split.
- Communicate uncertainty intervals, and note they widen quickly beyond the training horizon.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
