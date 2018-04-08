class Test(object):

	def __init__(self):
		super(Test, self).__init__()
		self.__num = 100

	def set_number(self,new_number):
		self.__num = new_number
		print("set")

	def get_number(self):
		print("get")
		return self.__num

	#property为了方便调用get和set方法
	num = property(get_number,set_number)

t = Test()

# 私有属性名字重整，其实是可以调用的，下划线+类名+私有属性名print(t._Test__num)
print(t.get_number())
t.set_number(50)
print(t.get_number())

print("-"*10)

t.num = 300
#相当于 t.set_num(300)
print(t.num)
#相当于 t.get_num()

'''
注意点:
t.num 到底是调用getNum()还是setNum(),要根据实际的场景来判断,
1. 如果是给t.num赋值 那么一定调用setNum()
2. 如果是获取t.num的值,那么就一定调用getNum()
property的作用:相当于把方法进行了封装, 开发者在对属性设置数据的时候更方便
'''