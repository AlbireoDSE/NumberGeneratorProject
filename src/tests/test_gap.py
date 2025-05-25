import os
import sys

sys.path.insert(1, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))

import unittest
from rng_tests.gap_test import GapTest
from rng_tests.khi_square import KhiSquareTest
import numpy as np

class TestGap(unittest.TestCase):
    
    def test_gap_uniform_distribution(self):
        alpha = 0.05
        max_gap_size = 10
        
        np.random.seed(0)
        
        chi_square = GapTest.compute(data = np.random.rand(100))

        critical_value = KhiSquareTest.compute_critical_value(alpha, max_gap_size)

        self.assertLessEqual(chi_square, critical_value)

    def test_gap_non_uniform_distribution(self):
        alpha = 0.05
        max_gap_size = 10
        
        chi_square = GapTest.compute(data = np.clip(np.random.normal(loc=0.2, scale=0.1, size=100), 0.0, 1.0).tolist())

        critical_value = KhiSquareTest.compute_critical_value(alpha, max_gap_size)

        self.assertGreater(chi_square, critical_value)
    
if __name__ == "__main__":
    unittest.main()