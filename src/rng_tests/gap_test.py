from collections import Counter

import numpy as np

from rng_tests.khi_square import KhiSquareTest
from utilities.histogram import Histogram


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



class GapTest:

    @staticmethod
    def compute(data: list, a: float = 0, b: float = 0.5, max_gap_size: int = 10):

        probability = b - a 
        
        gaps = GapTest.__make_gaps(a = a, b = b, samples = data)

        gaps_counts = GapTest.__count_gaps(gaps = gaps, max_gap_size = max_gap_size)

        expected_probs = probability * (1 - probability) ** np.arange(max_gap_size)
        
        expected_probs[-1] += (1 - probability) ** max_gap_size

        expected_probs *= len(gaps)
        
        print(expected_probs)

        return KhiSquareTest.compute(observed = gaps_counts, expected = expected_probs)

    @staticmethod
    def __make_gaps(a: float, b: float, samples: list):
        gaps = []
        gap_size = 0
        found_first = False
        for i, number in enumerate(samples):
            if a <= number < b:
                if found_first: 
                    gaps.append(gap_size)
                else:
                    found_first = True
                gap_size = 0
            elif found_first:
                gap_size += 1
        return gaps
    
    @staticmethod
    def __count_gaps(gaps: list, max_gap_size: int):
        gap_counts = np.zeros(max_gap_size + 1)
        for g in gaps:
            if g <= max_gap_size:
                gap_counts[g] += 1
            else:
                gap_counts[max_gap_size] += 1
        return gap_counts