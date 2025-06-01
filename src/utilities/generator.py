from utilities.iterator import EIterator

class EGenerator:
    """
    Generator to generate decimal number.
    
    Attributes:
        iterator (EIterator): Iterator class to iterate over the decimal
        num_decimals (int): The number of decimal wanted to be used. Defaults = 10 MAX = 15.
    """
    
    __MAX_DECIMALS = 15  # Maximum allowed decimal places
    __MIN = 1

    def __init__(self, iterator: EIterator, num_decimals: int = 10, shift: int = 1, prefix: str = "0."):
        """
        Initializes an EGenerator object.

        Args:
            iterator (EIterator): Iterator class to iterate over the decimal
            num_decimals (int, optional): The number of decimal wanted to be used. Defaults = 10 MAX = 15.
            period (int, optional): The value of the shift execute at each generation except for the first one. Defaults = 1 MAX <= num_decimals
            prefix (str, optional): The prefix to add before the number get from the iterator. Default = "0."
        """
        if num_decimals > EGenerator.__MAX_DECIMALS or num_decimals < 1: 
                raise ValueError(f"num_decimals ({num_decimals}) exceeds the maximum allowed ({EGenerator.__MAX_DECIMALS}) or fails behind the minimum allowed ({EGenerator.__MIN})")
            
        if shift > num_decimals or shift < 1:
                raise ValueError(f"shift ({shift}) exceeds the maximum allowed ({num_decimals}) or fails behind the minimum allowed ({EGenerator.__MIN})")
        
        self.iterator = iterator
        self.num_decimals = num_decimals
        self.shift = shift
        self.residual_digits = ""
        self.prefix = prefix
    
    def generate(self) -> float | None:
        """
        Generate a number with X decimals

        Returns:
            float: generated number
        """
        try:
            if len(self.residual_digits) > 0:
                self.residual_digits = self.residual_digits[self.shift:]
                
            self.residual_digits = self.residual_digits + "".join(next(self.iterator) for _ in range(self.num_decimals - len(self.residual_digits)))
            return float(self.prefix + self.residual_digits)
        
        except Exception as e:
            return None
        
    def generate_all_value(self, verbose: int = 1) -> list:
        """
        Generate all value until we reach the end of the file 

        Returns:
            list: Generated values
        """
        
        number_list = []
        number = self.generate()
        while number != None:
            number_list.append(number)
            number = self.generate()

        if verbose == 1:
            print("All the decimal as been used:")
            print(f"\t- Number of decimal after 0.: {self.num_decimals}")
            print(f"\t- Shift : {self.shift}")
            print(f"\t- The length of the list is: {str(len(number_list))}")
        return number_list
