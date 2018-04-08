class Dog():
	
	def __init__(self,new_name):
		self.name = new_name
		self.age = 0 #初始化年龄

	def set_age(self,new_age):
		if new_age > 0:
			self.age = new_age
		else:
			self.age = '输入有误' # =0

	def get_age(self):
		return self.age # str

dog=Dog("xiaobai")
dog.set_age(40)
age=dog.get_age()
print(age)
print(dog.age)

