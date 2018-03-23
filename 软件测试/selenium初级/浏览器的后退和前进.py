# coding=utf-8
from selenium import webdriver
import  time
b = webdriver.Chrome()
b.maximize_window()
b.get('https://www.baidu.com/')
b.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
print(b.capabilities['version'])  #获取浏览器的版本号
print(b.current_url)          #获得当前页面的URL
print(b.title)
for i in range(100) :
    time.sleep(2)
    b.back()   #浏览器后退
    time.sleep(2)
    b.forward() #浏览器前进
