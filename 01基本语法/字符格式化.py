# Author：SUN HONG
name=input("输入你的名字")
age=input("输入你的年龄")
salary=input("输入你的薪水")
info1='''
----------info of {0}----------
name:{0}
age:{1}
salary:{2}
'''.format(name,age,salary)
print(info1)
info2='''
----------info of %s----------
name:%s
age:%s
salary:%s
'''%(name,name,age,salary)
print(info2)