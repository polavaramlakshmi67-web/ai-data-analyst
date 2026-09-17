---
name: arima-forecasting
description: Fit ARIMA/SARIMA models for time series forecasting.
---

# Arima Forecasting

Fit ARIMA/SARIMA models for time series forecasting.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: fit ARIMA/SARIMA models for time series forecasting.

## Procedure
- Use ACF/PACF plots (or auto_arima) to select (p,d,q) orders.
- Difference the series only as much as needed to achieve stationarity.
- Backtest on a holdout period before trusting forecast intervals.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
