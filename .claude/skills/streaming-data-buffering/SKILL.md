---
name: streaming-data-buffering
description: Buffer and window streaming/incremental data safely for batch-style analysis.
---

# Streaming Data Buffering

Buffer and window streaming/incremental data safely for batch-style analysis.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: buffer and window streaming/incremental data safely for batch-style analysis.

## Procedure
- Define a clear window size and slide interval before processing.
- Make writes idempotent so re-processing a window doesn't duplicate records.
- Watch for out-of-order arrival and decide a lateness tolerance.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
