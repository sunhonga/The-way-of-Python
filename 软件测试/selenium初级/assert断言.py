# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get('https://www.baidu.com/')
try :
    assert '百度一下' in driver.title
    print('assertion test pass')
except Exception as e :
    print('assert test fail',format(e))