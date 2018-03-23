# coding=utf-8
import os
'''查找最新的测试报告'''
result_dir = 'F:\\jichu\\web测试用例\\report'           #定义文件目录
lists = os.listdir(result_dir)
lists.sort(key=lambda x : os.path.getmtime(result_dir+'\\'+x))
print(lists[-1])
file = os.path.join(result_dir,lists[-1])
print(file)