# coding=utf-8
from selenium import webdriver
import time
d=webdriver.Firefox()
d.get(r'F:\jichu\软件测试\alter对话框处理.html')
d.find_element_by_id('alter').click()
time.sleep(2)
alter=d.switch_to_alert()
print(alter.text)
time.sleep(2)
alter.accept()