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

def test_gap(data: list, a = 0, b = 0.5):

    print("\n ------------------Gap------------------\n")

    GapTest.is_goodness_fit(data = data, a = a, b = b)

def generate_all_number(num_decimals: int, period: int, prefix: str):
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = num_decimals, period = period, prefix = prefix)
    
    return generator.generate_all_value()
    
def decimal_test(file_path: str, num_interval: int = 10, range_max: int = 10):
    
    print("\n ------------Start Decimal Test-----------\n")
    
    data = generate_all_number(num_decimals = 1, period = 1, prefix = "")
    
    histogram = Histogram(data = data, num_interval = num_interval, range_max = range_max)
    
    histogram.save_plot(plot_type = PlotType.BAR)
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data = data)

    test_gap(data = data, b = 4.5)

    print("\n -------------End Decimal Test------------\n")
    
def test_our_generator(file_path: str, num_interval: int = 10):
    
    print("\n ------------Start Decimal Test-----------\n")
    
    data = generate_all_number()
    
    histogram = Histogram(data = data, num_interval = num_interval)
    
    histogram.save_plot(plot_type = PlotType.BAR)
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data = data)

    test_gap(data = data, b = 4.5)

    print("\n -------------End Decimal Test------------\n")
    
def test_python_generator(file_path):
    print("\n ------------Start Decimal Test-----------\n")
    
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = 1, period = 1, prefix = "")
    
    data = generator.generate_all_value()
    
    histogram = Histogram(data = data, num_interval = 10)
    
    histogram.save_plot(plot_type = PlotType.BAR)
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data = data)

    test_gap(data = data, b = 4.5)

    print("\n -------------End Decimal Test------------\n")

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")

    decimal_test(file_path = file_path)







