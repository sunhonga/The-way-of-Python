# coding=utf-8
from urllib import  request
re = request.urlopen('http://www.baidu.com', data = None, timeout = 10)
def progess(blk,blk_size,total_size) :
    print('%d/%d - %0.02f%%' %(blk*blk_size,total_size,blk*blk_size*100/total_size  ))
fname,msg = request.urlretrieve('http://blog.kamidox.com','index.html',reporthook=progess)
print(fname)
print(msg.items())  #返回解析过的头的信息，是一个列表，每个列表元素由一个元祖组成，元祖（字段名称，字段值）
print(re.info())
