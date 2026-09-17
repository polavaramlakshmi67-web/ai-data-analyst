---
name: time-series-decomposition
description: Decompose a time series into trend, seasonality, and residual components.
---

# Time Series Decomposition

Decompose a time series into trend, seasonality, and residual components.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: decompose a time series into trend, seasonality, and residual components.

## Procedure
- Choose additive vs. multiplicative decomposition based on whether seasonal amplitude scales with the trend.
- Check stationarity (ADF test) before fitting models that assume it.
- Flag structural breaks or regime changes visible in the residual component.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
