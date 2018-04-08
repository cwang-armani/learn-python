class Test(object):
	"""docstring for Test"""
	def __init__(self):
		super(Test, self).__init__()
		self.__num = 100

	def set_number(self,new_number):
		self.__num = new_number

	def get_number(self):
		return self.__num

t = Test()
# 私有属性名字重整，其实是可以访问的，下划线+类名+私有属性名print(t._Test__num)
print(t._Test__num)
print(t.get_number())
print("-"*10)
t.set_number(50)
print(t.get_number())