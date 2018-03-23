# coding=utf-8
from threading import Thread
from selenium import webdriver
from time import ctime,sleep
#测试用列
def test_baidu(index,search):
    print('start:%s'%ctime())
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_xpath('//*[@id="su"]').click()
    sleep(5)
    if search in driver.title :
        print('%s测试成功'%index)
    else:print('%s测试失败'%index)
    driver.quit()
if __name__ == '__main__' :
    # lists = ['chrome','python','threading','selenium','threading','selenium','chrome','python','threading','selenium']
    lists = list( map(lambda x : str(x)+'a',[x for x in range(5)]))
    threads = []
    files = range(len(lists))
    for i,value in enumerate(lists):
        t = Thread(target=test_baidu,args=(i,value))
        threads.append(t)
    for t in files :
        threads[t].start()
    for t in files:
        threads[t].join()
    print('end:%s'%ctime())