'''strs[start:end:step]
   1.step缺省值为1
   2.step为正时，start为空，默认为负无穷；end为空，默认为正无穷。如果start＞end，则为空。
   3.step为负时，start为空，默认为正无穷；end为空，默认为负无穷。如果start＜end，则为空。
'''
strs="123456789"
#步长为正时
print(strs[0:2]) #输出为12
print(strs[0:-1])#输出为12345678    -1相当于正向的index为8，即strs[0:1]=strs[0:8]
print(strs[:-1])#输出为12345678
print(strs[:])#输出为123456789
print(strs[5:1])#输出为空
print(strs[-1:0])#输出为空    相当于strs[-1:0]=strs[8:0] 8＞0，所以为空
print(strs[::2])#输出为13579
#步长为负时
print(strs[-1:0:-1])#输出为98765432
print("反转字符串")
print(strs[-1::-1])#输出为987654321，改操作为反转字符串
print(strs[::-1])#也是反转字符串