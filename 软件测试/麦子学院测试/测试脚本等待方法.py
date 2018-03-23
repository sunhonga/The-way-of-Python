# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
'''d=webdriver.Firefox()
d.get("http://www.baidu.com")
d.find_element_by_id('kw').send_keys('麦子学院')
d.implicitly_wait(5)     #该方法是针对所有元素，5秒找不到就会抛出异常
d.find_element_by_id('kw1')   #查找kw1这个元素的时间为五秒。
'''
url = 'https://www.maiziedu.com/'
login_text = '登录'
account = 'maizi_test@139.com'
pwd = "abc123456"
def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)
def login_test():
    d=webdriver.Firefox()#本机打开需要38秒
    d.get(url)
    d.maximize_window()
    # time.sleep(30)
    # d.find_element_by_link_text(login_text).click()
    ele_login=get_ele_times(d,10,lambda d : d.find_element_by_link_text(login_text))
    ele_login.click()

    account_ele = d.find_element_by_id('id_account_l')
    time.sleep(2)
    account_ele.clear()
    account_ele.send_keys(account)
    pwd_ele=d.find_element_by_id('id_password_l')
    pwd_ele.clear()
    pwd_ele.send_keys(pwd)
    d.find_element_by_id('login_btn').click()
    try :
        d.find_element_by_link_text('该账号格式不正确')
        print('Account And Pwd Error')
    except:
        print('Account And Pwd Right')
if __name__ == '__main__':
    login_test()
