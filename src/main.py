from generator import EGenerator
from iterator import EIterator
from src.histogram import Histogram
from utils.path_finder import PathFinder

if __name__ == "__main__":
    
    #file_path = PathFinder.get_complet_path("files/e2M.txt")
    #iterator = EIterator(file_path = file_path)
    #generator = EGenerator(iterator = iterator)
    
    #print(generator.generate())

    data = [0.1, 0.1, 0.5, 0.6, 0.9, 0.99, 0.3]

    hist = Histogram(interval_nb=5).create(data)
    print(hist)