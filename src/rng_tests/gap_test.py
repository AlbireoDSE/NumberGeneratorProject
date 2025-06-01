from collections import Counter

import numpy as np

from rng_tests.khi_square import KhiSquareTest

class GapTest:

    @staticmethod
    def is_goodness_fit(data: list, alpha: float = 0.05, a: float = 0, b: float = 0.5, max_gap_size: int = 10, range_max: int = 1, return_bol: bool = False) ->  None | bool:
        """
        Computes the X statistic for a given histogram and determine if
        the frequencies are following a the uniform law

        Args:
            data (list): A list of observed values.
            alpha (float): Significance level (default is 0.05).

        Returns:
            float: The X test statistic.
            
        More informations:
            H0: If χ² ≤ critical value -> The distribution follow the uniform law (good). 
            H1: If X² > critical value -> The distribution does not follow the uniform law (not good).
        """
        
        chi_square = GapTest.compute(data = data, a = a, b = b, max_gap_size = max_gap_size, range_max = range_max)
        
        critical_value = KhiSquareTest.compute_critical_value(alpha = alpha, degree_freedom = max_gap_size)
        
        is_good = chi_square <= critical_value
        
        # print("gap chi square: ", chi_square)
        # print("gap critical: ", critical_value)
        if return_bol:
            return is_good
        
        if is_good :
            print("Verily, the distribution is well-balanced, as though guided by divine order !")
        else:
            print("Verily, the distribution is corrupted and uneven, for the Deceiver hath sown disorder among the number !")
            
            
    @staticmethod
    def compute(data: list, a: float = 0, b: float = 0.5, max_gap_size: int = 10, range_max: int = 1):
        """
            Performs the Gap Test on a list of pseudo-random data to evaluate
            the uniformity of the sequence by analyzing the gaps between occurrences
            of samples falling within the target interval [a, b].

        Args:
            data (list): List of pseudo-random values to be tested.
            a (float): Lower bound of the target interval (by default: 0)
            b (float): Upper bound of the target interval (by default: 0.5)
            max_gap_size (int): Maximum gap size to consider; all larger gaps are grouped into the last bin (by default: 10)
            range_max (int): Maximum value of the data if normalized (by default: 1)
        Return:
            The Chi-Square statistic comparing observed gap frequencies to expected frequencies.
        """

        probability = b - a 
        
        gaps = GapTest.__make_gaps(a = a, b = b, samples = data, range_max = range_max)

        gaps_counts = GapTest.__count_gaps(gaps = gaps, max_gap_size = max_gap_size)

        expected_probs = probability * (1 - probability) ** np.arange(max_gap_size + 1)
        
        expected_probs[max_gap_size] = (1 - probability) ** max_gap_size

        expected_probs *= len(gaps)

        #print(len(gaps))
        # print("observed: ", gaps_counts)
        # print("expected: ", expected_probs)
        return KhiSquareTest.compute(observed = gaps_counts, expected = expected_probs)

    @staticmethod
    def __make_gaps(a: float, b: float, samples: list, range_max: int):
        """
            Identifies the sequence of gap sizes (number of consecutive samples outside the target interval [a, b])
            between 'successes' (samples that fall within the interval [a, b]) in the given data.

            Args:
                a (float): Lower bound of the interval.
                b (float): Upper bound of the interval.
                samples (list): List of pseudo-random values to be analyzed.
                range_max (int): Maximum value of the samples.

            Return:
                List of gap sizes, each representing the count of consecutive samples outside [a, b] between two successes.
        """
        gaps = []
        gap_size = 0
        found_first = False
        for i, number in enumerate(samples):
            if a <= (number/range_max) < b:
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
        """
            Counts the number of occurrences of each gap size in the list of gaps,
            grouping all gaps larger than max_gap_size into the last bin.

        Args:
            gaps (list): List of gap sizes.
            max_gap_size (int): The maximum gap size to consider; all larger gaps are counted in the last bin.

        Return:
            An array of size (max_gap_size + 1) where each index represents the count
            of gaps of size equal to the index. The last index counts all gaps >= max_gap_size.
        """
        gap_counts = np.zeros(max_gap_size + 1)
        for g in gaps:
            if g <= max_gap_size:
                gap_counts[g] += 1
            else:
                gap_counts[max_gap_size] += 1
        return gap_counts