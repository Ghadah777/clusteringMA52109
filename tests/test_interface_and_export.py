import os
import tempfile
import unittest
import pandas as pd

from cluster_maker.interface import run_clustering
from cluster_maker.data_exporter import export_to_csv, export_formatted


class TestInterfaceRunClustering(unittest.TestCase):

    def test_run_clustering_missing_file(self):
        # File does NOT exist → should raise FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            run_clustering("this_file_does_not_exist.csv", feature_cols=["x", "y"])

    def test_run_clustering_missing_columns(self):
        # Create a temporary CSV file without required feature columns
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "data.csv")
            df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
            df.to_csv(path, index=False)

            # Required feature columns "x", "y" are missing → KeyError
            with self.assertRaises(KeyError):
                run_clustering(path, feature_cols=["x", "y"])


class TestExportFunctions(unittest.TestCase):

    def test_export_to_csv_success(self):
        df = pd.DataFrame({"x": [1, 2, 3]})

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "out.csv")
            export_to_csv(df, path)
            self.assertTrue(os.path.exists(path))  # File must be created

    def test_export_to_csv_invalid_path(self):
        df = pd.DataFrame({"x": [1, 2, 3]})
        invalid_path = os.path.join("non_existing_dir", "out.csv")

        # Should raise *some* exception because directory doesn't exist
        with self.assertRaises(Exception):
            export_to_csv(df, invalid_path)

    def test_export_formatted_success(self):
        df = pd.DataFrame({"x": [1, 2, 3]})

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "table.txt")
            export_formatted(df, path)
            self.assertTrue(os.path.exists(path))

    def test_export_formatted_invalid_path(self):
        df = pd.DataFrame({"x": [1, 2, 3]})
        invalid_path = os.path.join("no_such_folder", "table.txt")

        with self.assertRaises(Exception):
            export_formatted(df, invalid_path)
