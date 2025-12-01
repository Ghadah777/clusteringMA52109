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

def summarize_numeric_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Summarise each numeric column with mean, std, min, max and number of
    missing values.

    Non-numeric columns are ignored.

    Parameters
    ----------
    data : pandas.DataFrame

    Returns
    -------
    summary : pandas.DataFrame
        Index = column name.
        Columns = ['mean', 'std', 'min', 'max', 'missing'].
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")

    numeric = data.select_dtypes(include="number")
    if numeric.empty:
        raise ValueError("No numeric columns found in the DataFrame.")

    summary_dict = {}
    for col in numeric.columns:
        series = numeric[col]
        summary_dict[col] = {
            "mean": series.mean(),
            "std": series.std(),
            "min": series.min(),
            "max": series.max(),
            "missing": series.isna().sum(),
        }

    summary = pd.DataFrame.from_dict(summary_dict, orient="index")
    summary.index.name = "column"
    return summary


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

def summarize_numeric_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Summarise each numeric column with mean, std, min, max and number of
    missing values.

    Parameters
    ----------
    data : pandas.DataFrame
        Input DataFrame that may contain numeric and non-numeric columns.

    Returns
    -------
    summary : pandas.DataFrame
        A DataFrame where each row corresponds to a numeric column and
        contains summary statistics.
    """

    # Check input type
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")

    # Select only numeric columns
    numeric = data.select_dtypes(include="number")

    # If there are no numeric columns, raise an error
    if numeric.empty:
        raise ValueError("No numeric columns found in the DataFrame.")

    summary_dict = {}

    # Compute statistics for each numeric column
    for col in numeric.columns:
        series = numeric[col]
        summary_dict[col] = {
            "mean": series.mean(),
            "std": series.std(),
            "min": series.min(),
            "max": series.max(),
            "missing": series.isna().sum(),
        }

    # Convert to DataFrame
    summary = pd.DataFrame.from_dict(summary_dict, orient="index")
    summary.index.name = "column"

    return summary
