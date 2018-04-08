from threading import Thread
import time
'''
线程之间共享全局变量
在⼀个进程内的所有线程共享全局变量，能够在不适⽤其他⽅式的前提下完成多线程之间的数据共享
这点要⽐多进程要好 缺点就是 线程是对全局变量随意遂改可能造成多线程之间对全局变量混乱 即线程不安全
'''

def work1(num):
	num.append(13)
	print("----in work1-----",num)


def work2(num):
	time.sleep(2)
	print("----in work2-----",num)

def main():
	number = [10,11,12]
	print("----in main-----",number)
	
	t1 = Thread(target=work1,args=(number,))
	t1.start()

	t2 = Thread(target=work2,args=(number,))
	t2.start()

if __name__ == '__main__':
	main()