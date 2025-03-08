import matplotlib.pyplot as plt
from utils.path_finder import PathFinder
from enum import Enum

class PlotType(Enum):
    BAR = "bar"
    HiSTOGRAM = "hist"


class Histogram:
    """
    A class for creating histograms from numerical data.

    This class provides a static method to compute a histogram with a specified 
    number of intervals, given a range of values.
    
    Attributes:
        data (list of float): The input numerical data to be binned.
        interval_nb (int): The number of intervals (bins) in the histogram.
        range_min (float, optional): The minimum value of the range. Defaults = 0.
        range_max (float, optional): The maximum value of the range. Defaults = 1.
    """
    
    def __init__(self, data: list, num_interval: int, range_min: int = 0, range_max: int = 1):
        
        """
        Initializes the histogram with data and specified parameters.
        
        Args:
            data (list of float): The input numerical data to be binned.
            interval_nb (int): The number of intervals (bins) in the histogram.
            range_min (float, optional): The minimum value of the range. Defaults = 0.
            range_max (float, optional): The maximum value of the range. Defaults = 1.
        """
        self.data = data
        self.num_interval = num_interval
        self.range_min = range_min
        self.range_max = range_max
        self.hist = [0] * num_interval
        self.mean = len(self.data)/self.num_interval
        
        self._create()

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

            self.hist[index] += 1
        
            
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
        
        plt.figure(figsize=(8, 5))
        
        devider = self.range_max/self.num_interval 
        
        categories = [str(i/devider) for i in range(self.range_min, self.range_max)]
        
        bars = plt.bar(categories, self.hist, edgecolor="black", alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 0.5,
                    str(height), ha='center', va='bottom', fontsize=10)

        plt.xlabel("Values")
        plt.ylabel("Frequency")
        plt.title("Bar Chart")
        plt.grid(axis="y", linestyle="--", alpha=0.8)

        plt.axhline(self.mean, color='red', linestyle='dashed', linewidth=2)
        
        plt.text(self.range_max + 0.6, self.mean, 'Mean:\n{:.2f}'.format(self.mean), color="red")

        plt.savefig(PathFinder.get_complet_path("images/my_bar.png"))
            

    def save_histogram(self) -> None:
        """
        Save the histogram using matplotlib.

        The histogram is save as a bar chart, with bins on the x-axis
        and frequency counts on the y-axis.

        """
        plt.figure(figsize=(8, 5))
        
        counts, bins, _ = plt.hist(self.data, bins = self.num_interval,
                                 range=(self.range_min, self.range_max), 
                                 edgecolor="black", alpha=0.7, density=False)

        for count, bin_edge in zip(counts, bins[:-1]):
            plt.text(bin_edge + (bins[1] - bins[0]) / 2, count + 0.5,
                    str(int(count)), ha='center', va='bottom', fontsize=10)

        plt.xlabel("Value Range")
        plt.ylabel("Frequency")
        plt.title("Histogram")
        
        plt.grid(axis="y", linestyle="--", alpha=0.8)

        plt.axhline(self.mean, color='red', linestyle='dashed', linewidth=2)
        
        plt.text(self.range_max + 0.6, self.mean, 'Mean:\n{:.2f}'.format(self.mean), color="red")
        
        plt.savefig(PathFinder.get_complet_path("images/my_histogram.png"))
        
        plt.close()