class Dog():
	def __init__(self):
		print("---init---")
	
	def __del__(self):
		print("---del---")
	
	def __str__(self):
		print("---str---")

	#cls此时是dog指向的类对象
	def __new__(cls):
		print("---new---")
		return object.__new__(cls) 


xiaotq=Dog()
#new创建 init初始化