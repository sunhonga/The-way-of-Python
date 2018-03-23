from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
driver = webdriver.Chrome(chrome_options=options)
browser=webdriver.Chrome()
print(u'页面加载')
browser.get("https://www.baidu.com")
print(u'完成')