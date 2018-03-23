# coding=utf-8
from selenium import webdriver
import time
d=webdriver.Firefox()
d.get('https://www.baidu.com/')
d.maximize_window()
d.find_element_by_id('kw').clear()
d.find_element_by_id('kw').send_keys('麦子学院')
time.sleep(1)
d.find_element_by_id('su').click()
time.sleep(1)
d.find_element_by_partial_link_text('专业IT职业教育平台').click()
time.sleep(10)
print(d.window_handles)
d.switch_to_window(d.window_handles[0])
d.current_window_handle

