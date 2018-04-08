from multiprocessing import Process
import os
import time

# 子进程要执行的代码
def run_proc(name):

	print('Run child process %s (%s,%s)...' % (name, os.getpid(),os.getppid()))
	time.sleep(2)
	# time.sleep(3)
	# 模拟子进程未结束，测试join的作用

def main():
	
	print('Parent process %s.' % os.getpid())
	time.sleep(2)

	p = Process(target=run_proc, args=('test',))
	# 利用元组传递参数，于子进程中调用
	print('Child process will start.')
	# 开始执行函数里面的代码
	p.start()
	# 等待子进程结束的最长时间,子进程未结束,则进行主进程
	p.join()
	time.sleep(2)
	print('Child process end.')

if __name__=='__main__':
	main()
