from utilities.histogram import Histogram, PlotType
from rng_tests.gap_test import GapTest
from rng_tests.khi_square import KhiSquareTest
from rng_tests.kolmogorov_smirnov import KolmogorovSmirnov
from utilities.generator import EGenerator
from utilities.iterator import EIterator
from utilities.path_finder import PathFinder

def test_khi_square(histogram: list):
    
    print("\n ----------------------KHI SQUARE----------------------\n")
    
    KhiSquareTest.is_goodness_fit(histogram = histogram)

def test_kolmogorov_smirnov(data: list):
    
    print("\n ------------------Kolmogorov Smirnov------------------\n")
    
    KolmogorovSmirnov.is_goodness_fit(data = data)

def global_test(data: list):
    
    #histogram = Histogram(data = data, num_interval = 10)
    
    #histogram.save_plot()
    
    #test_khi_square(histogram = histogram)
    
    #test_kolmogorov_smirnov(data=data)

    print("\n -----------------------END TEST----------------------\n")

    print("\n -----------------End Test----------------\n")
    
def decimal_test(file_path: str, num_interval: int = 10, range_max: int = 10):
    
    print("\n ------------Start Decimal Test-----------\n")
    
    # GETTING ALL THE DECIMAL
    
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = 1, period = 1)
    
    data = generator.generate_all_value()
    
    # GENERATE THE HISTOGRAM (BAR CHART)
    
    histogram = Histogram(data = data, num_interval = num_interval, range_max = range_max)
    
    histogram.save_plot(plot_type = PlotType.BAR)

    # KHI SQUARE TEST
    
    test_khi_square(histogram = histogram)
    
    # KOLMOGOROV SMIRNOV TEST
    
    test_kolmogorov_smirnov(data = data)
    
    print("\n -------------End Decimal Test------------\n")

    GapTest.compute(samples=data)

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")

    # global_test(data)

    decimal_test(file_path = file_path)







