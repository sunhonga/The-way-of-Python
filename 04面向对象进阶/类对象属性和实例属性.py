# coding=utf-8
#__init__方法
class MyClass(object):
    def __init__(self):
        print("MyClass类的构造方法被调用！")
class1 = MyClass()
'''
类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，
对于公有的类属性，在类外可以通过类对象和实例对象访问。'''
# class People:
#     name = 'jack'  # 公有的类属性
#     __age = 12  # 私有的类属性
# p = People()
# print(p.name)  # 正确
# print(People.name)  # 正确
# print(p.__age)  # 错误，不能在类外通过实例对象访问私有的类属性
# print(People.__age)  # 错误，不能在类外通过类对象访问私有的类属性

'''实例属性
实例属性是不需要在类中显示定义的'''
# class people1:
#     name = 'jack'
# p = people1()
# p.age = 12
# print(p.name)  # 正确
# print(p.age)  # 正确
# print(people1.name)  # 正确
# print(people1.age)  # 错误
'''在类外对类对象people1进行实例化之后，产生了一个实例对象p，
然后p.age = 12这句给p添加了一个实例属性age，赋值为12。
这个实例属性是实例对象p所特有的，注意，
类对象people1并不拥有它（所以不能通过类对象来访问这个age属性）。'''

'''
如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。
如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，
不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，
实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。'''
class people:
    country = 'china'
print(people.country)
p = people()
print(p.country)
p.country = 'japan'
print(p.country)  # 实例属性会屏蔽掉同名的类属性
print(people.country) #类的country属性没有变
del p.country  # 删除实例属性
print(p.country)
