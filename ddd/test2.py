# coding=utf-8


list = [x for x in range(101)]
print(list)

print(list[1::2])

print(map(lambda x:x+3,list))
print(sum(list))
print(sum(map(lambda x:x+3,list[1::2])))

list2 = [-2, 1, 3, -6]

list2.sort(key=abs,reverse=True)
print(list2)