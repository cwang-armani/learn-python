# coding；utf-8
import  time
def application(env,start_response):
    # env包含用户请求的所有数据
    status = " 404 Not Found"
    headers = []
    start_response(status,headers)
    return 'file not found'