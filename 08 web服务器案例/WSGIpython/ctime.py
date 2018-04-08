# coding；utf-8
import  time
def application(env,start_response):
    # env包含用户请求的所有数据
    status = " 200 OK"
    headers = [
        ("Content-Type","text/plain")
    ]
    start_response(status,headers)
    return time.ctime()