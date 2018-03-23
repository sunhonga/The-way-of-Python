from selenium import webdriver
browser=webdriver.Firefox()
print(u'页面加载')
browser.get("https://www.baidu.com")
print(u'完成')