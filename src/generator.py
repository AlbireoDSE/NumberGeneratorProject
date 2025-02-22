from iterator import EIterator

class EGenerator:

    def __init__(self, iterator: EIterator, num_decimals: int = 10):
        self.iterator = iterator
        self.num_decimals = num_decimals
        self.divider = 10 ** self.num_decimals
    
    def generate(self):
        decimals = "".join(next(self.iterator) for _ in range(self.num_decimals))
        return int(decimals) / self.divider

