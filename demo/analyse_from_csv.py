#!/usr/bin/env python
"""
Demo script: analyse_from_csv.py

Usage:
    python demo/analyse_from_csv.py path/to/input.csv
"""

from __future__ import annotations
import sys
import os
import pandas as pd

from cluster_maker.data_analyser import summarize_numeric_columns
from cluster_maker.data_exporter import export_summary


def main(argv=None) -> int:
    # Use command-line arguments if not provided
    if argv is None:
        argv = sys.argv

    # Expect exactly 2 arguments: script + CSV file path
    if len(argv) != 2:
        script_name = os.path.basename(argv[0])
        print("ERROR: expected exactly one argument (CSV file path).")
        print(f"Usage: python demo/{script_name} path/to/input.csv")
        return 1

    input_path = argv[1]

    # Check if file exists
    if not os.path.exists(input_path):
        print(f"ERROR: File '{input_path}' does not exist.")
        return 1

    print(f"Reading CSV file: {input_path}")
    try:
        df = pd.read_csv(input_path)
    except Exception as exc:
        print(f"ERROR: Could not read CSV file: {exc}")
        return 1

    print("Computing numeric summary...")
    try:
        summary = summarize_numeric_columns(df)
    except Exception as exc:
        print(f"ERROR: Cannot compute summary: {exc}")
        return 1

    # Prepare output folder
    os.makedirs("demo_output", exist_ok=True)

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    csv_out = os.path.join("demo_output", f"{base_name}_summary.csv")
    txt_out = os.path.join("demo_output", f"{base_name}_summary.txt")

    print("Saving outputs:")
    print(f"  CSV:  {csv_out}")
    print(f"  TXT:  {txt_out}")

    try:
        export_summary(summary, csv_out, txt_out)
    except Exception as exc:
        print(f"ERROR: Could not export summary files: {exc}")
        return 1

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
