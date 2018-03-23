# coding=utf-8
import time
from selenium import webdriver
class BrowserEngine(object):
    """
    定义一个浏览器引擎类，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE，Firefox, Chrome
    """
    def __init__(self, driver):
        self.driver = driver
    browser_type = "cc"  # maybe Firefox, Chrome, IE
    def get_browser(self):
        """
        通过if语句，来控制初始化不同浏览器的启动，默认是启动Chrome
        :return: driver
        """
        if self.browser_type == 'Firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'IE':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
if __name__ == '__main__' :
    import time
    # from test1.browser_engine import BrowserEngine
    class TestBrowserEngine(object):
        def open_browser(self):
            browserengine = BrowserEngine(self)
            driver = browserengine.get_browser()
            return driver

    tbe = TestBrowserEngine()
    tbe.open_browser().get('http://www.baidu.com')
    time.sleep(2)
