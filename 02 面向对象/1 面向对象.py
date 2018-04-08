#大驼峰
class Cat:
	#属性
	def eat(self):
		print("吃鱼")

	def drink(self):
		print("喝水")
	#方法
	#按对象调用函数
	def introduce(self):#至少有一个函数，用于接收对象
		print("%s的年龄是：%d"%(self.name,self.age))

tom=Cat()

tom.eat()
tom.drink()

tom.name="Tom"
tom.age=18

tom.introduce()  #tom.introdice(tom)相当于

bluecat=Cat()


bluecat.name="bluecat"
bluecat.age=20
bluecat.introduce()