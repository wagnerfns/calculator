import unittest
#import sys
#sys.path.insert(0,'~/github/calculator/operations.py')
from operations import Operations


class TestMethods(unittest.TestCase):

    def test_operation_addition(self):
        operation = Operations(100, 100)
        self.assertEqual(operation.setAddition(), 200, 'Incorrect result') 
    def test_operation_subtraction(self):
        operation = Operations(100, 100)
        self.assertEqual(operation.setSubtraction(), 0, 'Incorrect result') 
    def test_operation_multiplication(self):
        operation = Operations(100, 1)
        self.assertEqual(operation.setMultiplication(), 100, 'Incorrect result') 
    def test_operation_division(self):
        operation = Operations(100,100)
        self.assertEqual(operation.setDivision(), 1, 'Incorrect result')

    def test_operation_root(self):
        operation = Operations(100,1)
        self.assertEqual(operation.setRoot(), 10, 'Incorrect result')

    def test_operation_potentiation(self):
        operation = Operations(10,1)
        self.assertEqual(operation.setPotentiation(), 100, 'Incorrect result')

if __name__ == '__main__':
    unittest.main()
