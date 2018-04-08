# coding:utf-8
from socket import *

from multiprocessing import Process

def handel_client(tcp_client_socket,tcp_client_addr):
    '''处理客户端请求'''
    # 获取客户端请求数据
    receive_data = tcp_client_socket.recv(1024)
    print("request data [%s]:%s"%(str(tcp_client_addr),receive_data))

    # 构造相应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server: My server\r\n"
    response_body = "hello wangnima"
    response = response_start_line + response_header +"\r\n" + response_body
    print("response data: %s"%response)

    # 返回响应数据
    tcp_client_socket.send(bytes(response,"utf-8"))

    # 关闭客户端
    tcp_client_socket.close()

def main():
    tcp_socket_server = socket(AF_INET, SOCK_STREAM)
    local_addr = ("",8001)
    tcp_socket_server.bind(local_addr)
    tcp_socket_server.listen(128)
    while True :
        tcp_client_socket,tcp_client_addr = tcp_socket_server.accept()
        print("a new client came:[%s]"%(str(tcp_client_addr)))
        handel_client_process = Process(target=handel_client,args=(tcp_client_socket,tcp_client_addr))
        handel_client_process.start()
        tcp_client_socket.close()

if __name__ == "__main__":
    main()