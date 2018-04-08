
from multiprocessing import Pool
import os,time

def test1():
	print("Child process is statring, pid=%s,ppid=%s"%(os.getpid(),os.getppid()))
	for i in range(3):
		print("---process--%d--"%i)
	return "haha"

def test2(*args):
	print("callback process is statring, pid=%s,ppid=%s"%(os.getpid(),os.getppid()))
	for i in range(3):
		print("---callback process--%d--"%i)
	return "hehehe"
	print("---callback-function----pid=%s"%os.getpid())
	print("---callback-function----args=%s"%args)

if __name__ == '__main__':
	p = Pool(3)
	# 
	p.apply_async(func=test1,callback=test2)

	count = 0
	while True:
		count +=1
		print("---main process's pid=%s"%os.getpid())
		time.sleep(0.2)
		if count>10:
			break

