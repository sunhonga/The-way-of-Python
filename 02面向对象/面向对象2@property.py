# coding=utf-8
class Student(object) :
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value <0 and value > 100 :
            raise ValueError('score musdt between 0~100!')
        self.__score = value
s = Student()
s.score = 60
print(s.score)
s.score = 90
print(s.score)
