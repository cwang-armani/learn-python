# coding:utf-8
from socket import *
import re
import sys
from multiprocessing import Process
# 设置静态文件根目录 当前目录的子目录
HTML_ROOT_DIR = "./html"

WSGI_PYTHON_DIR = "./WSGIpython"

class HTTPServer(object):
    def __init__(self):
        self.tcp_socket_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.response_headers = ""

    def set_port(self,local_addr):
        self.tcp_socket_server.bind(local_addr)

    def start_process(self):
        self.tcp_socket_server.listen(128)
        while True:
            tcp_client_socket, tcp_client_addr = self.tcp_socket_server.accept()
            print("a new client came:[%s]" % (str(tcp_client_addr)))
            handel_client_process = Process(target=self.handel_client, args=(tcp_client_socket, tcp_client_addr))

            # 为新用户开启子进程
            handel_client_process.start()
            tcp_client_socket.close()

    def dynamic_response(self, status, headers):
        response_header = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            response_header += "%s:%s\r\n" %header
        self.response_headers = response_header

    def handel_client(self,tcp_client_socket, tcp_client_addr):
        '''处理客户端请求'''
        request_data = tcp_client_socket.recv(1024)

        # HTTP请求报文
        request_lines = request_data.splitlines()
        for request_content in request_lines:
            print(request_content)

        # 解析请求报文 'GET /index.html HTTP/1.1'
        request_start_line = request_lines[0]

        # 提取用户需求的文件名 re.match(r"\w+ +(/[^ ]*) ",request_start_line)
        file_name = re.search(r"(/.+?) ", request_start_line.decode("utf-8")).groups(1)
        file_method = re.search(r"(\w+ ?)", request_start_line.decode("utf-8")).groups(1)
        file_name = file_name[0]

        # 动态页面的响应，__import__为动态加载类和函数
        if file_name.endswith(".py"):

            # 防止请求的文件不存在，出现异常,容错处理
            try:
                m = __import__(file_name[1:-3])
            except Exception:
                self.response_headers = "HTTP/1.1 404 Not Found \r\n"
                response_body = "Not found"
            else:
                environment = {
                    "PATH_INFO":file_name,
                    "METHOD":file_method
                }
                response_body = m.application(environment, self.dynamic_response)

            response = self.response_headers + "\r\n" + str(response_body)

        else:
            if "/" == file_name:
                file_name = "index.html"

            # 以二进制方式打开文件内容,防止请求的文件不存在，出现异常
            try:
                file = open(HTML_ROOT_DIR + file_name[0], "rb")

            except IOError:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_header = "Server: My server\r\n"
                response_body = "the file is not found"

            # 无异常，执行此代码，正常读取静态文件
            else:
                file_data = file.read()
                file.close()
                # 构造响应数据
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_header = "Server: My server\r\n"
                response_body = file_data.decode("utf-8")#以二进制方式读取文件，需要解码

            response = response_start_line + response_header + "\r\n" + response_body

        # 打印响应报文
        print("response data: %s" % response)

        # 返回响应数据
        tcp_client_socket.send(response.encode("utf-8"))

        # 关闭客户端
        tcp_client_socket.close()

def main():

    # 增加接口文件至搜索路径中
    sys.path.insert(1,WSGI_PYTHON_DIR)

    http_server = HTTPServer()
    local_addr = ("",8001)
    http_server.set_port(local_addr)
    http_server.start_process()


if __name__ == "__main__":
    main()