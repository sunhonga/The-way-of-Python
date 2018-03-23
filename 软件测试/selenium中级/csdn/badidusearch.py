# coding=utf-8
import time
import sys
sys.path.append('./test1')
from selenium import webdriver
from pgtest1.basepage import BasePage
# import test1.basepage.Basepage
class BaiduSearch(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    basepage = BasePage(driver)
    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(2)
    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("Selenium")
        time.sleep(2)
        self.basepage.back()
        time.sleep(2)
        self.basepage.forward()
        time.sleep(2)
        self.basepage.quit_browser()
baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()
