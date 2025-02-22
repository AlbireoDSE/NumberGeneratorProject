class EIterator:
    """ 
    Iterator to read little by little the decimal of e (max 2_000_000).
    
    Attributes:
        filepath (str): The path to the file containing the e decimal.
        chunk_size (int): Number of decimal load at once.
    
    """
    
    def __init__(self, filepath: str, chunk_size: int = 10000):
        """
        Initializes an Iterator object.

        Args:
            filepath (str): The path to the file containing the e decimal
            chunk_size (int): Number of decimal load at once. Defaults = 10000.
            
        """
        self.filepath = filepath
        self.chunk_size = chunk_size
        self.file = open(self.filepath, "r")
        self.buffer = ""
        self.index = 0

    def __iter__(self):
        """
        Returns the iterator itself.
        
        Returns:
            EIterator: The iterator instance itself.
            
        """
        return self

    def __next__(self) -> str:
        """
        Returns the next decimal character from the file.

        If the buffer is exhausted, it reads the next chunk from the file.
        If the file has no more data, it raises StopIteration to signal the end.

        Returns:
            str: The next decimal character from the file.

        Raises:
            StopIteration: If there are no more characters to read.
            
        """
        if self.index >= len(self.buffer):
            self.buffer = self.file.read(self.chunk_size).strip()
            self.index = 0
            if not self.buffer:
                self.file.close()
                raise StopIteration
        char = self.buffer[self.index]
        self.index += 1
        return char