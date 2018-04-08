'''
采用types.MethodType
代码动态更新
为类添加方法
函数名也可以作为变量进行传递
'''
import types
class Person(object):
	num = 0
	def __init__(self, name = None, age = None):
		self.name = name
		self.age = age
	def eat(self):
		print("eat food")

def run(self, speed):
	print("%s在移动, 速度是 %d km/h"%(self.name, speed))

#定义了一个类方法
@classmethod
def testClass(cls):
	cls.num = 100

#定义了一个静态方法
@staticmethod
def testStatic():
	print("---static method----")

P = Person("老王", 24)

P.eat()
#给这个对象添加实例方法 并调用（比较特殊）
P.a = types.MethodType(run, P)
P.a(180)

#给Person类绑定类方法 并调用 进行前后结果对比
print(Person.num)
Person.b = testClass
Person.b()
print(Person.num)

#给Person类绑定静态方法 并进行调用
Person.c = testStatic
Person.c()