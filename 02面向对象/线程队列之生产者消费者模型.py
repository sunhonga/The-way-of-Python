# coding=utf-8
import threading,time,queue
q=queue.Queue(maxsize=10)
def Producer(name):
    count = 1
    while True :
        q.put('骨头%s'%count)
        print('生产了骨头',count)
        count +=1
def Consumer(name):
    while True :
        print('<%s>取到<%s>并且吃了它'%(name,q.get()))
        time.sleep(1)
s=threading.Thread(target=Producer,args=("孙洪",))
a=threading.Thread(target=Consumer,args=("啊黄",))
b=threading.Thread(target=Consumer,args=("灰太狼",))
s.start()
a.start()
b.start()