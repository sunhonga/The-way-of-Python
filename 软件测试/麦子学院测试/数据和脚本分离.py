# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)
def openBrower(x):
   if x == 'F' :
        return webdriver.Firefox()
   elif (x == 'C') :
        return webdriver.Chrome(chrome_options=option)
def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()
    # time.sleep(5)
def findElement(d,arg):
    if 'text_id' in arg :
        ele_login=get_ele_times(d,20,lambda d: d.find_element_by_link_text(arg['text_id']))
        # time.sleep(5)
        # ele_login = d.find_element_by_link_text(arg['text_id'])
        ele_login.click()
    useEle = d.find_element_by_xpath(arg['userxpath'])
    pwdEle = d.find_element_by_xpath(arg['pwdxpath'])
    loginEle = d.find_element_by_xpath(arg['loginxpath'])
    tuple1 = (useEle,pwdEle,loginEle)
    return tuple1
def sendVals(eletuple,arge):
    listkey=['uname','pwd']
    i=0
    for key in listkey :
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arge[key])
        i=i+1
    eletuple[2].click()
def checkResult(d,text):
    try :
        d.find_element_by_link_text(text)
        print('Account And Pwd Error')
    except :
        print("Account And Pwd Right!")
def login_test(ele_dict,user_list):
    d=openBrower('C')
    openUrl(d,ele_dict['url'])
    ele_tuple=findElement(d,ele_dict)
    for arg in user_list :
        sendVals(ele_tuple,arg)
        checkResult(d,'该帐号格式不正确')
if __name__ == '__main__':
    url = 'https://www.maiziedu.com/'
    login_text = '登录'
    account = 'maizi_test@139.com'
    pwd = "abc123456"
    ele_dict={'text_id':login_text,'userxpath':'//*[@id="id_account_l"]',\
              'pwdxpath':'//*[@id="id_password_l"]','loginxpath':'//*[@id="login_btn"]',\
              'url':url}
    user_list = [{'uname': account, 'pwd': pwd}]
    login_test(ele_dict,user_list)

