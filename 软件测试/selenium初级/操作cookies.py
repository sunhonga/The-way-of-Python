# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.youdao.com')
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbb'})
cookie = driver.get_cookies()
for i in cookie :

    print(i)
driver.quit()