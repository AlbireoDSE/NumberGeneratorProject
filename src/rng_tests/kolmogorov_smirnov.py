
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from collections import Counter
from utils.path_finder import PathFinder

class KolmogorovSmirnov:
     
    """
    

    """
    
    @staticmethod
    def is_goodness_fit(data: list, alpha: float = 0.05) -> None:
        """
        Performs the Kolmogorov-Smirnov test to check if the given data follows a uniform(0,1) distribution.

        Args:
            data (list): A list of observed values.
            alpha (float): Significance level (default is 0.05).

        More informations:
            H0: If Dn ≤ critical value -> The distribution follow the uniform law (good). 
            H1: If Dn > critical value -> The distribution does not follow the uniform law (not good).
        """
        
        degree_freedom = len(data)
        
        ks_value = KolmogorovSmirnov.compute(data = data)
        
        critical_value = stats.kstwo.ppf(1 - alpha, degree_freedom)
        
        if ks_value <= critical_value :
            print("Verily, the distribution is well-balanced, as though guided by divine order !")
        else:
            print("Verily, the distribution is corrupted and uneven, for the Deceiver hath sown disorder among the number !")
    
    
    @staticmethod
    def compute(data: list, save_plot: bool = True) -> tuple:
        
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
        
        
        
        