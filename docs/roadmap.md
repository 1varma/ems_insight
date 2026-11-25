# Roadmap

## Phase 1 — Public-data demo (weeks 1–8)
- [ ] Request NEMSIS 2025 Public-Release Research Dataset (nemsis.org → Request Research Data)
- [ ] Download NY SPARCS de-identified discharge data (Health Data NY)
- [ ] `ingest`: load NEMSIS files into DuckDB/Parquet
- [ ] `quality`: rule-based completeness + consistency scoring per record
- [ ] Notebook: quality by element, call type, month
- [ ] Simple dashboard + 2-minute demo video

## Phase 2 — First upstate pilot (months 3–6)
- [ ] Identify 3–5 target upstate county/municipal agencies or regional EMS councils
- [ ] One-page pitch built around the Phase 1 demo
- [ ] Data use agreement + BAA; HIPAA-eligible hosting (AWS/Azure under BAA)
- [ ] Confirm data-sharing process with NYS DOH Bureau of EMS
- [ ] Run quality module on pilot data; review findings with medical director

## Phase 3 — Forecasting and protocol compliance (months 6–12)
- [ ] Call-volume / hotspot forecasting by area and hour
- [ ] Protocol-compliance checks (stroke, STEMI, sepsis) with medical director input

## Phase 4 — Hospital integration (year 2+)
- [ ] Pre-arrival risk score API
- [ ] HL7/FHIR integration path toward Epic/Cerner
