
from threading import Thread, Lock
import time
# 加锁的位置 决定了内存资源占用效率
g_num = 0

def test1():
	global g_num
	# 执行到100万次的时候打印值，该值不一定是100000
	for i in range(10):
		mutex.acquire()
		g_num += 1
		print("---test1---g_num=%d"%g_num)
		time.sleep(0.1)
		mutex.release()

def test2():
	global g_num
	# 执行到100万次的时候打印值，该值不一定是100000
	for i in range(10):
		mutex.acquire()
		g_num += 1
		print("---test2---g_num=%d"%g_num)
		time.sleep(0.1)
		mutex.release()	

	#两个线程争抢着上锁，一方上锁则另一方被堵塞，处于休眠状态，节省资源占用，效率高

if __name__ == '__main__':
	
	# 创建一把互斥锁	
	# 去掉join方法和不去掉的区别
	mutex = Lock()
	p1 = Thread(target=test1)
	#p1.setDaemon(True)
	p1.start()
	p1.join()

	p2 = Thread(target=test2)
	# p2.setDaemon(True)
	p2.start()
	p2.join()

	print("---g_num=%d---"%g_num)
