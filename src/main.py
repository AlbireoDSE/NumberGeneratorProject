from Iterator import EIterator
from utils.path_finder import PathFinder

if __name__ == "__main__":
    
    file_path = PathFinder.get_complet_path("files/e2M.txt")
    iterator = EIterator(file_path)
    print("".join(next(iterator) for _ in range(10)))
    print("".join(next(iterator) for _ in range(10)))