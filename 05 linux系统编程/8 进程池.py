from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (its pid=%s and ppid=%s)...' % (name, os.getpid(),os.getppid()),end=' ')
	
	start = time.time()
	time.sleep(random.random() * 3)
	
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
	
	print('Parent process %s.' % os.getpid())
	
	# 同一时刻所执行的进程个数
	p = Pool(3)
	# 向进程池中添加任务，任务数如果超过进程数，多余的任务会等待进程池中的任务执行完毕
	for i in range(10):
		p.apply_async(long_time_task, args=(i,))
		#相当于Process函数，同样利用元组传递参数，于子进程中调用
	print('-------Waiting for all subprocesses done--------')
	
	# 关闭进程池，无法添加任务了
	p.close()
	# join所完成的工作就是进程同步，即主进程任务结束之后，进入阻塞状态，一直等待其他的子进程执行结束之后，主进程在终止
	# timeout设置，超出时间则杀死子进程
	p.join()

	print("-------All subprocesses done.-------")

'''
from multiprocessing import Pool
import os
import random
import time

def func(num):
		print("---pid=%d---num=%d---"%(os.getpid(),num))
		time.sleep(1)


if __name__ == '__main__':

	#同时运行的最大进程数
	p = Pool(3)

	for i in range(10):
		#向进程池中添加任务，任务数如果超过进程数，多余的任务会等待进程池中的任务执行完毕
		print("---%d---"%i)
		p.apply_async(func,(i,))
	#关闭进程池，无法添加任务了
	p.close()
	#主进程结束后，完成进程池中的任务，没有join进程池中的任务不会执行
	p.join()
	'''