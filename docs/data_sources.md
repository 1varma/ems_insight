# Data sources

| Source | Scope | Contains PHI? | Access |
|---|---|---|---|
| NEMSIS Public-Release Research Dataset | National, 54 states/territories; no patient, agency or hospital identifiers | No | Request form at nemsis.org; single year per request; download link expires |
| NY SPARCS (de-identified) | New York hospital discharges | No (de-identified files) | Health Data NY open data |
| US Census / ACS, TIGER shapefiles | Population, geography | No | Public |
| Pilot agency ePCR data (Phase 2) | One upstate agency | **Yes** | DUA + BAA required; HIPAA hosting only |

Notes
- The public NEMSIS file cannot be relied on to isolate New York; check the data dictionary for retained geography fields.
- Everything in `data/` stays local and out of git.
