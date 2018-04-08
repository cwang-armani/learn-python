# coding:utf-8
from socket import *
import re
import sys
from multiprocessing import Process

# 设置静态文件根目录 当前目录的子目录
HTML_ROOT_DIR = "./html"
#WSGI_PYTHON_DIR = "./WSGIpython"

class HTTPServer(object):
    def __init__(self, application):
        self.tcp_socket_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.app = application
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
        response_header = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_header += "%s:%s\r\n" %header
        self.response_headers = response_header

    def handel_client(self,tcp_client_socket, tcp_client_addr):
        '''处理客户端请求'''
        request_data = tcp_client_socket.recv(1024)

        # HTTP请求报文拆分
        request_lines = request_data.splitlines()
        for request_content in request_lines:
            print(request_content)

        # 解析请求报文 'GET /index.html HTTP/1.1'
        request_start_line = request_lines[0]

        # 提取用户需求的文件名 re.match(r"\w+ +(/[^ ]*) ",request_start_line)
        file_name = re.search(r"(/.+?) ", request_start_line.decode("utf-8")).groups(1)
        file_method = re.search(r"(\w+ ?)", request_start_line.decode("utf-8")).groups(1)
        file_name = file_name[0]

        environment = {
            "PATH_INFO":file_name,
            "METHOD":file_method
        }
        response_body = self.app(environment, self.dynamic_response)

        response = self.response_headers + "\r\n" + str(response_body)

        # 打印响应报文
        print("response data: %s\r\n" % response)
        print("-"*40)

        # 返回响应数据
        tcp_client_socket.send(response.encode("utf-8"))

        # 关闭客户端
        tcp_client_socket.close()

def main():

    # 增加接口文件至搜索路径中
    #sys.path.insert(1,WSGI_PYTHON_DIR)
    # sys.argv为列表，第一个元素是程序本身，随后才依次是外部给予的参数。
    print(sys.argv)
    if len(sys.argv) < 2:
        sys.exit("python MyWebServer.py Module:app")
    # python MyWebServer.py MyWebFramework:app
    module_name , app_name = sys.argv[1].split(":")
    # module_name = MyWebFramework app_name = app
    m = __import__(module_name)
    app = getattr(m,app_name)# 获取对象的属性或者方法

    http_server = HTTPServer(app)
    local_addr = ("",8001)
    http_server.set_port(local_addr)
    http_server.start_process()


if __name__ == "__main__":
    main()