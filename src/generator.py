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
    
    def generate(self) -> float | None:
        """
        Generate a number with X decimals

        Returns:
            float: generated number
        """
        try:
            decimals = "".join(next(self.iterator) for _ in range(self.num_decimals))
            return int(decimals) / self.divider
        
        except Exception as e:
            return None
        
    def generate_all_value(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        
        number_list = []
        while True:
            number = self.generate()
            if number:
                number_list.append(number)
            else:
                print("All the decimal as been used:")
                print(f"\t- Number of decimal after 0.: {self.num_decimals}")
                print(f"\t- The length of the list is: {str(len(number_list))}")
                break
            
        return number_list
