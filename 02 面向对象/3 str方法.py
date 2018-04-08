#大驼峰
#属性：定义cat类
class Cat:
	#初始化对象
	def __init__(self,name,age):
		self.name=name
		self.age=age

	#初始化对象
	def __str__(self):
		return "%s的年龄是啊啊啊：%d"%(self.name,self.age)

	def eat(self):
		print("吃鱼")

	def drink(self):
		print("喝水")
	#方法
	#按对象调用函数
	def introduce(self):#至少有一个函数，用于接收对象
		print("%s的年龄是：%d"%(self.name,self.age))

tom=Cat("Tom",40) #除了第一个参数，都需要传入

tom.introduce()  #tom.introdice(tom)相当于

bluecat=Cat("bluecat",20)

print(tom)