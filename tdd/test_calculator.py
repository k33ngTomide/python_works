
import unittest
from calculator import added

class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        result = add(2, 3)
        self.assertEqual(result, 6)

    def test_add_negative_numbers(self):
        result = add(-2, -3)
        self.assertEqual(result, -5)

if __name__ == '__main__':
    unittest.main()