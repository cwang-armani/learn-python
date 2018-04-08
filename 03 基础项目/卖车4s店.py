class Carstore(object):

	def __init__(self):
		super(Carstore, self).__init__()
		self.factory = Factory

	def order(self,name):
		return self.factory.select_car_by_type(name)

class Factory(object):

	def select_car_by_type(type):
		if type == "名图":
			return Mingtu()
		elif type == "宝马":
			return BMW()
		elif type == "桑塔纳":
			return Santana()

class Car(object):
	"""docstring for Car"""
	def music(self):
		print("The car is playing music")

	def move(self):
		print("The car is moving")

class Mingtu(Car):
	pass
class BMW(Car):
	pass
class Santana(Car):
	pass
		
		
car_store = Carstore()
car = car_store.order("名图")
car.music()
car.move()