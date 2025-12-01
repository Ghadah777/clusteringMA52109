import sys
import os
import pandas as pd
from cluster_maker.data_analyser import summarise_numeric
#from cluster_maker.data_exporter import export_summary as exp_sum

OUTPUT_DIR = "demo_output"


def main(args):
    print("=== cluster_maker: CSV Analysis Demo ===\n")

    # Check number of arguments
    if len(args) != 2:
        print("ERROR: Incorrect number of arguments.")
        print("Usage: python demo/analyse_from_csv.py path/to/input.csv")
        return

    input_path = args[1]
    print(f"Input CSV file: {input_path}")

    if not os.path.exists(input_path):
        print(f"ERROR: File '{input_path}' does not exist.")
        return

    # Load CSV
    print("Reading CSV file...")
    df = pd.read_csv(input_path)
    print("CSV loaded successfully.\n")

    # Analyse data
    print("Running numeric summary analysis...")
    summary = summarise_numeric(df)
    print("Summary computed.\n")

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Output paths
    csv_out = os.path.join(OUTPUT_DIR, "numeric_summary.csv")
    txt_out = os.path.join(OUTPUT_DIR, "numeric_summary.txt")

    # Export
    print("Exporting summary to files...")
    # Save summary to CSV
    summary.to_csv(csv_out, index=True)

    # Save summary to text file
    with open(txt_out, 'w') as f:
        f.write("Summary Statistics\n")
        f.write("=" * 50 + "\n\n")
        f.write(summary.to_string())

    print(f"Summary saved to {csv_out}")
    print(f"Text summary saved to {txt_out}")
    print("Summary exported successfully:")
    print(f" - {csv_out}")
    print(f" - {txt_out}")

    print("\n=== End of analysis ===")

if __name__ == "__main__":
    main(sys.argv)