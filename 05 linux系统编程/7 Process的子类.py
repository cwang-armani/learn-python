from multiprocessing import Process
import time
import random

class My_new_process(Process):

	def __init__(self):
		super(My_new_process, self).__init__()

	def run(self):
			print("---1---")
			time.sleep(2)

def main():
	i=1
	while i<=5:
		
		p = My_new_process()
		# start方法在My_new_procee的父类Process之中 此时Process(target=run)
		p.start()
		p.join(1)

		print("---2---")
		time.sleep(2)
		i +=1

if __name__ == '__main__':
		main()			