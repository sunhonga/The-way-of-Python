# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://www.baidu.com/")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__submit']").click()
error_mes = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_8__error']").text
try:
    assert error_mes == u'请您填写手机/邮箱/用户名'
    print ('Test pass.')
except Exception as e:
    print ("Test fail.", format(e))