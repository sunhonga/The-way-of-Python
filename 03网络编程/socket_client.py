# Author：SUN HONG
import socket
client=socket.socket()  #申明socket类型，同时生成socket连接对象
client.connect(('localhost',999))
while True :
    msg=input(">>:").strip()
    if len(msg)==0 :continue
    client.send(msg.encode())
    data=client.recv(1024)
    print("recv:",data.decode())
client.close()