import unittest
import numpy as np

from rng_tests.kolmogorov_smirnov import KolmogorovSmirnov

class TestKolmogorovSmirnov(unittest.TestCase):
    
    def test_compute_uniform_distribution(self):
        data = np.linspace(0, 1, 100).tolist()
        ks_stat = KolmogorovSmirnov.compute(data, save_plot = False)
        self.assertIsInstance(ks_stat, float)
        self.assertLessEqual(ks_stat, 0.1)

    def test_compute_non_uniform_distribution(self):
        data = [0.1,0.1,0.1,0.5,0.6,0.6,0.7,0.9]
        ks_stat = KolmogorovSmirnov.compute(data, save_plot=False)
        self.assertIsInstance(ks_stat, float)
        self.assertGreater(ks_stat, 0.1)
    
    
if __name__ == "__main__":
    unittest.main()