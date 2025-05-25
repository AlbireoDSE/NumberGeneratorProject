import os
import sys

sys.path.insert(1, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))

import unittest
import numpy as np
from rng_tests.khi_square import KhiSquareTest
from utilities.histogram import Histogram

class TestKhiSquare(unittest.TestCase):
    
    def test_compute_uniform_distribution(self):
        num_interval = 10
        alpha = 0.05
        histogram = Histogram(data = np.linspace(0, 1, 100).tolist(), num_interval = num_interval)
        expected = [histogram.mean] * num_interval
        chi_square = KhiSquareTest.compute(observed = histogram.observed, expected = expected)
        critical_value = KhiSquareTest.compute_critical_value(alpha, num_interval - 1)
        self.assertLessEqual(chi_square, critical_value)

    def test_compute_non_uniform_distribution(self):
        num_interval = 10
        alpha = 0.05
        histogram = Histogram(data = np.clip(np.random.normal(loc = 0.5, scale = 0.15, size = 100), 0.0, 1.0).tolist(), num_interval = num_interval)
        expected = [histogram.mean] * num_interval
        chi_square = KhiSquareTest.compute(observed = histogram.observed, expected = expected)
        critical_value = KhiSquareTest.compute_critical_value(alpha, num_interval - 1)
        self.assertGreater(chi_square, critical_value)
    
if __name__ == "__main__":
    unittest.main()