# coding=utf-8
from selenium import webdriver
import unittest,time
from HTMLTestRunner import HTMLTestRunner
class MyTest(unittest.TestCase):
    '''百度搜索测试'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://www.baidu.com'
    def test_baidu(self):
        '''搜索关键字：unittest'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys('unittest')
        driver.find_element_by_id('su').click()
        time.sleep(2)
        title = driver.title
        self.assertEqual(title,'unittest_百度搜索')
    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(MyTest('test_baidu'))
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = './' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,title='百度搜索测试报告',description='用例执行情况')
    runner.run(testunit)
    fp.close()