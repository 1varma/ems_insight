"""Load the NEMSIS Public-Release Research Dataset.

Design notes
- The release ships as several linked tables keyed by a record ID. Keep them as separate
  Parquet tables in data/interim and join in DuckDB, rather than one wide frame.
- Normalize NEMSIS "Not Values" (not recorded / not applicable) to nulls at load time,
  but keep a flag column so the quality module can tell "blank" from "explicitly not recorded".
"""
from pathlib import Path


def load_table(raw_dir: Path, table: str):
    """Read one NEMSIS table from raw_dir and return a DataFrame. TODO: implement once files arrive."""
    raise NotImplementedError


def to_parquet(raw_dir: Path, interim_dir: Path) -> None:
    """Convert every raw table to Parquet in interim_dir. TODO."""
    raise NotImplementedError
