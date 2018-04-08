'''
#队列先进先出
from multiprocessing import Queue
import os
import time
#取队列前看队列是否为空，加之前看是否满
'''
from multiprocessing import Pool,Manager
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
			value = q.get(True)
			print('Get %s from queue.' % value)
			print('current queue siez = ',q.qsize())
			time.sleep(0.5)
		else:
			break

if __name__=='__main__':
# 父进程创建Queue，并传给各个子进程：
	print('Process %s start:' %os.getpid())
	
	q =Manager().Queue()
	po = Pool(3)
	#队列中允许的最大数值，可以不输入

	po.apply_async(write, (q,))
	po.apply_async(read, (q,))
	
	po.close()
	po.join()