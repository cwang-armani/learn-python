'''
在多线程开发中,全局变量是多个线程都共享的数据
⽽局部变量等是,各⾃线程的,是⾮共享的
'''
from threading import Thread
import threading
import time

def test1():
	name = threading.current_thread().name
	print("---Thread name is %s"%name)

	g_num = 100

	if name == "Thread-1":
		g_num += 1
	else:
		time.sleep(2)

	print("---thread is %s and g_num=%d"%(name,g_num))

p1 = Thread(target=test1)
p1.start()

p2 = Thread(target=test1)
p2.start()