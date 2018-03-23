# Author：SUN HONG
'''bytes类型：二进制由bytes数据表示，字符串和二进制分开，二进制和字符串的相互转化。
            字符串到二进制："孙洪".encode("utf-8")   说明该字符串为utf-8编码，python3默认为utf-8
            二进制到字符串：b'\xe5\xad\x99\xe6\xb4\xaa'.decode("utf-8")
            网络编程用
'''
str1="孙洪"
print(str1.encode(encoding="gbk"),type(str1))#utf-8可以不写，python3默认utf-8编码,encoding=gbk说明str1编码为gbk
print(b'\xe5\xad\x99\xe6\xb4\xaa'.decode())