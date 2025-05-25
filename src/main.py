from utilities.histogram import Histogram, PlotType
from rng_tests.gap_test import GapTest
from rng_tests.khi_square import KhiSquareTest
from rng_tests.kolmogorov_smirnov import KolmogorovSmirnov
from utilities.generator import EGenerator
from utilities.iterator import EIterator
from utilities.path_finder import PathFinder

def test_khi_square(histogram: list, verbose: int = 1):
    
    if verbose == 1:
        print("\n ----------------------KHI SQUARE----------------------\n")
    
    KhiSquareTest.is_goodness_fit(histogram = histogram)

def test_kolmogorov_smirnov(data: list, verbose: int = 1):
    
    if verbose == 1:
        print("\n ------------------Kolmogorov Smirnov------------------\n")
    
    KolmogorovSmirnov.is_goodness_fit(data = data)

def test_gap(data: list, a = 0, b = 0.5, verbose: int = 1):

    if verbose == 1:
        print("\n ------------------Gap------------------\n")

    GapTest.is_goodness_fit(data = data, a = a, b = b)

def generate_all_number(file_path, num_decimals: int, period: int, prefix: str):
    
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = num_decimals, period = period, prefix = prefix)
    
    return generator.generate_all_value()
    
def decimal_test(file_path: str, num_interval: int = 10, range_max: int = 10):
    
    print("\n ------------Start Decimal Test-----------\n")
    
    data = generate_all_number(file_path = file_path, num_decimals = 1, period = 1, prefix = "")
    
    histogram = Histogram(data = data, num_interval = num_interval, range_max = range_max, decimals = 0)
    
    histogram.save_plot(plot_type = PlotType.BAR)
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data = data)

    test_gap(data = data, b = 4.5)

    print("\n -------------End Decimal Test------------\n")
    
def test_our_generator(file_path: str, num_interval: int = 10):
    
    print("\n ------------Start Our Generator Test-----------\n")
    
    data = generate_all_number(file_path = file_path, num_decimals = 10, period = 1, prefix = "0.")
    
    histogram = Histogram(data = data, num_interval = num_interval, decimals = 2)
    
    histogram.save_plot(plot_type = PlotType.HiSTOGRAM)
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data = data)

    test_gap(data = data, b = 4.5)

    print("\n -------------End Our Generator Test------------\n")
    
def test_python_generator(file_path):
    print("\n ------------Start Python Generator Test-----------\n")
    
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = 10, period = 1)
    
    data = generator.generate_all_value()
    
    histogram = Histogram(data = data, num_interval = 10, decimals = 0)
    
    histogram.save_plot(plot_type = PlotType.BAR)
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data = data)

    test_gap(data = data, b = 4.5)

    print("\n -------------End Python Generator Test------------\n")

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")

    # decimal_test(file_path = file_path)
    
    test_our_generator(file_path = file_path)






