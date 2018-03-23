# coding=utf-8
import re
print(re.findall(r'你好','你好大的你好你好好好'))
print(re.findall(r'你好好','你好大的你好你好好好'))
class L():
    def __str__(self):
        return self.__class__.__name__
a = L()
print(a)