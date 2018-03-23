# coding=utf-8
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
time.sleep(1)
print(driver.current_window_handle)
driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a").click()
print(driver.current_window_handle)  # 输出当前窗口句柄
handles = driver.window_handles  # 获取当前全部窗口句柄集合
print(handles)  # 输出句柄集合
for i in range(2) :
    for handle in handles:  # 切换窗口
        # if handle != driver.current_window_handle:
        #     print('switch to second window', handle)
        #driver.close()  # 关闭第一个窗口
        time.sleep(1)
        driver.switch_to.window(handle)  # 切换到第二个窗口
driver.quit()