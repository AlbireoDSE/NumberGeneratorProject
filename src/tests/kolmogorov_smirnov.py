import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import Counter
from utils.path_finder import PathFinder

class KolmogorovSmirnov:
     
    """
    
    More informations:
        H0: If KS > critical value -> The distribution follow the uniform law
        H1: If KS <= critical value -> The distribution does not follow the uniform law
    """
    
    @staticmethod
    def reject_null(data: list, alpha: float = 0.05) -> None:
        """
        Performs the Kolmogorov-Smirnov test to check if the given data follows a uniform(0,1) distribution.

        Args:
            data (list): A list of observed values.
            alpha (float): Significance level (default is 0.05).

        Prints:
            Decision whether to reject or not reject H0.
        """
        
        degree_freedom = len(data) - 1
        
        ks_value = KolmogorovSmirnov.compute(data = data)
        
        critical_value = stats.kstwo.ppf(1 - alpha, degree_freedom)
        
        if ks_value <= critical_value :
            print("Distribution is close to uniform so it's good")
        else:
            print("Distribution significantly differs from uniform so it's a big NO NO")
    
    
    @staticmethod
    def compute(data: list) -> tuple:
        data = np.sort(data)
        size = len(data)
        count_values = Counter(data)

        relative_frequency = np.array(list(count_values.values())) / size
        
        observed_distribution = np.cumsum(relative_frequency)
        
        theorical_distribution = np.arange(1, len(observed_distribution) + 1) / size
        
        absolute_difference = np.abs(observed_distribution - theorical_distribution)
        
        max_diff_index = np.argmax(absolute_difference)
        
        ks_statistic = absolute_difference[max_diff_index]

        KolmogorovSmirnov.__save_plot(list(count_values.keys()), 
                                    observed_distribution = observed_distribution, 
                                    theorical_distribution = theorical_distribution,
                                    max_diff_index = max_diff_index
                                    )
        
        return ks_statistic
    
    @staticmethod
    def __save_plot(unique_values, observed_distribution, theorical_distribution, max_diff_index) -> None:
        """
        Plots the empirical CDF and the expected uniform CDF.

        Args:
        
        """

        plt.figure(figsize=(8, 5))
        plt.step(unique_values, observed_distribution, where="post", label="Empirical CDF", color="blue")
        plt.plot(unique_values, theorical_distribution, linestyle="--", label="Theoretical CDF", color="red")

        
        plt.vlines(unique_values[max_diff_index], theorical_distribution[max_diff_index], observed_distribution[max_diff_index], 
                   colors="black", linestyles="dashed", label="Max Difference (D)")

        plt.xlabel("Value Range")
        plt.ylabel("Cumulative Probability")
        plt.title("Kolmogorov-Smirnov Test: Empirical vs. Uniform CDF")
        plt.legend()
        plt.grid()

        plt.savefig(PathFinder.get_complet_path("images/ks_test.png"))
        plt.close()
        
        
        
        