from utilities.histogram import Histogram, PlotType
from rng_tests.gap_test import GapTest
from rng_tests.khi_square import KhiSquareTest
from rng_tests.kolmogorov_smirnov import KolmogorovSmirnov
from utilities.generator import EGenerator
from utilities.iterator import EIterator
from utilities.path_finder import PathFinder
import pandas as pd
import os
import random

def test_khi_square(histogram: list, verbose: int = 1, return_bol: bool = False):
    
    if verbose == 1:
        print("\n ----------------------KHI SQUARE----------------------\n")
    
    return KhiSquareTest.is_goodness_fit(histogram = histogram, return_bol = return_bol)

def test_kolmogorov_smirnov(data: list, verbose: int = 1, return_bol: bool = False):
    
    if verbose == 1:
        print("\n ------------------Kolmogorov Smirnov------------------\n")
    
    return KolmogorovSmirnov.is_goodness_fit(data = data, return_bol = return_bol)

def test_gap(data: list, a = 0, b = 0.5, verbose: int = 1, return_bol: bool = False):

    if verbose == 1:
        print("\n ------------------Gap------------------\n")

    return GapTest.is_goodness_fit(data = data, a = a, b = b, return_bol = return_bol)

def generate_all_number(file_path, num_decimals: int, period: int, prefix: str, verbose: int = 1):
    
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = num_decimals, period = period, prefix = prefix)
    
    return generator.generate_all_value(verbose = verbose)

def generate_all_number_using_python(num_decimals: int, period: int, prefix: str, seed:int = 25):
    
    random.seed(10)
    
    random.uniform(0,1)
    
    return generator.generate_all_value(verbose = verbose)
    
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
    
    results = []
    
    for num_decimals in range(3, 5):
        
        for period in range(1, num_decimals + 1):
            
            data = generate_all_number(file_path = file_path, num_decimals = num_decimals, period = period, prefix = "0.", verbose = 0)
            
            histogram = Histogram(data = data, num_interval = num_interval, decimals = 2)
            
            khi_square = test_khi_square(histogram = histogram, verbose = 0, return_bol = True)
            
            ks = test_kolmogorov_smirnov(data = data, verbose = 0, return_bol = True)

            gap = test_gap(data = data, verbose = 0, return_bol = True)
            
            results.append({
                "num_decimals": num_decimals,
                "period": period,
                "num_generated": histogram.number_data,
                "khi_square": khi_square,
                "kolmogorov_smirnov": ks,
                "gap_test": gap
            })
            
    df = pd.DataFrame(results)
    
    print(df.to_latex(buf= PathFinder.get_complet_path(os.path.join("files", "our_generator_table.txt")), index=False))
    
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

    test_gap(data = data)

    print("\n -------------End Python Generator Test------------\n")

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")

    # decimal_test(file_path = file_path)
    
    test_our_generator(file_path = file_path)






