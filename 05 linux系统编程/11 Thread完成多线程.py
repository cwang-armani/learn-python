#跟process创建多进程类似
from threading import Thread
import os
import time

def say_sorry():
	print('subthread %s is starting his parent is %s'%(os.getpid(),os.getppid()))
	print("----sorry----")
	time.sleep(1)

def main():
	print('main thread %s is starting'%os.getpid())
	p = Thread(target=say_sorry)
	p.start()
	p.join()
	print('main thread %s is ending'%os.getpid())

if __name__ == '__main__':
	main()