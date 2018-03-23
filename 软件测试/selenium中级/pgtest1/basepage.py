# coding=utf-8
class BasePage(object):
    """
    主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
    quit()
    """
    def __init__(self, driver):
        """
        写一个构造函数，有一个参数driver
        :param driver:
        """
        self.driver = driver
    def back(self):
        """
        浏览器后退按钮
        :param none:
        """
        self.driver.back()
    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()
    def open_url(self, url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)
    def quit_browser(self):
        """
        关闭并停止浏览器服务
        :param none:
        """
        self.driver.quit()