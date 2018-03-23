# coding=utf-8
from selenium import webdriver
import time
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
url = 'https://www.maiziedu.com/'
ligon_text='登录'
account = 'maizi_test@139.com'
pwd = "abc123456"
def login_test():
    d = webdriver.Chrome(chrome_options=option)
    d.get(url)

    # d=webdriver.Firefox()#本机打开需要38秒
    # d.get(url)
    d.maximize_window()
    # time.sleep(30)
    d.find_element_by_link_text(ligon_text).click()
    time.sleep(2)
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
