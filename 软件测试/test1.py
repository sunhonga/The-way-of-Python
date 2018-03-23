# coding=utf-8
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
driver.implicitly_wait(8)  # 设置隐式时间等待

driver.get("https://www.baidu.com")







