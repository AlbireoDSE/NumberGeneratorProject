from collections import defaultdict
from math import factorial

from utils.calculator import Calculator
from tests.khi_square import KhiSquareTest


class CouponCollectorTest:

    @staticmethod
    def compute(samples, interval_nb):

        collected = defaultdict(int)  # Store the values for histogram
        trials = 0 # r, also used as index to loop through samples

        while len(collected) < interval_nb and trials < len(samples) :
            hist_interval = int(samples[trials] * interval_nb)
            collected[hist_interval] += 1
            trials += 1

        hist = [collected[i] for i in range(interval_nb)]

        #compute Sr probability

        #perform Khi_square with hist and compare with Sr
        KhiSquareTest.is_goodness_fit(hist)



    @staticmethod
    def p_r(r, d):
        return Calculator.stirling_number(r, d) * (factorial(d) / d ** r)

    @staticmethod
    def q_r(r, d):
        return 1 - CouponCollectorTest.p_r(r, d)

    @staticmethod
    def s_r(r, d):
        if r < d: return 0
        return (factorial(d)/d**r) * (Calculator.stirling_number(r, d) - d* Calculator.stirling_number(r-1, d))
