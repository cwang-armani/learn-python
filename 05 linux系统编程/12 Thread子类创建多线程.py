import threading
import time
#类中调用run方法
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm "+self.name+' @ '+str(i) 
            #name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    
	for i in range(3):
		t = MyThread()
		t.start()
