import matplotlib.pyplot as plt
from utils.path_finder import PathFinder

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
    
    def __init__(self, data: list, interval_nb: int, range_min: int = 0, range_max: int = 1):
        
        """
        Initializes the histogram with data and specified parameters.
        
        Args:
            data (list of float): The input numerical data to be binned.
            interval_nb (int): The number of intervals (bins) in the histogram.
            range_min (float, optional): The minimum value of the range. Defaults = 0.
            range_max (float, optional): The maximum value of the range. Defaults = 1.
        """
        self.data = data
        self.interval_nb = interval_nb
        self.range_min = range_min
        self.range_max = range_max
        self.hist = [0] * interval_nb
        
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
        
        interval_width = (self.range_max - self.range_min) / self.interval_nb
        
        for value in self.data:
            index = int((value - self.range_min) / interval_width)
            if index >= self.interval_nb:
                index = -1

            self.hist[index] += 1
            
    def save_plot(self) -> None:
        """
        Save the histogram using matplotlib.

        The histogram is save as a bar chart, with bins on the x-axis
        and frequency counts on the y-axis.

        """
        plt.figure(figsize=(8, 5))
        plt.hist(self.data, bins=self.interval_nb, range=(self.range_min, self.range_max), 
                 edgecolor="black", alpha=0.7, density=False)

        plt.xlabel("Value Range")
        plt.ylabel("Frequency")
        plt.title("Histogram")
        plt.grid(axis="y", linestyle="--", alpha=0.6)

        plt.savefig(PathFinder.get_complet_path("images/my_histogram.png"))
        plt.close()