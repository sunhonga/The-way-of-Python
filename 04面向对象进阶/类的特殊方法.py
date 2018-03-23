# coding=utf-8
class People(object):
    def __getitem__(self, item):
        return self.__dict__[item]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
p = People()
p['name']= 'lisi'
print(p['name'])