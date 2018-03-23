# coding=utf-8
from time import sleep
from selenium import webdriver
d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(5)
d.get('https://www.baidu.com.cn/')
d.get_screenshot_as_file('C:\\Users\\Administrator\\Desktop\\baidu.png')