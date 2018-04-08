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

xiaotq = xiaotq()
xiaotq.fly()
xiaotq.bark()
xiaotq.eat()


