from socket import *

server_addr=("127.0.0.1",9422)
#创建tcp套接字
tcp_socket=socket()

#发起连接
tcp_socket.connect(server_addr)

#发送接收消息
while True:
    msg=input(">>")
    tcp_socket.send(msg.encode())
    if msg=="##":
        break
    data = tcp_socket.recv(20)
    print("从服务器收到：",data.decode())


tcp_socket.close()




