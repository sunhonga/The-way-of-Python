# Author：SUN HONG
'''
1.数字:int整型、float浮点型、复数complex 5+4j
2.布尔值：真或假=1或0
3.三元运算：result=值1 if 条件 else 值2
4.16进制以大写H表示
5.bytes类型：二进制由bytes数据表示，字符串和二进制分开，二进制和字符串的相互转化。
            字符串到二进制："孙洪".encode("utf-8")   说明该字符串为utf-8编码，python3默认为utf-8
            二进制到字符串：b'\xe5\xad\x99\xe6\xb4\xaa'.decode("utf-8")
            网络编程用
'''
print("孙洪".encode("uyf-8"))#utf-8可以不写，python3默认utf-8编码
print(b'\xe5\xad\x99\xe6\xb4\xaa'.decode("utf-8"))