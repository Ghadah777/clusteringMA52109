###
## cluster_maker
## James Foadi - University of Bath
## November 2025
###

from __future__ import annotations
import pandas as pd


def calculate_descriptive_statistics(data: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")
    return data.describe()


def calculate_correlation(data: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")
    return data.corr(numeric_only=True)


def summarise_numeric(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return summary statistics for each numeric column.
    Includes: mean, std, min, max, n_missing.
    Ignores non-numeric columns.
    """
    numeric_cols = df.select_dtypes(include="number")

    if numeric_cols.empty:
        raise ValueError("No numeric columns found in DataFrame.")

    summary = {
        "mean": numeric_cols.mean(),
        "std": numeric_cols.std(),
        "min": numeric_cols.min(),
        "max": numeric_cols.max(),
        "n_missing": numeric_cols.isna().sum(),
    }

    return pd.DataFrame(summary)
