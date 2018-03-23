# coding=utf-8
import time ,threading
event=threading.Event()
def lighter():
    count=1
    while True :
        if count>5 and count<11 :
            print('red light is on')
            event.clear()  # 把标志位清除
        else :
            print("green light is on ")
            event.set()
        time.sleep(1)
        if count==10:
            count=1
        else:
            count+=1
def car(name):
    while True :
        if event.is_set():
            print('%s running...'%name)
            time.sleep(1)
        else:
            print('%s sees red light,waiting...'%name)
            event.wait()#等待被设置
            print('%s green light is on ,start going...'%name)
light=threading.Thread(target=lighter,)
car1=threading.Thread(target=car,args=('tesla',))
light.start()
car1.start()

