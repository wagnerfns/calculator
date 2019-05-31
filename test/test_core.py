import unittest
from operations import Operations


class TestMethods(unittest.TestCase):

    def test_operation_addition(self):
        operation = Operations(100, 100)
        self.assertEqual(operation.addition(), 200, 'Incorrect result')

    def test_operation_subtraction(self):
        operation = Operations(100, 100)
        self.assertEqual(operation.subtraction(), 0, 'Incorrect result')

    def test_operation_multiplication(self):
        operation = Operations(100, 1)
        self.assertEqual(operation.multiplication(), 100, 'Incorrect result')

    def test_operation_division(self):
        operation = Operations(100,100)
        self.assertEqual(operation.division(), 1, 'Incorrect result')

    def test_operation_division_by_zero(self):
        operation = Operations(100,0)
        self.assertEqual(operation.division(), None, 'Incorrect result')

    def test_operation_root(self):
        operation = Operations(100,1)
        self.assertEqual(operation.root(), 10,  'Incorrect result')

    def test_operation_potentiation(self):
        operation = Operations(10,1)
        self.assertEqual(operation.potentiation(), 100,  'Incorrect result')

    def test_avg(self):
        operation = Operations([1,2,3,4], False)
        self.assertAlmostEqual(operation.avg(), 2.5, msg='Incorrect result')

    def test_factorial(self):
        operation = Operations(6)
        self.assertEqual(operation.factorial(), 720, msg='Incorrect Result')

if __name__ == '__main__':
    unittest.main()
