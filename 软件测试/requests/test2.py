# coding=utf-8
import urllib
def urlencode():
    params = {'score': 100,'name':'爬虫基础','comment':'very good'}
    qs = urllib.urlencode(params)
    print(qs)
if __name__ == '__main__':
    urlencode()