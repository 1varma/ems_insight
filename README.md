# EMS Insight

Analytics for emergency medical services, starting in upstate New York. The software takes the NEMSIS patient care reports that ambulance crews already file, joins them with hospital and geographic data, and turns them into insights.

## What it does (target)

| Module | User | Output |
|---|---|---|
| `quality` | Medical directors, billing teams | Per-record documentation completeness and protocol-compliance flags (stroke, STEMI, etc.) |
| `features` + `models` | Emergency managers | Call-volume and hotspot forecasts by area and hour |
| `models` + `api` | Hospital EDs | Pre-arrival risk score (admit / ICU / readmission risk) |

## Phase 1 (now): documentation-quality demo

Built only on de-identified public data. No PHI.

1. Load the NEMSIS Public-Release Research Dataset (`ingest`)
2. Score each record for missing or inconsistent required elements (`quality`)
3. Summarize quality by element, call type, and month (notebook + dashboard)

## Data sources

See [docs/data_sources.md](docs/data_sources.md). Raw data never goes in git; `data/` is gitignored.

## Layout

```
config/            settings.yaml – paths, element lists, thresholds
data/raw|interim|processed   local only, gitignored
docs/              roadmap, data sources, compliance notes
notebooks/         exploration
src/emsinsight/
  ingest/          load + standardize NEMSIS / SPARCS files
  quality/         documentation-quality rules and scoring
  features/        time, location, call-type features
  models/          forecasting and risk models
  api/             FastAPI service for scores
tests/
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
