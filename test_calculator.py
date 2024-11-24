import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
        self.assertEqual(self.calc.add(100, 200), 300)
        self.assertEqual(self.calc.add(300, 1), 301)

        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(10, 10), 0)

        self.assertEqual(self.calc.multiply(10, 10), 100)
        self.assertEqual(self.calc.multiply(3, 3), 9)

        self.assertEqual(self.calc.divide(21, 7), 3)
        self.assertEqual(self.calc.divide(20, 20), 1)

        self.assertEqual(self.calc.modulo(20, 4), 0)
        self.assertEqual(self.calc.modulo(10, 3), 1)

if __name__ == '__main__':
    unittest.main()