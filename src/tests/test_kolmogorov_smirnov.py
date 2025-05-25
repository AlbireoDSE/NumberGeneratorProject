import os
import sys

sys.path.insert(1, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))

import unittest
import numpy as np
from rng_tests.kolmogorov_smirnov import KolmogorovSmirnov

class TestKolmogorovSmirnov(unittest.TestCase):
    
    def test_compute_uniform_distribution(self):
        alpha = 0.05
        data = np.linspace(0, 1, 100).tolist()
        ks_stat = KolmogorovSmirnov.compute(data = data, save_plot = False)
        critical_value = KolmogorovSmirnov.compute_critical_value(1 - alpha, len(data))
        self.assertLessEqual(ks_stat, critical_value)

    def test_compute_non_uniform_distribution(self):
        alpha = 0.05
        data = [0.1]*25 + [0.2]*50 + [0.3]*5 + [0.8]*10 + [0.9]*5 + [0.95]*5
        ks_stat = KolmogorovSmirnov.compute(data = data, save_plot = False)
        critical_value = KolmogorovSmirnov.compute_critical_value(1 - alpha, len(data))
        self.assertGreater(ks_stat, critical_value)
    
if __name__ == "__main__":
    unittest.main()