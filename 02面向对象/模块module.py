'''
   module:模块就好比是工具包，想要使用这个工具包中的工具（就好比函数），就需要导入这个模块。
   导入方法：
           1.import random
           2.from random import 接random模块的方法
           3.form random import* （*代表所有）很少用这种方法
           4.如果模块名特别长可以用：import random as ra
    标注库：不需要安装，直接用，python很多常用功能   安装在C:\\Program Files\\Anaconda3\\Lib下
          sys模块
          os模块
    第三方库：必须安装才能使用  C:\\Program Files\\Anaconda3\\ib\\site-packages下 自己写的模块也可以放在这个目录下，然后可以
              正常调用，同时模块在同一个目录下依然可以调用。
     python3.5的pyc

'''
import sys
import os
print(sys.path)#打印环境变量
print(sys.argv)#把脚本的绝对路径打印出来了
#print（sys.argv[2]）  以后脚本测试不懂看这儿
#cmd_res=os.system("dir")#执行命令，不保存结果
cmd_res=os.system("dir").read()
print("--＞",cmd_res)
os.mkdir("new_dir")#在当前目录下创建new_dir的一个文件。