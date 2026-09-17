---
name: csv-encoding-detection
description: Detect file encoding, delimiter, and header row issues before parsing a CSV/TSV file.
---

# Csv Encoding Detection

Detect file encoding, delimiter, and header row issues before parsing a CSV/TSV file.

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: detect file encoding, delimiter, and header row issues before parsing a CSV/TSV file.

## Procedure
- Sniff encoding (utf-8, latin-1, utf-16) before pandas.read_csv to avoid mojibake.
- Detect delimiter automatically when it's not a plain comma (csv.Sniffer or explicit check).
- Handle files where the header isn't row 0 (metadata rows above the real header).
- Report the exact row/column where parsing first breaks, don't just raise a generic error.

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
