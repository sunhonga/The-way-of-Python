# coding=utf-8
from selenium import selenium
sel = selenium('localhost',4444,'*chrome','http://www.baidu.com/')
sel.start()
sel.open('/')
sel.type('id=kw','selenium grid')
sel.click('id=su')
sel.wait_for_page_to_load('30000')
sel.stop()