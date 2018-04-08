# coding；utf-8
import time
from MyWebServer import  HTTPServer

# 设置静态文件根目录 当前目录的子目录
HTML_ROOT_DIR = "./html"

class Application(object):
    '''框架核心，通用框架'''
    def __init__(self,urls):
        self.urls = urls

    # __call__()的作用是使实例能够像函数一样被调用，同时不影响实例本身的生命周期
    def __call__(self, env, dynamic_response):
        path = env.get("PATH_INFO","/")
        # 读取静态文件
        if path.startswith("/static"):
            file_name = path[7:]
            try:
                file = open(HTML_ROOT_DIR + file_name, "rb")

            except IOError:
                status = "404 Not Found"
                headers = []
                dynamic_response(status, headers)
                return "not found"
            else:
                file_data = file.read()
                file.close()
                # 构造响应数据
                status = "200 OK"
                headers = []
                dynamic_response(status, headers)
                return file_data.decode("utf-8")  # 以二进制方式读取文件，需要解码

        else:
            for url, handler in self.urls:
                if path == url:
                    response_body = handler(env, dynamic_response)# handler即为调用的函数名
                    return response_body #返回响应体文件

def show_ctime(env,start_response):
    status = " 200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()


def say_hello(env, start_response):
    status = " 200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return "hello welcome"

urls = [
    ("/",show_ctime),
    ("/ctime.py", show_ctime),
    ("/sayhello.py", say_hello),
]
app = Application(urls)

# if __name__ == "__main__":
#
#     urls = [
#         ("/ctime.py", show_ctime),
#         ("/sayhello.py", say_hello),
#     ]
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     local_addr = ("", 8001)
#     http_server.set_port(local_addr)
#     http_server.start_process()
