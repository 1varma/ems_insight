import pandas as pd

from emsinsight.quality.scoring import completeness


def test_completeness_counts_present_fields():
    df = pd.DataFrame({"a": [1, None], "b": [1, 1]})
    assert completeness(df, ["a", "b"]).tolist() == [1.0, 0.5]


def test_completeness_ignores_missing_columns():
    df = pd.DataFrame({"a": [1]})
    assert completeness(df, ["a", "zzz"]).tolist() == [1.0]
