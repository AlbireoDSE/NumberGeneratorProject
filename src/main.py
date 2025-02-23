from src.histogram import Histogram
from src.tests.khi_square import KhiSquareTest

if __name__ == "__main__":
    
    #file_path = PathFinder.get_complet_path("files/e2M.txt")
    #iterator = EIterator(file_path = file_path)
    #generator = EGenerator(iterator = iterator)
    
    #print(generator.generate())

    data1 = [0.1, 0.2, 0.01, 0.1, 0.2, 0.01, 0.1, 0.2, 0.01, 0.4, 0.1, 0.5, 0.6, 0.9, 0.99, 0.3, 2, 0.7]
    data2 = [0.1, 0.5, 0.5, 0.6, 0.9, 0.99, 0.3, 2, 0.01, 0.1]

    hist_creator = Histogram(interval_nb=5)

    hist1 = hist_creator.create(data1)
    hist2 = hist_creator.create(data2)



    khi_square = KhiSquareTest(hist1, hist2).run()
    print(khi_square)
