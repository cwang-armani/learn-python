class CarStore():

	def __init__(self):
		#定义一个类属性，用来存放其他类的引用
		self.factory = Factory
	
	def order(self,type):
		return self.factory.select_car_by_type(type) 

class Factory():
	#简单工场模式 通过类的方式 分离 car 和car store
	def select_car_by_type(type):
		if type == "索纳塔":
			return Suonata() 
		elif type == "名图":
			return Mingtu() 
		elif type == "IX35":
			return IX35() 

class Car():
	def move(self):
		print("车在移动")

	def music(self):
		print("听音乐")

	def stop(self):
		print("停车")

class Suonata(Car):
	pass
class Mingtu(Car):	
	pass
class IX35(Car):
	pass

car_store = CarStore()

#car指向了Car的子类，并调用子类的方法，子类中不存在方法，在父类中寻找方法解决
car = car_store.order("名图")
#结果是car指向了mingtu类

car.move()
car.music()
car.stop()