# coding=utf-8
print('nihao')
'''
多态即多种形态，在运行时确定其状态，在编译阶段无法确定其类型，这就是多态。
Python中的多态和Java以及C++中的多态有点不同，Python中的变量是弱类型的，
在定义时不用指明其类型，它会根据需要在运行时确定变量的类型（个人觉得这也是多态的一种体现），
并且Python本身是一种解释性语言，不进行预编译，因此它就只在运行时确定其状态，
故也有人说Python是一种多态语言。在Python中很多地方都可以体现多态的特性，
比如内置函数len(object)，len函数不仅可以计算字符串的长度，还可以计算列表、元组等对象中的数据个数，
这里在运行时通过参数类型确定其具体的计算过程，正是多态的一种体现。这有点类似于函数重载（一个编译单元中有多个同名函数，但参数不同），
相当于为每种类型都定义了一个len函数。这是典型的多态表现。有些朋友提出Python不支持多态，我是完全不赞同的。
本质上，多态意味着可以对不同的对象使用同样的操作，但它们可能会以多种形态呈现出结果。len(object)函数就体现了这一点。
在C++、Java、C#这种编译型语言中，由于有编译过程，因此就鲜明地分成了运行时多态和编译时多态。
运行时多态是指允许父类指针或名称来引用子类对象，或对象方法，而实际调用的方法为对象的类类型方法，
这就是所谓的动态绑定。编译时多态有模板或范型、方法重载（overload）、方法重写（override）等。
而Python是动态语言，动态地确定类型信息恰恰体现了多态的特征。在Python中，任何不知道对象到底是什么类型，
但又需要对象做点什么的时候，都会用到多态。
能够直接说明多态的两段示例代码如下：
'''
# 方法多态:
# _metaclass_ = type  # 确定使用新式类
# class calculator:
#     def count(self, args):
#         return 1
# calc = calculator()  # 自定义类型
# from random import choice
# obj = choice(['hello,world', [1, 2, 3], calc])  # obj是随机返回的 类型不确定
# print(type(obj))
# print(obj.count('a'))  # 方法多态
# print('list'.count('a'))
'''
对于一个临时对象obj，它通过Python的随机函数取出来，不知道具体类型（是字符串、元组还是自定义类型），
都可以调用count方法进行计算，至于count由谁（哪种类型）去做怎么去实现我们并不关心。
'''
# 有一种称为”鸭子类型（duck typing）“的东西，讲的也是多态：
class Duck:
    def quack(self):
        print
        "Quaaaaaack!"
    def feathers(self):
        print("The duck has white and gray feathers.")
class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
def in_the_forest(duck):
    duck.quack()
    duck.feathers()
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
game()
'''就in_the_forest函数而言，参数对象是一个鸭子类型，它实现了方法多态。但是实际上我们知道，
从严格的抽象来讲，Person类型和Duck完全风马牛不相及。'''
#运算符多态
def add(x, y):
    return x + y
print(add(1, 2))  # 输出3
print(add("hello,", "world"))  # 输出hello,world
print(add(1, "abc"))  # 抛出异常 TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''上例中，显而易见，Python的加法运算符是”多态“的，理论上，我们实现的add方法支持任意支持加法的对象，
但是我们不用关心两个参数x和y具体是什么类型。
'''
# Python同样支持运算符重载，实例如下：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)