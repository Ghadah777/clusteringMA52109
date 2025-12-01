import unittest
import numpy as np

from cluster_maker.preprocessing import standardise_features, apply_pca


class TestPCAExtension(unittest.TestCase):
    def test_apply_pca_reduces_dimensions(self):
        rng = np.random.RandomState(0)
        X = rng.normal(size=(50, 5))

        X_scaled = standardise_features(X)
        X_pca = apply_pca(X_scaled, n_components=2)

        self.assertEqual(X_pca.shape, (50, 2))
