import os
import time

ret = os.fork()

if ret == 0:
	print("zijincheng")
	time.sleep(3)
	print("zijincheng--over--")
else:
	print("fujincheng")

print("---game---over---")#该行 共执行两次
#父进程完全执行完毕后 执行子进程(顺序不确定)