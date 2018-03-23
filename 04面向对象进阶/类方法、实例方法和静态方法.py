# coding=utf-8
print('nihao ')
'''
类方法：
是类对象所拥有的方法，需要用修饰器"@classmethod"来标识其为类方法，对于类方法，
第一个参数必须是类对象，一般以"cls"作为第一个参数（当然可以用其他名称的变量作为其第一个参数，
但是大部分人都习惯以'cls'作为第一个参数的名字，就最好用'cls'了），能够通过实例对象和类对象去访问。
'''
# class people:
#     country = 'china'
#     # 类方法，用classmethod来进行修饰
#     @classmethod
#     def getCountry(cls):
#         return cls.country
# p = people()
# print(p.getCountry())  # 可以用过实例对象引用
# print(people.getCountry())  # 可以通过类对象引用
'''类方法还有一个用途就是可以对类属性进行修改：'''
# class people:
#     country = 'china'
#     # 类方法，用classmethod来进行修饰
#     @classmethod
#     def getCountry(cls):
#         return cls.country
#     @classmethod
#     def setCountry(cls, country):
#         cls.country = country
# p = people()
# print(p.getCountry()) # 可以用过实例对象引用
# print(people.getCountry())  # 可以通过类对象引用
# p.setCountry('japan')
# print(p.getCountry())
# print(people.getCountry())
'''实例方法：
在类中最常定义的成员方法，它至少有一个参数并且必须以实例对象作为其第一个参数，
一般以名为'self'的变量作为第一个参数（当然可以以其他名称的变量作为第一个参数）。
在类外实例方法只能通过实例对象去调用，不能通过其他方式去调用。'''
# class people:
#     country = 'china'
#     # 实例方法
#     def getCountry(self):
#         return self.country
# p = people()
# print(p.getCountry())  # 正确，可以用过实例对象引用
# print(people.getCountry())  # 错误，不能通过类对象引用实例方法
'''静态方法：
需要通过修饰器"@staticmethod"来进行修饰，静态方法不需要多定义参数。'''
class people:
    country = 'china'
    @staticmethod
    # 静态方法
    def getCountry():
        return people.country
p = people()
print(p.getCountry()) #正确
print(people.getCountry()) #正确
'''
对于类属性和实例属性，如果在类方法中引用某个属性，该属性必定是类属性，
而如果在实例方法中引用某个属性（不作更改），并且存在同名的类属性，
此时若实例对象有该名称的实例属性，则实例属性会屏蔽类属性，即引用的是实例属性，
若实例对象没有该名称的实例属性，则引用的是类属性；如果在实例方法更改某个属性，
并且存在同名的类属性，此时若实例对象有该名称的实例属性，则修改的是实例属性，
若实例对象没有该名称的实例属性，则会创建一个同名称的实例属性。想要修改类属性，
如果在类外，可以通过类对象修改，如果在类里面，只有在类方法中进行修改。
从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，
那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，
那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），
不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。'''