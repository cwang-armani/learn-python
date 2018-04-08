class Animal():
	def eat(self):
		print("吃")
	def drink(self):
		print("喝")
	def sleep(self):
		print("睡")
	def run(self):
		print("跑")

'''继承父类的名字，直接打在里面，前面定义的就不用重写'''
'''调用方法 先子类 后父类'''

class Dog(Animal): 
	def bark(self):
		print("汪汪叫")

class Cat(Animal):
	def catch(self):
		print("抓老鼠")

a=Animal()
a.eat()

wangcai = Dog()
wangcai.eat()
wangcai.bark()

tom=Cat()
tom.eat()
tom.catch()