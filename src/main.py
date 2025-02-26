from histogram import Histogram
from tests.khi_square import KhiSquareTest
from generator import EGenerator
from iterator import EIterator
from utils.path_finder import PathFinder

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")
    iterator = EIterator(file_path = file_path)
    generator = EGenerator(iterator = iterator, num_decimals = 15)
    data = []
    
    while True:
        number = generator.generate()
        if number != -1:
            data.append(number)
        else:
            print("The length of the list is: "+ str(len(data)))
            print("No more number in the list")
            break

    histogram = Histogram(data=data, interval_nb = 5)
    histogram.save_plot()

    khi_square = KhiSquareTest.from_distribution(histogram.hist)

    print(khi_square)
    
    KhiSquareTest.is_goodness_fit(data)
