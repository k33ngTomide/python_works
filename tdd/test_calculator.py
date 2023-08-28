import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEquals(result, 5)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEquals(result, -5)

    def test_multiply_returns_numbers(self):
        multiply_result = multiply(5, 7)
        self.assertEquals(multiply_result, 35)

    def test_that_test_can_pass(self):
        pass


if __name__ == '__main__':
    unittest.main()
