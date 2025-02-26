import scipy.stats as stats

class KhiSquareTest:
    """
    Chi-Square Goodness of Fit test.

    This test determines whether the observed distribution significantly 
    differs from an expected uniform distribution.
    """
    
    @staticmethod
    def is_goodness_fit(hist: list, alpha: float = 0.05) -> None:
        """
        Computes the Chi-Square statistic for a given histogram and determine if
        it's 

        Args:
            hist (list): A list of observed frequencies for each interval.

        Returns:
            float: The Chi-Square test statistic.
            
        More informations:
            - If X² > critical value -> The distribution significantly differs from uniform (not good).
            - If χ² ≤ critical value -> The distribution is close to uniform (good).

        """
        
        degree_freedom = len(hist) - 1
        
        chi_square = KhiSquareTest.from_distribution(hist=hist)
        
        critical_value = stats.chi2.ppf(1 - alpha, degree_freedom)
        
        if chi_square <= critical_value :
            print("Distribution is close to uniform so it's good")
        else:
            print("Distribution significantly differs from uniform so it's a big NO NO")
        
        
    @staticmethod
    def from_distribution(hist: list) -> float:
        """
        Computes the Chi-Square statistic for a given histogram, assuming 
        a uniform expected distribution.

        Args:
            hist (list): A list of observed frequencies for each interval.

        Returns:
            float: The Chi-Square test statistic.

        Example:
            >>> khi_test = KhiSquareTest()
            >>> khi_test.from_distribution([10, 15, 12, 13])
            1.04
        """
        
        interval_nb = len(hist) 
        total_obs = sum(hist)
        expected = [total_obs / interval_nb] * interval_nb

        return KhiSquareTest.__chi_square_stat(hist, expected)

    @staticmethod
    def __chi_square_stat(hist: list, expected: list):
        """
        Computes the Chi-Square statistic given observed and expected frequencies.

        Args:
            hist (list): A list of observed frequencies.
            expected (list): A list of expected frequencies.

        Returns:
            float: The Chi-Square test statistic.
        """
        
        chi_square = 0
        
        for observed, expected in zip(hist, expected):
            chi_square += ((observed - expected) ** 2) / expected
            
        return chi_square