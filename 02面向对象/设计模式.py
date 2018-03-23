'''
   #__new__ 方法 构建当前类的对象
   class User(object):
         def __init__(self,name,password):
              self.name=name
              self.password=password
         print("对象已经建立好了，由解释器自动回调的init方法，对象初始划")
         #new方法是当对象构建的时候由解释器自动回调的方法，改方法必须返回当前的类的对象。
         #这里重写父类这个方法，不重写解释器直接调用object中的__new__方法。
         def __new__ (cls,name,password)：
              print("User类的对象开始构建")
              return object.__new__(cls)   #必须要有返回值，没得对象就构建不成功。
          #不定义__str__方法，print(u)时会输出系统默认的文本。改方法也必须有返回值。
          def __str__(self):
              return "用户名%s,密码%s"%(self.name,self.password)
   u=User("zs","123")
   print(u)
   __del__方法 销毁一个对象
   python 设计模式
   单例模式：一个类只有一个对象
'''
   #实现单例
class User(object):
    __instance=None
    def __init__(self,name):
            self.name=name
    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance=object.__new__(cls)

        return  cls.__instance
u1=User("张三")
u2=User("李四")
print(u1==u2) #==判断表达式如果返回True，这两个对象是一个个对象，并且内存地址相同。
print("u1对象的内存地址：%s,u2对象的内存地址：%s"%(id(u1),id(u2)))
#python没有绝对化的单例 如下
u3=object.__new__(User)
#简单工厂模式
