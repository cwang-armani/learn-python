# coding:utf-8
from socket import *
import re
from multiprocessing import Process
# 设置静态文件根目录 当前目录的子目录
HTML_ROOT_DIR = "./html"

def handel_client(tcp_client_socket,tcp_client_addr):
    '''处理客户端请求'''
    # 获取客户端请求数据
    request_data = tcp_client_socket.recv(1024)
    # print("request data [%s]:%s"%(str(tcp_client_addr),request_data))
    request_lines = request_data.splitlines()
    for request_content in request_lines:
        print(request_content)

    # 解析请求报文 'GET /index.html HTTP/1.1'
    request_start_line = request_lines[0]

    # 提取用户需求的文件名 re.match(r"\w+ +(/[^ ]*) ",request_start_line)
    file_name = re.search(r"(/.+?) ", request_start_line.decode("utf-8")).groups()

    if "/" == file_name:
        file_name = "index.html"

    # 打开文件内容,防止请求的文件不存在，出现异常
    try:
        file = open(HTML_ROOT_DIR + str(file_name[0]),"rb")

    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_header = "Server: My server\r\n"
        response_body = "the file is not found"

    # 无异常，执行此代码，正常读取文件
    else:
        file_data = file.read()
        file.close()

        # 构造相应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server: My server\r\n"
        response_body = file_data.decode("utf-8")

    # 无论如何都会执行的代码，返回响应数据
    finally:
        response = response_start_line + response_header +"\r\n" + response_body
        print("response data: %s"%response)

    # 返回响应数据
    tcp_client_socket.send(response.encode("utf-8"))

    # 关闭客户端
    tcp_client_socket.close()

def main():
    tcp_socket_server = socket(AF_INET, SOCK_STREAM)
    # socket option reuse address重用地址
    tcp_socket_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    local_addr = ("127.0.0.1",8001)
    tcp_socket_server.bind(local_addr)
    tcp_socket_server.listen(128)

    while True :
        tcp_client_socket,tcp_client_addr = tcp_socket_server.accept()
        print("a new client came:[%s]"%(str(tcp_client_addr)))
        handel_client_process = Process(target=handel_client,args=(tcp_client_socket,tcp_client_addr))

        # 为新用户开启子进程
        handel_client_process.start()
        tcp_client_socket.close()

if __name__ == "__main__":
    main()