class Test(object):

	def __init__(self):
		super(Test, self).__init__()
		self.__num = 100
	
	#装饰器
	@property
	def num(self):
		print("set")
		return self.__num

	@num.setter
	def num(self,new_number):
		print("get")
		self.__num = new_number


t = Test()

t.num = 200
print(t.num)
