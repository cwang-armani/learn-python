'''
创建全局threadlocal对象，你可以把local_school看成全局变量，
但每个属性如local_school.student都是线程的局部变量，
可以任意读写⽽互不⼲扰，也不⽤管理锁的问题，ThreadLocal内部会处理。
'''
from threading import Thread
import threading
local_school = threading.local()

def process_student():
	std = local_school.student
	print("Hello %s in (%s)"%(std,threading.current_thread().name))

def process_thread(*args):
	local_school.student = args[2]
	process_student()

if __name__ == '__main__':
	
	t1 = Thread(target=process_thread,args=("东哥","li","xiaowang"))
	t2 = Thread(target=process_thread,args=("旭哥","wang","dalong"))

	t1.start()
	t2.start()