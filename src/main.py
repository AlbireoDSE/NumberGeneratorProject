from generator import EGenerator
from iterator import EIterator
from src.histogram import Histogram
from src.khi_square_test import KhiSquareTest
from utils.path_finder import PathFinder

if __name__ == "__main__":
    
    #file_path = PathFinder.get_complet_path("files/e2M.txt")
    #iterator = EIterator(file_path = file_path)
    #generator = EGenerator(iterator = iterator)
    
    #print(generator.generate())

    data1 = [0.1, 0.1, 0.5, 0.6, 0.9, 0.99, 0.3, 2]
    data2 = [0.1, 0.5, 0.5, 0.6, 0.9, 0.99, 0.3, 2, 0.01, 0.1]

    hist_creator = Histogram(interval_nb=5)

    hist1 = hist_creator.create(data1)
    hist2 = hist_creator.create(data1)



    khi_square = KhiSquareTest(hist1, hist2).run()
    print(khi_square)
