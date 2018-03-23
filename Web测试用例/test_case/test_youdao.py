# coding=utf-8
from selenium import webdriver
import unittest,time
class Mytest(unittest.TestCase):
    '''测试有道搜索'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = 'http://youdao.com'
    def test_youdao(self):
        '''搜索关键字：webdriver'''
        driver = self.driver
        driver.get(self.base_url+'/')
        driver.find_element_by_id('translateContent').clear()
        driver.find_element_by_id('translateContent').send_keys('webdriver')
        driver.find_element_by_xpath('//*[@id="form"]/button').click()
        time.sleep(2)
        title = driver.title
        self.assertTrue('webdriver'  in title)
    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()