from histogram import Histogram, PlotType
from tests.coupon_collector_test import CouponCollectorTest
from tests.poker_test import PokerTest
from tests.khi_square import KhiSquareTest
from tests.kolmogorov_smirnov import KolmogorovSmirnov
from generator import EGenerator
from iterator import EIterator
from utils.path_finder import PathFinder

def test_khi_square(histogram: list):
    
    print("\n ----------------------KHI SQUARE----------------------\n")
    KhiSquareTest.is_goodness_fit(hist = histogram.hist)

def test_kolmogorov_smirnov(data: list):
    
    print("\n ------------------Kolmogorov Smirnov------------------\n")
    
    KolmogorovSmirnov.reject_null(data = data)

def global_test(data: list):
    
    histogram = Histogram(data = data, num_interval = 10)
    
    histogram.save_plot()
    
    #test_khi_square(histogram = histogram)
    
    #test_kolmogorov_smirnov(data=data)

    print("\n -----------------------END TEST----------------------\n")

    print("\n ------------------Coupon Collector------------------\n")

    CouponCollectorTest.compute(data, 5)

    print("\n -----------------End Test----------------\n")

    print("\n ------------------Poker------------------\n")

    #categories, chi2_stat = PokerTest.compute(data)
    #print(categories)
    #print(chi2_stat)

    print("\n -----------------End Test----------------\n")
    
def decimal_test(file_path: str, num_interval: int = 10, range_max: int = 10):
    
    iterator = EIterator(file_path = file_path)
    
    generator = EGenerator(iterator = iterator, num_decimals = 1, period = 1, prefix="")
    
    data = generator.generate_all_value()
    
    histogram = Histogram(data = data, num_interval = num_interval, range_max = range_max)
    
    histogram.save_plot(plot_type = PlotType.BAR)
    
    test_khi_square(histogram = histogram)

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")
    
    decimal_test(file_path = file_path)





