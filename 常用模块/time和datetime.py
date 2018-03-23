import time
import  datetime
#time的相关操作
print(time.time())  #获取时间戳，1970到现在的秒数
a=time.time()/(3600*24*365)
print(a)
print(time.timezone)  #距离本初子午线的秒数
print(time.timezone/3600) #显示8.我们位于东八区
#time.sleep(2)    #程序睡眠两秒
x=time.localtime() #将本地时间转换为元组
print(x)
print(x.tm_year)
print(time.mktime(x))  #元祖时间转化到时间戳
print(time.strftime('%y-%m;%d %H:%M:%S',x))#将元祖时间转化为格式化的字符串
print(time.strptime('17-12;14 10:08:58','%y-%m;%d %H:%M:%S'))#将格式化的字符串转化为元祖时间
#time.struct_time(tm_year=2017, tm_mon=12, tm_mday=14, tm_hour=10, tm_min=8, tm_sec=58, tm_wday=3, tm_yday=348, tm_isdst=-1)
print(time.asctime(x))  #将元祖转化为字符串格式的时间 Thu Dec 14 10:57:32 2017
print(time.ctime(time.time())) #将时间戳转为字符串格式的时间 Thu Dec 14 10:57:32 2017
#datetime的相关操作
print("----"*5)
#print(datetime.date)
#print(datetime.date())
print(datetime.datetime.now())
c_time=datetime.datetime.now()
#print(c_time.replace(minute=3,hour=2))#替换时间