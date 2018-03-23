# coding=utf-8
from selenium.webdriver import Remote
from selenium import webdriver
def browser():
    #driver = webdriver.Chorme()
    #host = '127.0.0.1:4444'
    #根据我们的实际需求，配置测试用例在不同的主机及浏览器下运行。
    dc = {'browserName':'chrome','platform':'ANY','version':'','javascriptEnable':True}
    driver = Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=dc)
    return driver
if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com/')
