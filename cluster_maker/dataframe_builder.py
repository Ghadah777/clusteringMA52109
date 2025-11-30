from __future__ import annotations

from typing import List, Dict, Any, Sequence
import numpy as np
import pandas as pd


def define_dataframe_structure(column_specs: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Define a seed DataFrame with one row per cluster and one column per feature.
    """
    if not column_specs:
        raise ValueError("column_specs must be a non-empty list of dictionaries.")

    # Check equal length of reps
    reps_lengths = [len(spec.get("reps", [])) for spec in column_specs]
    if len(set(reps_lengths)) != 1:
        raise ValueError("All 'reps' lists must have the same length.")

    data = {}
    for spec in column_specs:
        name = spec.get("name")
        reps = spec.get("reps")

        if name is None or reps is None:
            raise ValueError("Each entry must have 'name' and 'reps'.")
        if not isinstance(reps, Sequence):
            raise TypeError("'reps' must be a sequence.")

        # reps are rows → correct orientation
        data[name] = list(reps)

    # CORRECT: rows = clusters, columns = features
    return pd.DataFrame(data)


def simulate_data(
    seed_df: pd.DataFrame,
    n_points: int = 100,
    cluster_std: float | str = "1.0",
    random_state: int | None = None,
) -> pd.DataFrame:

    if n_points <= 0:
        raise ValueError("n_points must be a positive integer.")

    # FIX: convert string → float BEFORE comparing
    cluster_std = float(cluster_std)
    if cluster_std <= 0:
        raise ValueError("cluster_std must be positive.")

    rng = np.random.RandomState(random_state)

    centres = seed_df.to_numpy(dtype=float)
    n_clusters, n_features = centres.shape

    # even distribution of points
    base = n_points // n_clusters
    remainder = n_points % n_clusters
    counts = np.full(n_clusters, base, dtype=int)
    counts[:remainder] += 1

    records = []

    for cid, (centre, count) in enumerate(zip(centres, counts)):
        noise = rng.normal(0, cluster_std, size=(count, n_features))
        points = centre + noise
        for point in points:
            rec = {col: val for col, val in zip(seed_df.columns, point)}
            rec["true_cluster"] = cid
            records.append(rec)

    return pd.DataFrame.from_records(records)
