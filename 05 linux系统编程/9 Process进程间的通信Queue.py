'''
队列先进先出
#取队列前看队列是否为空，加之前看是否满
Queue.qsize()：返回当前队列包含的消息数量
Queue.empty()：如果队列为空，返回True，反之False
Queue.full()：如果队列满了，返回True,反之False
Queue.get([block[,	timeout]])：获取队列中的⼀条消息，然后将其从列队 中移除，block默认值为True
'''
from multiprocessing import Process,Queue
import os
import time
# 写数据进程执行的代码:
def write(q):
	print('Process %s to write: %s' %(os.getpid(),os.getppid()))
	for value in ['process-1', 'process-2', 'process-3']:
		print('Put %s to queue...' % value)
		print('current queue siez = ',q.qsize())
		q.put(value)

# 读数据进程执行的代码:
def read(q):
	
	print('Process %s to read: %s' %(os.getpid(),os.getppid()))
	while True:
		if not q.empty():
		#取队列前看队列是否为空，加之前看是否满
			value = q.get()
			print('Get %s from queue.' % value)
			print('current queue siez = ',q.qsize())
			time.sleep(0.2)
		else:
			break

if __name__=='__main__':
# 父进程创建Queue，并传给各个子进程：
	print('Process %s start:' %os.getpid())
	
	q = Queue()
	#队列中允许的最大数值，可以不输入

	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	
	pw.start()
	pw.join()
	pr.start()
	pr.join()