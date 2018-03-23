# coding=utf-8
from selenium import webdriver
import time
b = webdriver.Chrome()
b.set_window_size(1000,500)  #自定义设置浏览器窗口大小
b.implicitly_wait(5)
b.get('http://news.baidu.com/')
ele = b.find_elements_by_xpath('//*[@type="radio"]')
for i in ele :
    time.sleep(2)
    i.click()

