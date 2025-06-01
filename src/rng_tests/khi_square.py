import scipy.stats as stats
from utilities.histogram import Histogram

class KhiSquareTest:
    """
        A class to perform the Chi-Square goodness-of-fit test to determine
        if a given distribution matches the uniform distribution.
    """
    
    @staticmethod
    def is_goodness_fit(histogram: Histogram, alpha: float = 0.05, return_bol: bool = False) ->  None | bool:
        """
        Computes the Chi-Square statistic for a given histogram and determine if
        the frequencies are following a the uniform law

        Args:
            histogram (Histogram): A object containing usefull information like the frequency for each interval, the mean, etc.
            alpha (float): The significance level used to determine the critical value for rejecting the H0. 
            return_bol (bool): Determine if the code should return a boolean or print a sentence
            
        Returns:
            float: The Chi-Square test statistic.
            
        More informations:
            H0: If χ² ≤ critical value -> The distribution follow the uniform law (good). 
            H1: If X² > critical value -> The distribution does not follow the uniform law (not good).

        """
        
        expected = [histogram.mean] * histogram.num_interval
        
        chi_square = KhiSquareTest.compute(observed = histogram.observed, expected = expected)
        
        critical_value = KhiSquareTest.compute_critical_value(alpha,  histogram.num_interval - 1)
        
        is_good = chi_square <= critical_value
        
        if return_bol:
            return is_good
        
        if chi_square <= critical_value :
            print("Verily, the distribution is well-balanced, as though guided by divine order !")
        else:
            print("Verily, the distribution is corrupted and uneven, for the Deceiver hath sown disorder among the number !")
    
    @staticmethod
    def compute_critical_value(alpha, degree_freedom) -> float:
        """
        Computes the Chi-Square critical value

        Args:
            alpha (float): The significance level used to determine the critical value for rejecting the H0. 
            degree_freedom (float): Degrees of freedom of the chi-square distribution.

        Returns:
            float: The Chi-Square critical value .
        """
        return stats.chi2.ppf(1 - alpha, degree_freedom)
        
    @staticmethod
    def compute(observed: list, expected: list) -> float:
        """
        Computes the Chi-Square statistic for a given histogram, assuming 
        a uniform expected distribution.

        Args:
            observed (list): A list of observed frequencies for each interval.
            expected (list): A list of expected frequencies for each interval.

        Returns:
            float: The Chi-Square test statistic.

        Example:
            >>> khi_test = KhiSquareTest()
            >>> khi_test.compute([10, 15, 12, 13], [12.5, 12.5, 12.5, 12.5])
            1.04
        """
        
        chi_square = 0
        
        for observed, expected in zip(observed, expected):
            chi_square += ((observed - expected) ** 2) / expected
        
        return chi_square
        
