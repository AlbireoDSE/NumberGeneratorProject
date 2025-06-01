import matplotlib.pyplot as plt
from utilities.path_finder import PathFinder
from enum import Enum
import numpy as np

class PlotType(Enum):
    BAR = "bar"
    HiSTOGRAM = "hist"


class Histogram:
    """
    A class for creating histograms from numerical data.

    This class provides a static method to compute a histogram with a specified 
    number of intervals, given a range of values.
    
    Attributes:
        data (list of float): The input numerical data to be used.
        interval_nb (int): The number of intervals (bins) in the histogram.
        range_min (float, optional): The minimum value of the range. Defaults = 0.
        range_max (float, optional): The maximum value of the range. Defaults = 1.
        decimals (int, optional): Number of decimal to use for category labels. Defaults to 2.
    """
    
    def __init__(self, data: list, num_interval: int, range_min: int = 0, range_max: int = 1, decimals: int = 2):
        
        """
        Initializes the histogram with data and specified parameters.
        
        Args:
            data (list of float): The input numerical data to be used.
            interval_nb (int): The number of intervals (bins) in the histogram.
            range_min (float, optional): The minimum value of the range. Defaults = 0.
            range_max (float, optional): The maximum value of the range. Defaults = 1.
            decimals (int, optional): Number of decimal to use for category labels. Defaults to 2.
        """
        self.data = data
        self.number_data = len(data)
        self.num_interval = num_interval
        self.range_min = range_min
        self.range_max = range_max
        self.observed = [0] * num_interval
        self.mean = self.number_data / num_interval
        self.categories = self._generate_categories(decimals = decimals) 
        
        self._create()

    def _generate_categories(self, decimals: int = 2):
        """
        Generates category labels for each interval in the histogram.

        Args:
            decimals (int): Number of decimal places for formatting labels.

        Returns:
            list of str: Formatted category labels corresponding to each interval.
        """
        step = self.range_max / self.num_interval
        format_str = f"{{:.{decimals}f}}"
        return [format_str.format(i * step) for i in range(0, self.num_interval)]
        
        
    def _median(self) -> float:
        """
        Estimates the median of the distribution based on cumulative frequencies.

        Returns:
            float: An estimated median value based on the histogram's bin counts.
        """
        mid = self.number_data / 2
        cumsum = np.cumsum(self.observed)
        above_mid_index = np.where(cumsum >= mid)[0][0]
        
        return (float(self.categories[above_mid_index]) + 0.1) / (cumsum[above_mid_index] / mid)
        

    def _create(self) -> None:
        """
        Creates a histogram by dividing the data into intervals.

        Example:
            >>> data = [0.1, 0.3, 0.5, 0.7, 0.9, 1.0]
            >>> histogram.hist = Histogram(data, interval_nb=5, range_min=0, range_max=1)
            >>> print(histogram.hist)
            [1, 1, 1, 1, 2]
        """
        
        interval_width = (self.range_max - self.range_min) / self.num_interval
        
        for value in self.data:
            index = int((value - self.range_min) / interval_width)
            if index >= self.num_interval:
                index = -1

            self.observed[index] += 1
            
    def save_plot(self, plot_type: PlotType = PlotType.HiSTOGRAM) -> None:
        """
        Save plot in specific format

        Args:
            plot_type (str, optional): The type of plot wanted to be generated. Defaults = PlotType.HiSTOGRAM.
        """
        
        if plot_type == PlotType.HiSTOGRAM:
            self.save_histogram()
        else:
            self.save_bar()
            
    def save_bar(self) -> None:
        """
        Save the bar chart using matplotlib.

        The histogram is save as a bar chart, with bins on the x-axis
        and frequency counts on the y-axis.
        """
    
        median = self._median()
        
        plt.figure(figsize=(8, 5))
        
        bars = plt.bar(self.categories, self.observed, edgecolor="black", alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                    str(height), ha='center', va='bottom', fontsize=10)

        plt.xlabel("Valeur")
        plt.ylabel("Fréquence")
        plt.title("Répartition des décimales", pad=30)
        plt.grid(axis="y", linestyle="--", alpha=0.8)

        plt.axhline(self.mean, color='red', linestyle='dashed', linewidth=2)
        
        plt.text(self.range_max * 1.05, self.mean, 'Moyenne:\n{:.2f}'.format(self.mean), color="red")
        
        plt.axvline(x = median, color='purple', linestyle='dotted', linewidth=2)
        
        plt.text(median, self.mean * 1.08, 'Médiane:{:.2f}'.format(median), color="purple", ha='center')

        plt.savefig(PathFinder.get_complet_path("images/my_bar.png"))
            

    def save_histogram(self) -> None:
        """
        Save the histogram using matplotlib.

        The histogram is save as a bar edges, with bins on the x-axis
        and frequency counts on the y-axis.

        """
        
        median = self._median()
        
        plt.figure(figsize=(8, 5))
        
        counts, bins, _ = plt.hist(self.data, bins = self.num_interval,
                                 range=(self.range_min, self.range_max), 
                                 edgecolor="black", alpha=0.7, density=False)

        for count, bin_edge in zip(counts, bins[:-1]):
            plt.text(bin_edge + (bins[1] - bins[0]) / 2, count + 0.5,
                    str(int(count)), ha='center', va='bottom', fontsize=10)

        plt.xlabel("Intervalle")
        plt.ylabel("Fréquence")
        plt.title("Histogramme", pad=30)
        
        plt.grid(axis="y", linestyle="--", alpha=0.8)

        plt.axhline(self.mean, color='red', linestyle='dashed', linewidth=2)
        
        plt.text(self.range_max * 1.05, self.mean, 'Moyenne:\n{:.2f}'.format(self.mean), color="red")
        
        plt.savefig(PathFinder.get_complet_path("images/my_histogram.png"))
        
        plt.close()