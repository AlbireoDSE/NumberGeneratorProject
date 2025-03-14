from collections import Counter

import numpy as np

from tests.khi_square import KhiSquareTest


class GapTest:

    @staticmethod
    def compute(samples: list, a: float = 0, b: float = 0.5, max_gap_size: int = 10):
        #should add a, b check ( 0 ≤ a < b ≤ 1 )

        p = b-a #probability to be in interval
        gaps, marked_index = GapTest.__make_gaps(a, b, samples)

        #gaps_counter_dict = Counter(gaps)
        gaps_counts = GapTest.__count_gaps(gaps, max_gap_size)

        expected_probs = p * (1 - p) ** np.arange(max_gap_size)
        expected_probs[-1] += (1 - p) ** max_gap_size  # Last category (gap >= max_gap)

        expected_gaps_counts = expected_probs * len(gaps)

        print(expected_gaps_counts, gaps_counts)
        khi_square_stat = KhiSquareTest.compute(gaps_counts, expected_gaps_counts)
        print(f"GAP TEST:\n -khi square value: {khi_square_stat}")

    @staticmethod
    def __make_gaps(a: float, b: float = 0, samples: list = 0.5):
        marked_index = []
        gaps = []
        gap_size = 0
        in_gap = True
        for i, number in enumerate(samples):
            if a <= number < b:
                marked_index.append(i)  # mark number in interval
                if in_gap:  # find new number in interval, gap end
                    gaps.append(gap_size)
                    in_gap = False
                gap_size = 0
            else:
                in_gap = True
                gap_size += 1
        return gaps, marked_index

    @staticmethod
    def __count_gaps(gaps: list, max_gap_size: int):
        gap_counts = [0] * max_gap_size
        for g in gaps:
            if g <= max_gap_size:
                gap_counts[g-1] += 1
            else:
                gap_counts[max_gap_size-1] += 1
        return gap_counts
