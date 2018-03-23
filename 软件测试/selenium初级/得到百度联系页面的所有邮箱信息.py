# coding=utf-8
from selenium import webdriver
import re
import time

b = webdriver.Chrome()
b.maximize_window()
b.implicitly_wait(5)
b.get('http://home.baidu.com/contact.html')
data = b.page_source
emails = re.findall(r'[\w]+@[\w]+\.com',data)
for i in emails :
    print(i)
for i in range(100) :
  b.refresh()  #刷新页面
  time.sleep(1)