# coding=utf-8
import requests
r = requests.get("http://www.sina.com/")
print(r.status_code)
# print(r.json())
print(r.headers)
print(r.headers.get("set-cookie"))
print(type(r))
