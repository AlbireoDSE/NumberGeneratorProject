from collections import defaultdict
from math import factorial

from utils.calculator import Calculator


class CouponCollectorTest:

    @staticmethod
    def compute(samples, interval_nb):

        collected = defaultdict(int)  # Store the values for histogram
        trials = 0 # r, also used as index to loop through samples

        while len(collected) < interval_nb and trials < len(samples) :
            hist_interval = int(samples[trials] * interval_nb)
            collected[hist_interval] += 1
            trials += 1

        hist = [0] * interval_nb

        for key in collected:
            hist[key] = collected[key]

        #collected = dict(sorted(collected.items(), reverse=True))
        print(collected)
        print(hist)
        print(trials)

    @staticmethod
    def p_r(r, d):
        return Calculator.stirling_number(r, d) * (factorial(d) / d ** r)

    @staticmethod
    def q_r(r, d):
        return 1 - CouponCollectorTest.p_r(r, d)
