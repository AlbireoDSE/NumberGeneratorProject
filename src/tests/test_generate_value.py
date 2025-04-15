import unittest

from utilities.generator import EGenerator,EIterator

class MockEIterator(EIterator):
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __next__(self):
        if self.index >= len(self.values):
            raise StopIteration
        val = self.values[self.index]
        self.index += 1
        return val

    def __iter__(self):
        return self

class TestEGenerator(unittest.TestCase):
    
    def test_generate_valid_number(self):
        digits = list("1234567890") * 2
        iterator = MockEIterator(digits)
        gen = EGenerator(iterator, num_decimals=10, period=1)

        self.assertEqual(gen.generate(), 0.1234567890)

    def test_generate_multiple_calls(self):
        digits = list("12345678901234567890")
        iterator = MockEIterator(digits)
        gen = EGenerator(iterator, num_decimals=10, period=3)

        self.assertEqual(gen.generate(), 0.1234567890)
        self.assertEqual(gen.generate(), 0.4567890123)
        self.assertEqual(gen.generate(), 0.7890123456)

    def test_generate_handles_exceptions(self):
        iterator = MockEIterator("1234")
        gen = EGenerator(iterator, num_decimals=10)
        result = gen.generate()
        self.assertIsNone(result)

    def test_generate_all_value(self):
        digits = list("12345678901234567890")
        iterator = MockEIterator(digits)
        gen = EGenerator(iterator, num_decimals = 10, period = 5)

        result = gen.generate_all_value(verbose = 0)
        expected = [0.1234567890, 0.6789012345, 0.1234567890]
        self.assertEqual(len(result), len(expected))
        for val, exp in zip(result, expected):
            self.assertEqual(val, exp)

    def test_invalid_num_decimals_raises(self):
        with self.assertRaises(ValueError):
            EGenerator(MockEIterator("1234"), num_decimals=0)

        with self.assertRaises(ValueError):
            EGenerator(MockEIterator("1234"), num_decimals=16)

    def test_invalid_period_raises(self):
        with self.assertRaises(ValueError):
            EGenerator(MockEIterator("1234"), num_decimals=10, period=0)

        with self.assertRaises(ValueError):
            EGenerator(MockEIterator("1234"), num_decimals=10, period=11)
        
    
    
if __name__ == "__main__":
    unittest.main()