from iterator import EIterator
from generator import EGenerator
from utils.path_finder import PathFinder

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")
    iterator = EIterator(file_path = file_path)
    generator = EGenerator(iterator = iterator)
    
    print(generator.generate())