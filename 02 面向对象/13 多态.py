'''
有时候，一个对象有多种类型或形式。假设有一个按钮，
有许多不同的拉伸输出（圆形按钮，复选按钮，方形按钮，按钮图像）
但它们确实共享相同的操作逻辑“点击”：。访问使用相同的方法。
这种思想称为：多态。
'''

class Dog(object):
	
	def print_self(self):
		print("i am xxxxx")

class Xiaotq(Dog):
	def print_self(self):
		print("hello everybody!")

def introduce(temp):
	temp.print_self()

dog1=Dog()
dog2=Xiaotq()

introduce(dog1)
introduce(Dog())

introduce(dog2)
introduce(Xiaotq())