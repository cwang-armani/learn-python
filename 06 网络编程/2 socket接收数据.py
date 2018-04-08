'''
使用udp发送数据，每一次都要写上接收方的ip和port
在同一个os中，端口不允许相同，如果某个端口被使用，其他进程不允许使用该端口
'''
#全双工 套接字

from socket import *
udp_socket = socket(AF_INET,SOCK_DGRAM)

#绑定本地的相关信息，如果⼀个⽹络程序不绑定，则系统会随机分配  
#一般接收方需要绑定，发送方多数情况下不绑定
bind_addr = ("",56479)#ip地址可以不填
udp_socket.bind(bind_addr)#绑定端口，元组的形式

#接收内容
recv_data = udp_socket.recvfrom(1024)#接收数据的字节数限制
#拆包
content,destinfo = recv_data
#解码打印
print("content is %s"%content)
print("content is %s"%content.decode("gb2312"))