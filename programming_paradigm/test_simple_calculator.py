import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
        
    def test_subtraction(self):
        """Test the suntraction  method."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(5, 1), 4)
        
    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(4, 1), 4)   
        
        
    def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(10, 2), 5)   
        self.assertEqual(self.calc.divide(10, 0), None)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.
        
if __name__ == "__main__":
        unittest.main()     
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.