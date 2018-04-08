'''时间片轮转 优先级调度'''
'''并发：任务数大于核心数 并行：任务数小于核心数'''
'''程序就是代码 进程就是正在运行的代码'''

from multiprocessing import Process
import os
import time

#创建一个新的进程，原进程（父进程）返回值大于零，新进程（子进程）返回值等于零
ret = os.fork()
if ret==0:
	while True:
		print("hiahia")
		time.sleep(1)
else:
	while True:
		print("haha")
		time.sleep(1)
