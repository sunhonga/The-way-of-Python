# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://www.baidu.com/")
time.sleep(1)
ele = driver.find_element_by_id('kw')
ele.send_keys('selenium')
time.sleep(3)
ele.send_keys(Keys.CONTROL,'a')  #全选
time.sleep(3)
ele.send_keys(Keys.CONTROL,'x')  #剪切
time.sleep(3)
ele.send_keys('三脚架')
time.sleep(2)
ele.send_keys(Keys.BACKSPACE) #退格

# try:
#     driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL , 't')  # 触发ctrl + t
#     print('打开')
# except Exception as e:
#     print('出错了')
# time.sleep(1)