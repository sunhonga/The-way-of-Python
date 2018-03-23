# coding=utf-8

import unittest

class Mydemo(unittest.TestCase):
    def setUp(self):
        print('demo_B开始')

    def tearDown(self):
        print('demo_B结束')
    # def test_sub(self):
    #     self.assertEqual(6,6)
    #     print('cc')
class demo_B(Mydemo):

    @classmethod
    def setUpClass(cls):
        print('hello demo_B')

    def test_aa(self):
        j = 3+ 5
        self.assertEqual(j,8)
        print('aa')

    def test_bb(self):
        k = 6-3
        self.assertEqual(k,3)
        print('bb')

if __name__ == "__main__":
    unittest.main()
