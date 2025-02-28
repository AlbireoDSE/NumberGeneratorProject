from histogram import Histogram
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
    
    histogram = Histogram(data = data, interval_nb = 10)
    
    histogram.save_plot()
    
    test_khi_square(histogram = histogram)
    
    test_kolmogorov_smirnov(data=data)

    print("\n -----------------------END TEST----------------------\n")

    print("\n ------------------Poker------------------\n")

    print(PokerTest.stirling_number(5, 2))

    print("\n -----------------End Test----------------\n")

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")
    iterator = EIterator(file_path = file_path)
    generator = EGenerator(iterator = iterator, num_decimals = 15)
    data = generator.generate_all_value()
    
    global_test(data = data)




