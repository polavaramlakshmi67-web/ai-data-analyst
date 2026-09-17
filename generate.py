import os

ROOT = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = os.path.join(ROOT, ".claude", "agents")
SKILLS_DIR = os.path.join(ROOT, ".claude", "skills")

# ---------------------------------------------------------------------------
# 25 SUBAGENTS
# Each: name, category, description (trigger text), tools, model, skills(preload), body
# ---------------------------------------------------------------------------
AGENTS = [
    # Ingestion
    dict(name="csv-loader", cat="Ingestion",
         desc="Use when the user needs to load, parse, or inspect CSV/TSV/Excel files, including messy or malformed ones.",
         tools="Read, Bash, Grep", model="haiku",
         skills=["csv-encoding-detection", "data-type-coercion", "data-sampling-strategies"],
         body="You load tabular files into clean, typed dataframes. Detect encoding and delimiter issues before parsing. Report row/column counts, dtypes, and the first parsing problems you hit. Never silently drop rows."),
    dict(name="database-connector", cat="Ingestion",
         desc="Use when the user needs to query a SQL/NoSQL database, write extraction queries, or pull data from a warehouse.",
         tools="Bash, Read, Grep", model="sonnet",
         skills=["sql-query-patterns", "data-sampling-strategies"],
         body="You write and run safe, read-only queries against the configured database connection. Always LIMIT exploratory queries. Explain the query plan in plain language before running anything expensive."),
    dict(name="api-fetcher", cat="Ingestion",
         desc="Use when the user needs to pull data from a REST/GraphQL API, including paginated or rate-limited endpoints.",
         tools="Bash, Read", model="haiku",
         skills=["api-pagination-handling", "json-flattening"],
         body="You fetch data from external APIs, handle pagination and rate limits gracefully, and flatten nested JSON into analysis-ready tables."),
    dict(name="streaming-ingest", cat="Ingestion",
         desc="Use when the user needs to handle streaming, real-time, or incrementally-arriving data sources.",
         tools="Bash, Read", model="sonnet",
         skills=["streaming-data-buffering", "reproducibility-logging"],
         body="You design ingestion for streaming or incremental data: windowing, buffering, and idempotent writes. Flag any risk of duplicate or out-of-order records."),

    # Cleaning / prep
    dict(name="schema-validator", cat="Cleaning",
         desc="Use when the user needs to validate a dataset's schema, enforce types, or catch structural inconsistencies.",
         tools="Read, Bash", model="haiku",
         skills=["schema-validation-rules", "data-type-coercion"],
         body="You check datasets against expected schemas (column names, types, ranges, nullability) and produce a clear pass/fail report with exact offending rows."),
    dict(name="missing-data-handler", cat="Cleaning",
         desc="Use when the user needs to detect, quantify, or impute missing values in a dataset.",
         tools="Read, Bash", model="sonnet",
         skills=["missing-value-imputation", "eda-summary-statistics"],
         body="You quantify missingness per column, diagnose whether it's MCAR/MAR/MNAR where feasible, and recommend or apply an imputation strategy — always disclosing the trade-offs of the method chosen."),
    dict(name="outlier-detector", cat="Cleaning",
         desc="Use when the user needs to find, explain, or handle outliers/anomalies in numeric data.",
         tools="Read, Bash", model="sonnet",
         skills=["outlier-detection-iqr", "outlier-detection-zscore"],
         body="You detect outliers using multiple methods (IQR, z-score, isolation-forest for multivariate cases), explain why each point was flagged, and never silently delete data without user confirmation."),
    dict(name="deduper", cat="Cleaning",
         desc="Use when the user needs to find and remove exact or fuzzy duplicate records.",
         tools="Read, Bash", model="haiku",
         skills=["dedup-fuzzy-matching"],
         body="You identify exact and fuzzy duplicates (name/address/email variants), show matched pairs with similarity scores, and only merge/drop after the approach is confirmed."),

    # Exploration
    dict(name="eda-summarizer", cat="Exploration",
         desc="Use when the user wants a general exploratory data analysis summary of a new dataset.",
         tools="Read, Bash", model="sonnet",
         skills=["eda-summary-statistics", "distribution-profiling", "pivot-table-generation"],
         body="You produce a structured first-look EDA: shape, dtypes, summary stats, missingness, and the 3-5 most notable patterns worth investigating further."),
    dict(name="correlation-explorer", cat="Exploration",
         desc="Use when the user wants to understand relationships or correlations between variables.",
         tools="Read, Bash", model="sonnet",
         skills=["correlation-analysis"],
         body="You compute pairwise correlations (Pearson/Spearman as appropriate), flag multicollinearity, and always caveat correlation vs causation in your summary."),
    dict(name="distribution-profiler", cat="Exploration",
         desc="Use when the user wants to understand the shape, skew, or spread of variables in a dataset.",
         tools="Read, Bash", model="haiku",
         skills=["distribution-profiling"],
         body="You profile distributions (histograms, skew, kurtosis, normality tests) and note which variables may need transformation before modeling."),
    dict(name="segment-explorer", cat="Exploration",
         desc="Use when the user wants to break data into cohorts/segments and compare them.",
         tools="Read, Bash", model="sonnet",
         skills=["segment-cohort-analysis", "pivot-table-generation"],
         body="You slice data into meaningful cohorts/segments, compare key metrics across them, and highlight the segments that differ most from the overall population."),

    # Statistical analysis
    dict(name="hypothesis-tester", cat="Statistics",
         desc="Use when the user wants to run or interpret a statistical hypothesis test.",
         tools="Read, Bash", model="opus",
         skills=["hypothesis-testing-framework", "chi-square-testing", "t-test-anova"],
         body="You choose the correct statistical test for the question and data type, check assumptions before running it, and report effect size and confidence intervals — not just a p-value."),
    dict(name="time-series-analyst", cat="Statistics",
         desc="Use when the user has time-indexed data and wants trend, seasonality, or decomposition analysis.",
         tools="Read, Bash", model="sonnet",
         skills=["time-series-decomposition"],
         body="You decompose time series into trend/seasonality/residual, check stationarity, and flag structural breaks or regime changes."),
    dict(name="causal-inference-analyst", cat="Statistics",
         desc="Use when the user wants to estimate a causal effect rather than a mere correlation (A/B tests, natural experiments, confounders).",
         tools="Read, Bash", model="opus",
         skills=["causal-inference-methods", "hypothesis-testing-framework"],
         body="You help design or analyze causal questions: identify confounders, pick an appropriate design (RCT, diff-in-diff, IV, matching), and are explicit about what assumptions the causal claim rests on."),

    # Modeling / ML
    dict(name="feature-engineer", cat="Modeling",
         desc="Use when the user needs to create, transform, or select features for a model.",
         tools="Read, Bash", model="sonnet",
         skills=["feature-engineering-patterns", "feature-selection"],
         body="You design features (encodings, interactions, aggregations, time-based features) and check for leakage before anything touches a model."),
    dict(name="model-trainer", cat="Modeling",
         desc="Use when the user wants to train a predictive model (classification, regression, clustering).",
         tools="Read, Bash", model="sonnet",
         skills=["model-training-sklearn", "cross-validation"],
         body="You train baseline and improved models, use proper train/val/test splits or cross-validation, and never report metrics computed on training data as if they were held-out performance."),
    dict(name="model-evaluator", cat="Modeling",
         desc="Use when the user wants to evaluate, compare, or diagnose a trained model's performance.",
         tools="Read, Bash", model="sonnet",
         skills=["model-evaluation-metrics", "cross-validation"],
         body="You evaluate models with task-appropriate metrics, check calibration and error distribution by subgroup, and call out where a model is likely to fail in production."),
    dict(name="forecaster", cat="Modeling",
         desc="Use when the user wants to forecast future values from historical time series data.",
         tools="Read, Bash", model="sonnet",
         skills=["forecasting-prophet", "time-series-decomposition"],
         body="You build forecasts with appropriate uncertainty intervals, backtest against holdout periods, and are explicit about the forecast horizon beyond which confidence drops sharply."),

    # Visualization
    dict(name="chart-builder", cat="Visualization",
         desc="Use when the user wants a specific chart or plot built from data.",
         tools="Read, Bash", model="haiku",
         skills=["plotly-chart-templates", "matplotlib-styling", "color-palette-selection"],
         body="You build the single clearest chart type for the data and question at hand — avoid chart junk, label axes, and never use a pie chart for more than 5 categories."),
    dict(name="dashboard-designer", cat="Visualization",
         desc="Use when the user wants a multi-chart dashboard or interactive data view.",
         tools="Read, Bash", model="sonnet",
         skills=["dashboard-layout-design", "chart-accessibility"],
         body="You lay out dashboards with a clear visual hierarchy (top-level KPIs first, drill-downs after), and keep every dashboard usable on both light and dark backgrounds."),
    dict(name="geo-mapper", cat="Visualization",
         desc="Use when the user wants to visualize geographic or location-based data.",
         tools="Read, Bash", model="haiku",
         skills=["geo-mapping-choropleth"],
         body="You build choropleth/point maps, pick projections appropriate to the region shown, and normalize by population/area where raw counts would mislead."),

    # Reporting
    dict(name="insight-writer", cat="Reporting",
         desc="Use when the user wants findings from an analysis turned into a written narrative.",
         tools="Read", model="sonnet",
         skills=["insight-narrative-writing", "data-storytelling"],
         body="You translate analysis results into a narrative structured as: headline finding, supporting evidence, caveats, and recommended next step — no more than one page unless asked for depth."),
    dict(name="exec-summary-writer", cat="Reporting",
         desc="Use when the user wants a short executive summary of an analysis for non-technical stakeholders.",
         tools="Read", model="sonnet",
         skills=["executive-summary-format", "report-templating"],
         body="You write a 3-5 bullet executive summary: what we found, why it matters, what to do next. No jargon, no methodology detail unless explicitly asked."),

    # QA / governance
    dict(name="data-quality-auditor", cat="Governance",
         desc="Use when the user wants an overall data quality or trustworthiness audit of a dataset or pipeline before it's used for decisions.",
         tools="Read, Bash, Grep", model="opus",
         skills=["data-quality-audit-checklist", "pii-redaction-checklist", "reproducibility-logging"],
         body="You run a full data-quality pass: completeness, consistency, freshness, PII exposure, and reproducibility of the pipeline that produced the data. Produce a pass/fail scorecard with specifics."),
]

assert len(AGENTS) == 25, len(AGENTS)

# ---------------------------------------------------------------------------
# 45 SKILLS  (name, category, one-line description, body bullets)
# ---------------------------------------------------------------------------
SKILLS = [
    # Ingestion (5)
    ("csv-encoding-detection", "Detect file encoding, delimiter, and header row issues before parsing a CSV/TSV file.",
     ["Sniff encoding (utf-8, latin-1, utf-16) before pandas.read_csv to avoid mojibake.",
      "Detect delimiter automatically when it's not a plain comma (csv.Sniffer or explicit check).",
      "Handle files where the header isn't row 0 (metadata rows above the real header).",
      "Report the exact row/column where parsing first breaks, don't just raise a generic error."]),
    ("sql-query-patterns", "Write safe, efficient, read-only SQL for exploratory data extraction.",
     ["Always add LIMIT during exploration; never run unbounded SELECT * on large tables.",
      "Prefer explicit column lists over SELECT *.",
      "Use EXPLAIN before running a query you suspect is expensive.",
      "Parameterize queries — never string-concatenate user input into SQL."]),
    ("api-pagination-handling", "Correctly page through REST/GraphQL API results without missing or duplicating records.",
     ["Detect pagination style: offset/limit, cursor-based, or link-header based.",
      "Respect rate limits with backoff; log how many pages were fetched.",
      "Deduplicate on a stable ID field across pages in case of overlap."]),
    ("json-flattening", "Flatten deeply nested JSON API responses into analysis-ready tabular form.",
     ["Use pandas.json_normalize with explicit record_path/meta rather than manual recursion when possible.",
      "Decide up front how to handle arrays of objects (explode vs. aggregate).",
      "Preserve a reference to the original nested structure in case flattening loses information."]),
    ("streaming-data-buffering", "Buffer and window streaming/incremental data safely for batch-style analysis.",
     ["Define a clear window size and slide interval before processing.",
      "Make writes idempotent so re-processing a window doesn't duplicate records.",
      "Watch for out-of-order arrival and decide a lateness tolerance."]),

    # Cleaning (6)
    ("missing-value-imputation", "Choose and apply an appropriate missing-value imputation strategy.",
     ["Quantify missingness per column before choosing a method.",
      "Prefer model-based or group-mean imputation over global-mean when subgroups differ meaningfully.",
      "Never impute the target variable in a supervised learning setup.",
      "Always flag which rows/columns were imputed for downstream transparency."]),
    ("outlier-detection-iqr", "Detect univariate outliers using the interquartile range method.",
     ["Flag points beyond Q1 - 1.5*IQR or Q3 + 1.5*IQR.",
      "Use a wider multiplier (3.0) for 'extreme outlier' flagging vs. 1.5 for 'mild'.",
      "Always visualize flagged points before removing them."]),
    ("outlier-detection-zscore", "Detect outliers using z-score or modified z-score (MAD-based) methods.",
     ["Use standard z-score only when the variable is roughly normal.",
      "Prefer the MAD-based modified z-score for skewed or heavy-tailed data.",
      "State the threshold used (commonly |z| > 3) explicitly in the output."]),
    ("dedup-fuzzy-matching", "Find near-duplicate records (typos, formatting differences) using fuzzy string matching.",
     ["Normalize case/whitespace/punctuation before comparing strings.",
      "Use token-sort or Levenshtein-based similarity with a stated threshold.",
      "Always show matched pairs with their similarity score before merging."]),
    ("schema-validation-rules", "Define and check schema rules: types, ranges, required columns, referential integrity.",
     ["Encode expected schema as a declarative spec (e.g., pandera/pydantic) rather than ad hoc checks.",
      "Validate ranges/enums for categorical and bounded numeric fields.",
      "Fail loudly with the specific row and rule violated, not a generic error."]),
    ("data-type-coercion", "Safely convert columns to their correct types without silent data loss.",
     ["Check for values that fail coercion (e.g., '12,000' to int) before force-casting.",
      "Preserve original values in a shadow column when coercion is lossy.",
      "Watch for mixed-type columns (numbers stored as strings mixed with real strings)."]),

    # Exploration (6)
    ("eda-summary-statistics", "Produce a structured first-look summary of a new dataset.",
     ["Report shape, dtypes, missingness %, and summary stats (mean/median/std/min/max) per column.",
      "Call out columns with a single dominant value (near-zero variance).",
      "Surface the 3-5 most surprising findings, not just a raw stats dump."]),
    ("correlation-analysis", "Compute and interpret pairwise correlations between variables.",
     ["Use Pearson for linear relationships, Spearman for monotonic/non-normal ones.",
      "Flag multicollinearity (|r| > 0.8) before it goes into a model.",
      "Always state correlation is not causation in the summary."]),
    ("distribution-profiling", "Characterize the shape, skew, and spread of numeric variables.",
     ["Report skewness/kurtosis alongside a histogram or KDE description.",
      "Run a normality test (Shapiro-Wilk for small n, D'Agostino for larger n).",
      "Recommend a transformation (log, Box-Cox) when skew is severe."]),
    ("segment-cohort-analysis", "Break a dataset into meaningful cohorts/segments and compare metrics across them.",
     ["Choose segment boundaries that are meaningful to the business question, not arbitrary quantiles.",
      "Report sample size per segment — flag segments too small to trust.",
      "Highlight the segments that diverge most from the overall average."]),
    ("pivot-table-generation", "Build pivot/cross-tab summaries to compare metrics across categorical dimensions.",
     ["Choose the right aggregation (sum/mean/count) for the metric's meaning.",
      "Watch for Simpson's paradox when aggregating across an uneven-sized dimension.",
      "Keep pivot tables to 2 dimensions max for human readability; use faceting beyond that."]),
    ("data-sampling-strategies", "Sample large datasets for fast, representative exploration.",
     ["Use stratified sampling when class/segment balance matters.",
      "State the sample size and method used so findings can be validated on the full dataset later.",
      "Avoid sampling entirely for rare-event analysis (e.g., fraud) — use all positives."]),

    # Statistics (6)
    ("hypothesis-testing-framework", "Choose the correct statistical test and interpret results rigorously.",
     ["Match test to data type and design: t-test (2 groups, continuous), ANOVA (3+ groups), chi-square (categorical).",
      "Check test assumptions (normality, variance homogeneity, independence) before trusting the result.",
      "Report effect size and confidence interval, not just a p-value.",
      "Correct for multiple comparisons when running many tests at once."]),
    ("chi-square-testing", "Test independence or goodness-of-fit for categorical data.",
     ["Ensure expected cell counts are >=5 before trusting the chi-square approximation.",
      "Use Fisher's exact test instead for small samples or 2x2 tables with low counts.",
      "Report Cramer's V as an effect size alongside the p-value."]),
    ("t-test-anova", "Compare means between two or more groups.",
     ["Check variance homogeneity (Levene's test) to choose Student's vs. Welch's t-test.",
      "Use ANOVA for 3+ groups, followed by a post-hoc test (Tukey HSD) for pairwise differences.",
      "Report the effect size (Cohen's d or eta-squared), not just significance."]),
    ("time-series-decomposition", "Decompose a time series into trend, seasonality, and residual components.",
     ["Choose additive vs. multiplicative decomposition based on whether seasonal amplitude scales with the trend.",
      "Check stationarity (ADF test) before fitting models that assume it.",
      "Flag structural breaks or regime changes visible in the residual component."]),
    ("arima-forecasting", "Fit ARIMA/SARIMA models for time series forecasting.",
     ["Use ACF/PACF plots (or auto_arima) to select (p,d,q) orders.",
      "Difference the series only as much as needed to achieve stationarity.",
      "Backtest on a holdout period before trusting forecast intervals."]),
    ("causal-inference-methods", "Select and apply a causal inference design appropriate to the available data.",
     ["Use randomized A/B test results directly when available — it's the gold standard.",
      "For observational data, consider diff-in-diff, instrumental variables, or matching depending on the confounding structure.",
      "Explicitly state the identifying assumption the causal claim depends on."]),

    # Modeling (7)
    ("feature-engineering-patterns", "Create informative model features without introducing leakage.",
     ["Derive time-based features (day-of-week, recency) explicitly rather than leaving raw timestamps.",
      "Check that no feature encodes information from the future relative to the prediction point.",
      "Cap/encode rare categorical levels ('other' bucket) to avoid overfitting on sparse categories."]),
    ("feature-selection", "Select the most predictive, non-redundant features for a model.",
     ["Remove near-zero-variance and highly collinear features before modeling.",
      "Prefer model-based importance (permutation importance) over raw correlation for selection.",
      "Re-validate feature importance on a held-out set, not training data."]),
    ("model-training-sklearn", "Train baseline and improved models with correct evaluation splits.",
     ["Always start with a simple baseline (mean/majority-class) to contextualize later scores.",
      "Split data before any preprocessing that learns from the data (fit scalers on train only).",
      "Use stratified splits for imbalanced classification targets."]),
    ("hyperparameter-tuning", "Tune model hyperparameters without overfitting to the validation set.",
     ["Use cross-validation, not a single validation split, when the dataset is small.",
      "Search a reasonably bounded grid/random space; log every trial for reproducibility.",
      "Reserve a final untouched test set that is never used during tuning."]),
    ("model-evaluation-metrics", "Choose and report the right performance metrics for the task.",
     ["Use precision/recall/F1 (not accuracy) for imbalanced classification.",
      "Use RMSE/MAE/MAPE appropriately depending on whether large errors should be penalized more.",
      "Break down metrics by important subgroups to catch uneven performance."]),
    ("cross-validation", "Set up cross-validation correctly for the data structure at hand.",
     ["Use k-fold for i.i.d. tabular data; use time-series split (no shuffling) for temporal data.",
      "Use grouped CV when rows from the same entity must not leak across folds.",
      "Report the mean and spread (std) of CV scores, not just the mean."]),
    ("forecasting-prophet", "Build forecasts with Prophet or similar decomposable trend+seasonality models.",
     ["Configure known seasonality (weekly/yearly) and holidays explicitly rather than relying on defaults.",
      "Backtest with a rolling-origin evaluation, not a single train/test split.",
      "Communicate uncertainty intervals, and note they widen quickly beyond the training horizon."]),

    # Visualization (6)
    ("plotly-chart-templates", "Build clear, interactive charts with Plotly for common analysis needs.",
     ["Pick chart type by relationship: line for trend, bar for comparison, scatter for correlation.",
      "Label axes and units always; add a title stating the takeaway, not just the variable names.",
      "Avoid dual y-axes unless absolutely necessary — they're easy to misread."]),
    ("matplotlib-styling", "Produce clean, publication-quality static charts with Matplotlib.",
     ["Remove chart junk: unnecessary gridlines, 3D effects, redundant legends.",
      "Use a consistent, colorblind-safe palette across a report's charts.",
      "Set explicit figure size and DPI for print/export quality."]),
    ("dashboard-layout-design", "Lay out multi-chart dashboards with clear visual hierarchy.",
     ["Put the most important KPI top-left where eyes land first.",
      "Group related charts and use consistent axis scales for comparability.",
      "Limit a single dashboard view to 5-7 charts to avoid overload."]),
    ("geo-mapping-choropleth", "Build geographic choropleth or point maps correctly.",
     ["Normalize by population/area for choropleths — raw counts mislead by region size.",
      "Choose a projection appropriate to the region shown (not always Mercator).",
      "Use a sequential palette for continuous values, categorical palette for discrete regions."]),
    ("color-palette-selection", "Choose color palettes that are accurate, accessible, and appropriate to the data type.",
     ["Use sequential palettes for ordered/continuous data, qualitative palettes for categories.",
      "Check palettes for colorblind-safety (avoid red-green as the only distinguishing cue).",
      "Keep a consistent palette for the same variable across all charts in a report."]),
    ("chart-accessibility", "Make charts usable for colorblind users and screen readers.",
     ["Add patterns/shapes in addition to color when color is the only encoding.",
      "Include descriptive alt text or a text summary alongside visual charts.",
      "Ensure sufficient contrast between chart elements and background in both light and dark mode."]),

    # Reporting (5)
    ("executive-summary-format", "Write a short, non-technical summary of an analysis for decision-makers.",
     ["Lead with the finding and the recommended action, not the methodology.",
      "Keep it to 3-5 bullets; push detail to an appendix if needed.",
      "State the confidence level and key caveat in one line each."]),
    ("insight-narrative-writing", "Turn analysis results into a clear written narrative.",
     ["Structure as: headline finding -> supporting evidence -> caveats -> next step.",
      "Use plain language for statistical concepts (say 'no meaningful difference' not just 'p > 0.05').",
      "Quantify impact in business terms (revenue, users, time) wherever possible."]),
    ("data-storytelling", "Sequence findings into a narrative arc that builds toward a conclusion.",
     ["Order findings from context -> tension (the problem found) -> resolution (the recommendation).",
      "Use one visual per key point rather than dumping all charts at once.",
      "End with a clear, specific call to action."]),
    ("report-templating", "Produce consistently formatted analysis reports.",
     ["Use a fixed section order: summary, methodology, findings, limitations, recommendations.",
      "Keep formatting consistent (heading levels, number formatting) across report versions.",
      "Version and date every report for traceability."]),
    ("citation-and-sourcing", "Track and cite the data sources and methods behind every claim in a report.",
     ["Record the exact source table/query/API endpoint behind each figure quoted.",
      "Note the data's as-of date/freshness in the report.",
      "Flag any figure derived from a sample vs. the full population."]),

    # Governance (4)
    ("pii-redaction-checklist", "Identify and redact personally identifiable information before analysis or sharing.",
     ["Scan for direct identifiers (name, email, phone, SSN) and quasi-identifiers (zip+birthdate+gender).",
      "Redact or hash identifiers before data leaves a secure environment.",
      "Confirm aggregation thresholds (e.g., k-anonymity) before publishing grouped results."]),
    ("data-quality-audit-checklist", "Run a systematic data quality audit before a dataset is used for decisions.",
     ["Check completeness, consistency, timeliness, and accuracy dimensions explicitly.",
      "Score each dimension and give an overall pass/fail with specific failing examples.",
      "Re-run the audit whenever the upstream pipeline changes."]),
    ("reproducibility-logging", "Ensure an analysis can be reproduced from raw data to final result.",
     ["Log the exact data snapshot/version and code version used for any reported number.",
      "Pin library versions and random seeds for any stochastic step.",
      "Keep a run log mapping each report figure back to the script/query that produced it."]),
    ("versioning-datasets", "Track dataset versions so analyses remain reproducible as data changes.",
     ["Snapshot or hash datasets at the point of analysis rather than pointing at a live, mutable source.",
      "Record schema changes between versions explicitly.",
      "Tag which dataset version each model or report was built on."]),
]

assert len(SKILLS) == 45, len(SKILLS)

AGENT_TEMPLATE = """---
name: {name}
description: {desc}
tools: {tools}
model: {model}
skills: [{skills}]
---

# {title}

Category: {cat}

{body}

## Working style
- State assumptions explicitly before proceeding on ambiguous requests.
- Return a concise result to the orchestrator: what you did, what you found, and what (if anything) needs human review.
- Prefer preloaded skills for procedure; use the Skill tool to pull in others as needed.
"""

SKILL_TEMPLATE = """---
name: {name}
description: {desc}
---

# {title}

{desc}

## When to use this skill
Use this whenever a subagent or the orchestrator needs to: {desc_lower}

## Procedure
{bullets}

## References
Put deeper reference material, code templates, or example datasets in `references/`, `scripts/`, or `assets/` alongside this file as this skill grows past a quick checklist.
"""

def title_case(slug):
    return " ".join(w.capitalize() for w in slug.split("-"))

os.makedirs(AGENTS_DIR, exist_ok=True)
os.makedirs(SKILLS_DIR, exist_ok=True)

for a in AGENTS:
    skills_str = ", ".join(a["skills"])
    content = AGENT_TEMPLATE.format(
        name=a["name"], desc=a["desc"], tools=a["tools"], model=a["model"],
        skills=skills_str, title=title_case(a["name"]), cat=a["cat"], body=a["body"]
    )
    with open(os.path.join(AGENTS_DIR, a["name"] + ".md"), "w") as f:
        f.write(content)

for name, desc, bullets in SKILLS:
    skill_dir = os.path.join(SKILLS_DIR, name)
    os.makedirs(skill_dir, exist_ok=True)
    for sub in ("references", "scripts", "assets"):
        os.makedirs(os.path.join(skill_dir, sub), exist_ok=True)
        with open(os.path.join(skill_dir, sub, ".gitkeep"), "w") as f:
            f.write("")
    bullet_str = "\n".join(f"- {b}" for b in bullets)
    content = SKILL_TEMPLATE.format(
        name=name, desc=desc, title=title_case(name),
        desc_lower=desc[0].lower() + desc[1:], bullets=bullet_str
    )
    with open(os.path.join(skill_dir, "SKILL.md"), "w") as f:
        f.write(content)

print(f"Generated {len(AGENTS)} agents and {len(SKILLS)} skills.")
