# coding=utf-8
with open(r"C:\Users\Administrator\Desktop\1.txt",'r') as f:
    for line in f.readlines():
        print(line.strip())
with open(r"C:\Users\Administrator\Desktop\2.txt",'w') as f1:
    f1.write("孙洪 灰太狼")
