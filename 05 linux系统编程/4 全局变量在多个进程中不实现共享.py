import os
import time

g_num = 100
ret = os.fork()

if ret == 0:
	print("zijincheng")
	g_num += 1
	print("ziujincheng----%d----"%g_num)
else:
	time.sleep(3)
	print("fujincheng")
	print("fujincheng----%d----"%g_num)
