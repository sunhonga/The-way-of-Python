# coding=utf-8
import time
import threading
start_time=time.time()
t_objs=[]
def run(self):
    print('task',self)
    time.sleep(2)
    print('runnint task',self,threading.current_thread())
for i in range(50):
    t=threading.Thread(target=run,args=('t-%s'%i,))
    # t.setDaemon(True)#把当前进程设为守护进程
    t.start()
    t_objs.append(t)
for t in t_objs:
    t.join()
print('----all threads has finished----',threading.current_thread(),threading.active_count())
print('cost;',time.time()-start_time)