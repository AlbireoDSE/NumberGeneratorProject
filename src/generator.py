from iterator import EIterator

class EGenerator:
    """
    Generator to generate decimal number.
    
    Attributes:
        iterator (EIterator): Iterator class to iterate over the decimal
        num_decimals (int): The number of decimal wanted to be used. Defaults = 10.
    """

    def __init__(self, iterator: EIterator, num_decimals: int = 10):
        """
        Initializes an EGenerator object.

        Args:
            iterator (EIterator): Iterator class to iterate over the decimal
            num_decimals (int): The number of decimal wanted to be used. Defaults = 10.
        """
        self.iterator = iterator
        self.num_decimals = num_decimals
        self.divider = 10 ** self.num_decimals
    
    def generate(self) -> float:
        """
        Generate a number with X decimals

        Returns:
            int: generated number
        """
        decimals = "".join(next(self.iterator) for _ in range(self.num_decimals))
        return int(decimals) / self.divider

