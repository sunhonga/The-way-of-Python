# coding=utf-8
import os
result_dir = 'F:\jichu\ddd'

list = os.listdir(result_dir)

print(list)

list.sort(key=lambda fn : os.path.getmtime(result_dir + '\\' + fn))

print(list[-1])

file = os.path.join(result_dir,list[-1])
print(file)