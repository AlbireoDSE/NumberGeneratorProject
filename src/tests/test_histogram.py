import os
import sys

sys.path.insert(1, "\\".join(os.path.realpath(__file__).split("\\")[0:-2]))

import unittest
import numpy as np
from rng_tests.khi_square import KhiSquareTest
from utilities.histogram import Histogram

class TestHistogram(unittest.TestCase):
    
    def test_normal_histogram(self):
        num_interval = 10
        histogram = Histogram(data = [0.08, 0.18, 0.28, 0.38, 0.48, 0.58, 0.68, 0.78, 0.88, 0.98], num_interval = num_interval)
        self.assertEqual([1]*10, histogram.observed)

    def test_overflow_histogram(self):
        num_interval = 10
        histogram = Histogram(data = [0.08, 0.18, 0.28, 0.38, 0.48, 0.58, 0.68, 0.78, 0.88, 0.98, 1], num_interval = num_interval)
        self.assertEqual([1]*9+[2], histogram.observed)
    
if __name__ == "__main__":
    unittest.main()