'''
使用udp发送数据，每一次都要写上接收方的ip和port
在同一个os中，端口不允许相同，如果某个端口被使用，其他进程不允许使用该端口
'''
#全双工 套接字

from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)

#发送内容,senddata.encode("utf-8") ("gb2312")
senddata = "大美女你好"
udp_socket.sendto(senddata.encode("gb2312"),("192.168.1.107",8080))

#第二种发送内容的方式
#udp_socket.sendto(b"dameinv,("192.168.1.107",8080))
