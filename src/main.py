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

    data1 = [0.1, 0.2, 0.01, 0.1, 0.2, 0.01, 0.1, 0.2, 0.01, 0.4, 0.1, 0.5, 0.6, 0.9, 0.99, 0.3, 2, 0.7]
    data2 = [0.1, 0.5, 0.5, 0.6, 0.9, 0.99, 0.3, 2, 0.01, 0.1]

    hist_creator = Histogram(interval_nb=5)

    hist1 = hist_creator.create(data1)
    hist2 = hist_creator.create(data2)

    khi_square_test = KhiSquareTest()

    khi_square1 = khi_square_test.from_histograms(hist1, hist2)
    khi_square2 = khi_square_test.from_distribution(hist1)

    print(khi_square1)
    print(khi_square2)
