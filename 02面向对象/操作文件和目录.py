# coding=utf-8
import os
import time
import shutil
'''a=os.path.abspath('.')
print(a)
b=os.path.join(a,'testdir')
print(b)
os.mkdir(b)
time.sleep(5)
os.rmdir(b)
'''
#对文件重命名： os.rename('test.txt','a_test.py')
#删除文件：os.remove('a_test.py')
#复制文件的函数在os模块中没有，shutil模块提供了copyfile()函数进行复制。
#shutil.copyfile('F:\\jichu\\02面向对象\\文件.py','C:\\Users\\Administrator\\Desktop')