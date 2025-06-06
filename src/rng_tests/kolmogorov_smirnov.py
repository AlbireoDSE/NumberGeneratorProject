
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import Counter
from utilities.path_finder import PathFinder

class KolmogorovSmirnov:
    """
        A class to perform the Kolmogorov Smirnov goodness-of-fit test to determine
        if a given distribution matches the uniform distribution.
    """
    
    @staticmethod
    def is_goodness_fit(data: list, alpha: float = 0.05, return_bol: bool = False) -> None | bool:
        """
        Performs the Kolmogorov-Smirnov test to check if the given data follows a uniform(0,1) distribution.

        Args:
            data (list): A list of observed values.
            alpha (float): Significance level (default is 0.05).
            return_bol (bool): Determine if the code should return a boolean or print a sentence

        More informations:
            H0: If Dn ≤ critical value -> The distribution follow the uniform law (good). 
            H1: If Dn > critical value -> The distribution does not follow the uniform law (not good).
        """
        
        n_samples = len(data)
        
        ks_value = KolmogorovSmirnov.compute(data = data)
        
        critical_value = KolmogorovSmirnov.compute_critical_value(alpha, n_samples)
        
        is_good = ks_value <= critical_value
        
        # print("ks_value: ", ks_value)
        # print("critical_value: ", critical_value)
        if return_bol:
            return is_good
        
        if is_good:

            print("Verily, the distribution is well-balanced, as though guided by divine order !")
        else:
            print("Verily, the distribution is corrupted and uneven, for the Deceiver hath sown disorder among the number !")
    
    
    @staticmethod
    def compute_critical_value(alpha, n_samples) -> float:
        """
        Computes the Kolmogorov Smirnov critical value

        Args:
            alpha (float): The significance level used to determine the critical value for rejecting the H0. 
            degree_freedom (float): Degrees of freedom of the kolmogorov smirnov distribution.

        Returns:
            float: The Kolmogorov Smirnov critical value .
        """
        return stats.kstwo.ppf(1 - alpha, n_samples)
    
    @staticmethod
    def compute(data: list, save_plot: bool = True) -> float:
        """
        Computes the Kolmogorov Smirnov statistic list of data.

        Args:
            data (list): A list of observed data.

        Returns:
            float: The Kolmogorov Smirnov test statistic.
        """
        
        data = np.sort(data)
        
        size = len(data)
        
        count_values = dict(sorted(Counter(data).items()))

        observed_frequency = np.array(list(count_values.values())) / size
        
        observed_cumulative_frequency = np.cumsum(observed_frequency)
        
        theorical_cumulative_frequency = np.arange(1, len(observed_cumulative_frequency) + 1) / len(observed_cumulative_frequency)
                
        absolute_difference = np.abs(observed_cumulative_frequency - theorical_cumulative_frequency)
        
        max_diff_index = np.argmax(absolute_difference)
        
        ks_statistic = absolute_difference[max_diff_index]

        if (save_plot):
            KolmogorovSmirnov.__save_plot(list(count_values.keys()), 
                                        observed_cumulative_frequency = observed_cumulative_frequency, 
                                        theorical_cumulative_frequency = theorical_cumulative_frequency,
                                        max_diff_index = max_diff_index,
                                        ks_statistic = ks_statistic
                                        )
        
        return ks_statistic
    
    @staticmethod
    def __save_plot(unique_values, observed_cumulative_frequency, theorical_cumulative_frequency, max_diff_index, ks_statistic) -> None:
        """
        Plots the empirical CDF and the expected uniform CDF.

        Args:
            data (list): Sorted data points.
            empirical_cdf (list): Empirical cumulative distribution function.
            theoretical_cdf (list): Theoretical cumulative distribution function.
            ks_statistic (float): KS statistic (Dn).
        
        """

        plt.figure(figsize=(8, 5))
        
        plt.step(unique_values, observed_cumulative_frequency, where="post", label="Fréquence cumulée observée", color="blue")
        
        plt.plot(unique_values, theorical_cumulative_frequency, linestyle="--", label="Fréquence cumulée théorique", color="red")
        
        plt.annotate("", xy=(unique_values[max_diff_index], observed_cumulative_frequency[max_diff_index]), xytext=(unique_values[max_diff_index], theorical_cumulative_frequency[max_diff_index]),
             arrowprops=dict(arrowstyle="<->", color='black', lw=2))
        
        plt.text(unique_values[max_diff_index], (observed_cumulative_frequency[max_diff_index] + theorical_cumulative_frequency[max_diff_index]) / 2, f' D={ks_statistic:.3f}', color='black', fontsize=12, 
         verticalalignment='center', horizontalalignment='right')

        plt.xlabel("Intervalle")
        plt.ylabel("Fréquence cumulée")
        plt.title("Test de Kolmogorov-Smirnov")
        plt.legend()
        plt.grid()

        plt.savefig(PathFinder.get_complet_path("images/ks_test.png"))
        plt.close()
        
        
        
        