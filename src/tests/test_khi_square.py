import os, sys

sys.path.insert(1, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))


import unittest
import numpy as np

from rng_tests.khi_square import KhiSquareTest
from utilities.histogram import Histogram

class TestKhiSquare(unittest.TestCase):
    
    def test_compute_uniform_distribution(self):
        num_interval = 10
        histogram = Histogram(data = np.linspace(0, 1, 100).tolist(), num_interval = num_interval)
        expected = [histogram.mean] * num_interval
        chi_square = KhiSquareTest.compute(observed = histogram.observed, expected = expected)
        self.assertLessEqual(chi_square, 0.1)

    def test_compute_non_uniform_distribution(self):
        num_interval = 10
        histogram = Histogram(data = [0.1,0.1,0.1,0.5,0.6,0.6,0.7,0.9], num_interval = num_interval)
        expected = [histogram.mean] * num_interval
        chi_square = KhiSquareTest.compute(observed = histogram.observed, expected = expected)
        self.assertGreater(chi_square, 0.1)
    
    
if __name__ == "__main__":
    unittest.main()