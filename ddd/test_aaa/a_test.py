# coding=utf-8
import unittest

class Mydemo(unittest.TestCase):
    def setUp(self):
        print('demo_A开始')

    def tearDown(self):
        print('demo_A结束')
    # def test_sub(self):
    #     self.assertEqual(6,6)
    #     print('cc')
class demo_A(Mydemo):

    @classmethod
    def setUpClass(cls):
        print('开始 demo_A')

    @classmethod
    def tearDownClass(cls):
        print('结束 demo_A')

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
