from iterator import EIterator
from decimal import Decimal

class EGenerator:
    """
    Generator to generate decimal number.
    
    Attributes:
        iterator (EIterator): Iterator class to iterate over the decimal
        num_decimals (int): The number of decimal wanted to be used. Defaults = 10 MAX = 15.
    """
    
    __MAX_DECIMALS = 15  # Maximum allowed decimal places
    __MIN = 1

    def __init__(self, iterator: EIterator, num_decimals: int = 10, period: int = 1):
        """
        Initializes an EGenerator object.

        Args:
            iterator (EIterator): Iterator class to iterate over the decimal
            num_decimals (int): The number of decimal wanted to be used. Defaults = 10 MAX = 15.
            period (int): The value of the shift execute at each generation except for the first one. Defaults = 1 MAX <= num_decimals
        """
        if num_decimals > EGenerator.__MAX_DECIMALS or num_decimals < 1: 
                raise ValueError(f"num_decimals ({num_decimals}) exceeds the maximum allowed ({EGenerator.__MAX_DECIMALS}) or fails behind the minimum allowed ({EGenerator.__MIN})")
            
        if period > num_decimals or period < 1:
                raise ValueError(f"period ({period}) exceeds the maximum allowed ({num_decimals}) or fails behind the minimum allowed ({EGenerator.__MIN})")
        
        self.iterator = iterator
        self.num_decimals = num_decimals
        self.period = period
        self.residual_digits = ""
    
    def generate(self) -> float | None:
        """
        Generate a number with X decimals

        Returns:
            float: generated number
        """
        try:
            if len(self.residual_digits) > 0:
                self.residual_digits = self.residual_digits[self.period:]
                
            self.residual_digits = self.residual_digits + "".join(next(self.iterator) for _ in range(self.num_decimals - len(self.residual_digits)))
            return float("0."+self.residual_digits)
        
        except Exception as e:
            print(e)
            return None
        
    def generate_all_value(self) -> list:
        """_summary_

        Returns:
            list: _description_
        """
        
        number_list = []
        while True:
            number = self.generate()
            if number != None:
                number_list.append(number)
            else:
                print(number)
                print("All the decimal as been used:")
                print(f"\t- Number of decimal after 0.: {self.num_decimals}")
                print(f"\t- The length of the list is: {str(len(number_list))}")
                break
            
        return number_list
