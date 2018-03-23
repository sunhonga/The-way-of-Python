'''
  在python中，所有数据类型都可以视为对象，当然也可以自定义对象。面向对象的抽象程度比函数要高，因为一个Class即包含数据，又包含操作数据的方法。
  面向对象的三大特点：数据封装、继承和多态。  python中面向对象有很多高级特性，多重继承、定制类、元类。
  定义一个类：
  class Student(object):
        pass
  创建一个对象
  zhangsan=Student()
  给对象绑定属性
  zhangsan.age=27
  zhangsan.sex="男"
  在创建对象的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的_init_方法，在创建对象的时候，就把name，sex等属性绑上去。
  class Student（object）:
        def _init_(self,age,sex):
            self.age=age
            self.sex=sex
  lisi=Student(35,"女")
  数据封装
          类是创建对象的模板，各个对象拥有的数据都相互独立，互不影响。
          方法就是与对象绑定的函数，和普通函数不同，方法可以直接访问对象的数据。
          通过对象上调用方法，我们就直接操作了对象的数据，但无需知道方法内部的实现细节。
          和静态语言不同，python允许对对象变量绑定任何数据，也就是说，对于两个对象变量，虽然它们都是同一个类的不同对象，但拥有的变量名称都可能不一样。
  方问限制
          如果内部属性不被外部访问，可以把属性的名称前加上双划线__,在python中，对象的变量名如果以__开头，就变成类一个私有变量（private）,只有内部可以访问，外部不能访问。
          class Student(object):
                def _init_(self,age,sex):
                    self.__age=age
                    self.__sex=sex
          这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
  继承和多态
          在OOP编程设计中，当我们定义一个class的时候，可以从某个现在的class继承，新的class称为子类，而被继承的class称为父类。
          继承的好处：子类获得了父类的全部功能。
          当子类和父类都存在相同的方法时，我们说，子类的方法覆盖了父类的方法，在代码运行的时候，总是会调用子类的方法。这样，我们就获得了继承的另一个好处：多态。
          我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类型和python自带的数据类型，比如str、list、dict没什么两样。
          a=list()#a是；list类型
          b=Animal()#b是：Aniaml类型
          c=Dog()#c是：Dog类型       Dog类是继承Animal类的（前面没写）
          判断一个变量是否是某个类型可以用isinstance()判断:
                isinstance(a,list)   反回值为True
           c不仅仅是Dog类型,c还是Animal类型 所以，在继承关系中，如果一个对象的数据类型是某个子类，那它的数据类型也可以被看做是父类。但反过来就不行。
  对象属性和类属性
          class Student():
                name="Student"     公共的类属性
                __password="123456"  私有类属性
                def _init_(self,name,sex)
                     self.name=name    对象的属性
                     self.sex=sex
          s=Student()#创建对象s
          print(s.name)#打印name属性，因为对象没有name属性，所以会继续查找class的name属性   输出结果为Student
          print(Student.name)#打印类的属性
          s.name="michal" #给对象绑定name属性
          print(s.name)  #由于对象属性优先级比类属性高，因此，它会屏蔽掉类的name属性  输出结果为michal
          print(Student.name)  #但是类属性并未消失，用Student.name仍然可以方位   输出结果为Student
          class yinianji_Student(Student):
                pass
          zhangsan=Student(zhangsan,男)
          print(yinianji_Student.name)
          print(zhangsan.name)
   类的方法和对象的方法
         class A(object):
               name="zs"
               def test1(self):
                    print("....A 的test1方法")
               @classmethod #类方法一定要在方法上面加上一个修饰器，类方法的参数cls,代表当前的类
               def test2(cls):
                   cls.name="ww"
                   print("....A的test2方法")
               @staticmethod#静态方法，属于类，没有默认传递的参数，可以通过类对象来调用，也可以通过类名来调用
               def test3():
                    A.mane="ls"
                    print("....A的test3静态方法")
          a=A()
          a.test2()
          A.test2()
          A.test3()
          print(A.name)
'''
from types import MethodType
class Student(object):
    __slots__ = ('name','age')
    pass
s = Student()
s.name = '灰太狼'
print(s.name)
# def set_age(self,age):
#     self.age = age
# s.set_age = MethodType(set_age,s)   #给实例绑定方法，对另一个实例不起作用
# s.set_age(25)
# print(s.age)
#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score
Student.set_score = MethodType(set_score,Student)
#如果只允许对Student实例添加name和age属性，使用__slots__  修改上方Student类,
#注意 __slots__ 定义的属性仅对当前类实例起作用
class Animal (object):
    def __init__(self,name):
        self.__name = name
dog = Animal('abc')
print(dog.__name)
#__name  这样的变量是内部变量，不能被外部访问。只能被Animal里面的方法访问