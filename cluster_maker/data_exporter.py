###
## cluster_maker
## James Foadi - University of Bath
## November 2025
###

from __future__ import annotations

from typing import Union, TextIO

import pandas as pd


def export_to_csv(
    data: pd.DataFrame,
    filename: str,
    delimiter: str = ",",
    include_index: bool = False,
) -> None:
    """
    Export a DataFrame to CSV.

    Parameters
    ----------
    data : pandas.DataFrame
    filename : str
        Output filename.
    delimiter : str, default ","
    include_index : bool, default False
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")
    data.to_csv(filename, sep=delimiter, index=include_index)


def export_formatted(
    data: pd.DataFrame,
    file: Union[str, TextIO],
    include_index: bool = False,
) -> None:
    """
    Export a DataFrame as a formatted text table.

    Parameters
    ----------
    data : pandas.DataFrame
    file : str or file-like
        Filename or open file handle.
    include_index : bool, default False
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("data must be a pandas DataFrame.")

    table_str = data.to_string(index=include_index)

    if isinstance(file, str):
        with open(file, "w", encoding="utf-8") as f:
            f.write(table_str)
    else:
        file.write(table_str)




def export_summary(
    summary: pd.DataFrame,
    csv_filename: str,
    txt_filename: str,
) -> None:
    """
    Export a numeric summary DataFrame to a CSV file and a simple
    human-readable text report.
    """

    # --- Basic validation ---
    if not isinstance(summary, pd.DataFrame):
        raise TypeError("summary must be a pandas DataFrame.")

    # =============================
    # 1) Export summary to CSV file
    # =============================
    export_to_csv(summary, csv_filename, delimiter=",", include_index=True)

    # =============================
    # 2) Create human-readable text
    # =============================
    lines = []

    for col, row in summary.iterrows():

        # Pick missing value safely (column name may be 'missing' or 'n_missing')
        if "missing" in row.index:
            missing_value = row["missing"]
        else:
            missing_value = row.get("n_missing", 0)

        # Build summary line
        line = (
            f"{col}: "
            f"mean={row['mean']:.3f}, "
            f"std={row['std']:.3f}, "
            f"min={row['min']:.3f}, "
            f"max={row['max']:.3f}, "
            f"missing={int(missing_value)}"
        )
        lines.append(line)

    report = "\n".join(lines)

    with open(txt_filename, "w", encoding="utf-8") as f:
        f.write(report)
