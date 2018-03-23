# coding=utf-8
# function.py
def add_and_multiply(x, y):
    addition = x + y
    multiple = multiply(x, y)
    return (addition, multiple)
def multiply(x, y):
    return x * y
    # a_test.py
import unittest
   # from function import add_and_multiply
class MyTestCase(unittest.TestCase):
    def test_add_and_multiply(self):
        x = 3
        y = 5
        addition, multiple = add_and_multiply(x, y)
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)
if __name__ == "__main__":
    unittest.main()