# coding=utf-8
import multiprocessing,time
def run(name):
    time.sleep(2)
    print('hello',name)
if __name__=='__main__':
    for i in range(10):
        p=multiprocessing.Process(target=run,args=('ht%s'%i,))
        p.start()