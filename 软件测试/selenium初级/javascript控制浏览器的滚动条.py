# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.set_window_size(700,600)
driver.find_element_by_id('kw').send_keys('selenium')
btn = driver.find_element_by_id('su')
btn.click()
print(btn.is_displayed())
time.sleep(5)
js = "window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(5)
driver.quit()
