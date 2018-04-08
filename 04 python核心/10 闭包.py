'''
如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）。
一个闭包就是你调用了一个函数A，这个函数A返回了一个函数B的引用给你。
这个返回的函数B就叫做闭包。你在调用函数A的时候传递的参数就是自由变量 
'''


def test(number):

	print("---1---")

	def test_in(number2):
		print("---2---")
		print(number+number2)

	print("---3---")
	return test_in

a = test(100)
a(20)
a(100)
a(200)
'''

#闭包可以简化调用过程，有些参数只需调用一次
def test(a,b):
	
	def test_in(x):
		print(a*x+b)
	
	return test_in

line1 = test(1,1)
line2 = test(10,4)
line1(0)
line2(0)
'''