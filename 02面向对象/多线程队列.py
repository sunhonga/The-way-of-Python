# coding=utf-8

import queue
q1=queue.Queue(maxsize=5)# 先进先出
q2=queue.LifoQueue(maxsize=5)#后进先出
q3=queue.PriorityQueue(maxsize=5)
q1.put(1)
q1.put(2)
q1.put(3)
q2.put(1)
q2.put(2)
q2.put(3)
q3.put('htl',-5)
q3.put('xyy',5)
q3.put('xhh',10)
print(q1.qsize())#判断队列的长度
print('======')
print(q1.get())
print(q1.get())
print(q1.get())
print(q2.get())
print(q2.get())
print(q2.get())
print(q3.get())
print(q3.get())
print(q3.get())
