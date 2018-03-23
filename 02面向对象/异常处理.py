'''
   所有的异常都继承Exception父类
   捕获异常
   try:  #是异常捕获开始代码，try放在特别关心的那段代码前面。
      代码  #如果这行运行代码出现了异常，那么后面的代码不会执行
      代码
      ...
    except 错误类型 as 把错误赋值给谁：#按照顺序依次比对类型，对上了后面的except就不对比。
    except
    ...
    else:  #没有异常时执行
    finally: #不管有没有异常都会执行
'''
try:
    print(a)
    i=1/0  #第三行没有执行
    print("hello")
except (NameError,ZeroDivisionError) as ex:   #ex代表刚刚捕获的异常对象
    print("出现异常了")
    print(ex)

#自定义异常
class PasswordException(Exception):
    del __init__(self,pw,min_length):
        self.password=pw
        self.min_length=min_length
    del __str__(self):
        return "%s的密码错误，密码的最小长度为%s"%(self.password,self.min_length)
def reg(username,password):
    if len(password)<6:
        raise PasswordException(password,6)
    else:
        print("用户名为：%s,密码为：%s"%(username,password))
try:
    reg("zs","12345")
except Exception as ex:
    print(ex)



