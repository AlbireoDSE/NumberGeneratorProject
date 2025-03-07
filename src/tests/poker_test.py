import sys
from collections import defaultdict, Counter

from histogram import Histogram
from tests.khi_square import KhiSquareTest

from utils.calculator import Calculator


class PokerTest:

    @staticmethod
    def count_values(fs: str) -> dict:
        dict = defaultdict(int)
        for n in fs:
            if n not in dict:
                dict[n]
            dict[n] += 1
        return dict


    @staticmethod
    def stirling_prob(k, d):
        prob = {}

        for r in range(1, k + 1):  # r correspond to the number of distincts groups
            S_kr = Calculator.stirling_number(k, r)

            # Computing of d(d-1)...(d-r+1)
            prod_d = 1
            for i in range(r):
                prod_d *= (d - i)

            p_r = (S_kr * prod_d) / (d ** k)
            prob[r] = p_r
        return prob


    @staticmethod
    def compute(sample, k=5, d=10):
        formatted_samples = [str(int(val * (10**k))).zfill(k) for val in sample]

        categories = {"Poker": 0, "Square": 0, "Full House": 0, "Brelan": 0, "Two Pairs": 0, "One Pair": 0, "All diff": 0}

        for number in formatted_samples:
            counts = Counter(number)
            counts = sorted(counts.values(), reverse=True)

            if counts == [5]:
                categories["Poker"] += 1
            elif counts == [4, 1]:
                categories["Square"] += 1
            elif counts == [3, 2]:
                categories["Full House"] += 1
            elif counts == [3, 1, 1]:
                categories["Brelan"] += 1
            elif counts == [2, 2, 1]:
                categories["Two Pairs"] += 1
            elif counts == [2, 1, 1, 1]:
                categories["One Pair"] += 1
            else:
                categories["All diff"] += 1

        stirling_probs = PokerTest.stirling_prob(k, d)
        poker_probs = {"5D": stirling_probs.get(5, 0), "4D": stirling_probs.get(4, 0),
                        "FH": stirling_probs.get(3, 0), "3D": stirling_probs.get(3, 0),
                        "2P": stirling_probs.get(2, 0), "1P": stirling_probs.get(1, 0),
                        "0P": stirling_probs.get(0, 0)}

        poker_counts = {k: v * len(sample) for k, v in poker_probs.items()}


        hist = Histogram(data = poker_probs, num_interval= 10)
        chi_square_stat = KhiSquareTest().compute(hist)

        return categories, chi_square_stat



