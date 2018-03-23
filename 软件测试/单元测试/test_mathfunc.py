# coding=utf-8
import unittest
from mathfunc import *
# print(add(2,3))
class TestMathFunc(unittest.TestCase):
    '''我们添加了setUp()和tearDown()两个方法（其实是重写了TestCase的这两个方法），
    这两个方法在每个测试方法执行前以及执行后执行一次，
    setUp用来为测试准备环境，tearDown用来清理环境，已备之后的测试。'''
    def setUp(self):
        print ("do something before test.Prepare environment.")
    def tearDown(self):
        print ("do something after test.Clean up.")
    #如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，我们可以用
    #setUpClass()与tearDownClass()
    @classmethod
    def setUpClass(cls):
        print ("This setUpClass() method only called once.")
    @classmethod
    def tearDownClass(cls):
        print ("This tearDownClass() method only called once too.")

    #可以看到setUpClass以及tearDownClass均只执行了一次。
    def test_add(self):
        self.assertEqual(3,add(1,2))
        self.assertNotEqual(3,add(2,2))
    def test_minus(self):
        self.assertEqual(1,minus(3,2))
        self.assertNotEqual(2,minus(3,2))
    def test_multi(self):
        self.assertEqual(6,multi(2,3))
        self.assertNotEqual(8,multi(2,3))
    @unittest.skip("I don't want to run this case.")
    #skip装饰器一共有三个unittest.skip(reason)、unittest.skipIf(condition, reason)、unittest.skipUnless(condition,
    #reason)，skip无条件跳过，skipIf当condition为True时跳过，skipUnless当condition为False时跳过。
    def test_divide(self):
        #self.skipTest('Do not run this.')加上此句和skip装饰效果一样
        self.assertEqual(2,divide(6,3))
        self.assertNotEqual(2.5,divide(5,2))
if __name__ == '__main__':
    unittest.main(verbosity=2)

#在第一行给出了每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E，跳过是 S。
#从上面也可以看出，测试的执行跟方法的顺序没有关系，test_divide写在了第4个，但是却是第2个执行的。
#每个测试方法均以 test 开头，否则是不被unittest识别的。
# 在unittest.main()中加 verbosity 参数可以控制输出的错误报告的详细程度，默认是 1，
# 如果设为 0，则不输出每一用例的执行结果，即没有上面的结果中的第1行；如果设为 2，则输出详细的执行结果