class Animal():
	def eat(self):
		print("吃")
	def drink(self):
		print("喝")
	def sleep(self):
		print("睡")
	def run(self):
		print("跑")


class Dog(Animal): #继承父类的名字
	def bark(self):
		print("汪汪叫")

class xiaotq(Dog):
	
	def fly(self):
		print("飞")
	def bark(self):
		print("狂叫")
		
		#子类方法调用重写父类方法
		#第一种
		#try:
		Dog.bark(self)
		#except Exception as result:
			#print(result)
 		#第二种
		#调用当前父类功能
		#super(xiaotq,self).bark()  python2
		super().bark()

xiaotq = xiaotq()
xiaotq.bark()



