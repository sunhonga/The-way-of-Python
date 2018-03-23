# coding=utf-8

class Person(object):

    def hello(self):
        print("hello")

    @classmethod
    def nihao(cls):
        print("nihao")

p1 = Person()
p1.hello()
Person().hello()

try:
    Person.hello()
except Exception:
    print('Person.hello()' + "出错了")

Person.nihao()
p1.nihao()