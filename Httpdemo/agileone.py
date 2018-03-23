# coding=utf-8
import requests

def agileine():
    url = "http://localhost/agileone/"
    headers = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
                }
    r1 = requests.get(url,headers=headers)
    print(r1.status_code)

    r2 = requests.post("http://localhost/agileone/index.php/common/login",
                       data={'username':'admin',
                             'password':'admin','savelogin':'false'}
                       )
    c1 = r2.cookies.get_dict()
    r2.encoding = "utf-8"
    print(c1)
    print(r2.text)
    r3 = requests.get("http://localhost/agileone/index.php/notice",cookies=c1)
    r3.encoding = "utf-8"
    print(r3.text)

session = requests.session()
r1 = session.post("http://localhost/agileone/index.php/common/login",
                       data={'username':'admin',
                             'password':'admin','savelogin':'false'}
        )
c1 = r1.cookies.get_dict()
r1.encoding = "utf-8"
print(c1)
print(r1.text)
r2 = session.get("http://localhost/agileone/index.php/notice")
r2.encoding = "utf-8"
print(r2.text)

