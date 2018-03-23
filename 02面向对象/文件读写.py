# Author：SUN HONG
'''
r只读模式，文件必须存在，不存在则抛出异常。默认模式   r+ 可读可写   写的时候是从文件最后面开始写
w只写模式，不可读，不存在则新建，存在则清空内容       w+写读  没什么用
a追加模式，可读，不存在则创建，存在则追加内容，指针自动移动到文件尾  a+可读可写
rb二进制文件 网络传输只能二进制
read(3),默认读所有，3表示读三个字节
readlines(),按行读取文件并且返回一个列表，每行一个列表的元素
readline（），从第一行依次读一行
tell(),返回指针位置，刚打开文件是值为0
seek（offest,[whence]），移动文件指针到制定位置,offset开始的偏移量，whence默认参数为0，表示要从哪个位置开始偏移，
                         0表示从文件开头开始算起，1代表当前位置开始算起，2表示从文件末尾算起。
'''
f=open("yesterday2.txt","w",encoding="utf8")#文件句柄
f.write("灰太狼abc\n红太狼ab\n喜羊羊a\n美羊羊\n沸羊羊\n小灰灰\n红太阳")
f=open("yesterday2.txt",encoding="utf8")
#print(f.read(3))
#list=f.readlines()
count=0
for line in f:           #一行一行的读文件
    if count==3:
        print("-----我是分割符-----")
        count += 1
        continue
    print(line)
    count+=1

#f.colse()
#f=open("yesterday2.txt",encoding="utf8")
#print(f.read(3))
