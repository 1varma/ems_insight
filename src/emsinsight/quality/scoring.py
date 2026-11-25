"""Documentation-quality scoring (Phase 1 core).

Approach
- Completeness: share of required elements present (not null, not a Not Value).
- Consistency: rule checks across fields, e.g. arrival time after dispatch time,
  a cardiac-arrest impression with a matching procedure recorded.
- Record score = weighted mix of the two; flag records below quality.min_record_score.
- Keep rules declarative (a list of named checks) so a medical director can review them.
"""
from collections.abc import Iterable

import pandas as pd


def completeness(df: pd.DataFrame, required: Iterable[str]) -> pd.Series:
    """Fraction of required columns that are non-null for each row."""
    cols = [c for c in required if c in df.columns]
    if not cols:
        return pd.Series(0.0, index=df.index)
    return df[cols].notna().mean(axis=1)


def consistency(df: pd.DataFrame) -> pd.DataFrame:
    """Return one boolean column per consistency rule (True = passes). TODO: add rules."""
    raise NotImplementedError
