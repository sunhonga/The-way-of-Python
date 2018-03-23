#生成6位随机验证嘛
import random
yanzhengma=''
for i in range(0,5):
    a=random.randint(0,1)
    if a==0:
        tmp=random.randint(0,9)
    else:
        tmp=chr(random.randint(65,90))
    yanzhengma+=str(tmp)
print(yanzhengma)
print(random.random())#随机取[0,1]中的数
print(random.randint(1,7))#随机取[1,7]中的整数
print(random.randrange(1,10))#随机取[1,10)中的随机整数
print(random.choice('helloword'))#随机取字符串的一个字符
print(random.choice([1,13,6,9]))#随机取列表的一个数字
print(random.sample('hello',2)) #随机取两个字符构成一个列表
print(random.uniform(1,10))#取[1,10]的随机浮点数