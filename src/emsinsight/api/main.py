"""Minimal API. Later serves quality scores and risk scores."""
from fastapi import FastAPI

app = FastAPI(title="EMS Insight")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
