# cluster_maker — Package Overview and Main Components

**cluster_maker** is a lightweight educational Python package designed for the MA52109 Programming for Data Science practical exam. It provides a complete and fully modular workflow for:

- generating synthetic clustered datasets  
- preprocessing and selecting features  
- running clustering algorithms (K-Means)  
- evaluating cluster quality  
- producing visualisations  
- exporting summaries  
- extending the workflow with PCA dimensionality reduction (Task 6)

The package uses only: **NumPy, pandas, matplotlib, SciPy, scikit-learn, and the Python standard library.**

---

## 1. Package Structure

cluster_maker/
│
├── dataframe_builder.py
├── data_analyser.py
├── data_exporter.py
├── preprocessing.py
├── algorithms.py
├── evaluation.py
├── plotting_clustered.py
├── interface.py
└── init.py

Each module is independent, making the package highly testable and ideal for debugging/extension tasks.

---

## 2. Data Generation (dataframe_builder.py)

Tools for creating synthetic data suitable for clustering.

### Key functions:
- **define_dataframe_structure(cols)**  
  Creates a structured empty DataFrame for numeric features.

- **simulate_data(n_samples, n_features, n_clusters, random_state)**  
  Generates synthetic data by sampling around randomly chosen centroids using Gaussian noise.  
  Includes a `true_cluster` label for evaluation.

---

## 3. Data Analysis (data_analyser.py)

Provides statistical tools for exploring numeric datasets.

### Key functions:
- **calculate_descriptive_statistics(df)**  
  Computes standard statistics (mean, std, min, max, quantiles).

- **calculate_correlation(df)**  
  Returns a numeric correlation matrix.

- **summarize_numeric_columns(df)** *(Task 3)*  
  Returns a clean summary table for each numeric column including:  
  mean, std, min, max, and number of missing values.  
  Used extensively in the Task 4 demo script.

---

## 4. Data Export (data_exporter.py)

Handles exporting DataFrames and summary outputs.

### Key functions:
- **export_to_csv(df, filename)**  
  Saves a DataFrame to CSV.

- **export_formatted(df, filename)**  
  Saves a readable plain-text table.

- **export_summary(summary_df, csv_path, txt_path)** *(Task 3)*  
  Exports the numeric summary to both:
  - a CSV file  
  - a human-readable text file  

---

## 5. Preprocessing (preprocessing.py)

Tools used before clustering.

### Key functions:
- **select_features(df, feature_cols)**  
  Extracts specified numeric columns.

- **standardise_features(X)**  
  Applies zero-mean/unit-variance scaling.

- **apply_pca(X, n_components)** *(Task 6 Extension)*  
  Performs PCA dimensionality reduction and returns the transformed features.

---

## 6. Algorithms (algorithms.py)

Implements clustering operations.

### Key functions:
- **run_kmeans(X, k, random_state)**  
  Wrapper around scikit-learn’s KMeans.

- Educational manual implementation (used for teaching):
  - init_centroids  
  - assign_clusters  
  - update_centroids  
  - kmeans  

---

## 7. Evaluation (evaluation.py)

Provides metrics for assessing cluster quality.

### Key functions:
- **compute_inertia(model)**  
  Returns the within-cluster sum of squares.

- **compute_silhouette(X, labels)**  
  Measures cluster separation quality.

- Supports the elbow method via repeated K-Means evaluations.

---

## 8. Plotting (plotting_clustered.py)

Creates visualisations.

### Key functions:
- **plot_clusters(X, labels)**  
  2D scatter plot displaying cluster assignments.

- **plot_elbow(k_values, inertias)**  
  Visualises inertia for different k values to help pick an optimal number of clusters.

---

## 9. High-Level Interface (interface.py)

The main pipeline used by students and demo scripts.

### **run_clustering(...)** performs:

1. Load input CSV  
2. Select required numeric features  
3. Standardise features  
4. *(Optional)* Apply PCA (Task 6)  
5. Run K-Means  
6. Compute metrics (inertia + silhouette)  
7. *(Optional)* Generate elbow plot  
8. Return all results in a structured dictionary  

It centralises all major components of the package.

---

## 10. Demo Scripts (demo/)

### cluster_analysis.py  
Performs a full clustering workflow: reading data, selecting features, clustering, evaluating, plotting, and exporting.

### analyse_from_csv.py *(Task 4)*  
Takes a single CSV file as input and:

- computes numeric summaries  
- exports both CSV and text summary files  
- handles errors gracefully with clear usage messages  
- writes output to the `demo_output/` folder  

---

## 11. Tests (tests/)

Full test coverage is included:

- Data simulation  
- DataFrame structure  
- Numeric summary function *(Task 3)*  
- Export functions *(Task 5)*  
- run_clustering error handling *(Task 5)*  
- PCA functionality *(Task 6)*  

All tests pass using:
pytest -v


---

## 12. PCA Extension (Task 6)

The extension introduces optional PCA before clustering.

### Additions include:
- **apply_pca()** in preprocessing.py  
- New parameters in run_clustering:
  - `use_pca=True/False`
  - `pca_components=<int>`
- Automatic integration after standardisation  
- A dedicated unit test to ensure dimensionality reduction works correctly  

This extension improves flexibility and reflects common real-world clustering workflows.

---

## 13. Conclusion

**cluster_maker** is a clean, modular, fully-tested educational package demonstrating an end-to-end clustering pipeline:

data simulation → preprocessing → clustering → evaluation → plotting → exporting.

The implementation includes all enhancements required for Tasks 1–6, making the package complete, organised, and ready for assessment.
