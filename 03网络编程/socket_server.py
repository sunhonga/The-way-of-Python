# Author：SUN HONG
import socket
server=socket.socket()
server.bind(("localhost",999))#绑定要监听的端口
server.listen(5)#监听的个数
conn,addr=server.accept()
while True :
    data=conn.recv(1024)
    print("recv:",data)
    conn.send(data.upper())
server.close()