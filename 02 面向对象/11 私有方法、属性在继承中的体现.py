class A():
	def __init__(self):
		self.num1 = 100
		#定义私有属性
		self.__num2 = 200

	def test1(self):
		print("test1")

	def __test2(self):
		print("test2")

	def test3(self):
		self.__test2()
		#调用私有方法__test2
		print(self.__num2)

class B(A):
	def test4(self):
		self.__test2()
		print(self.__num2)

b=B()

#b.test1()

#b.__test2() 直接调用私有方法不会被继承

b.test3()  #公有方法调用私有方法和私有属性是可以的

#b.test4()  #两者区别,父类中的方法可调用父类中的私有方法，子类中的方法无法调用父类中的私有方法
