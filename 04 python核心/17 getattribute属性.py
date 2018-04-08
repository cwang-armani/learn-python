class Itcast(object):

	def __init__(self, subject1):
		super(Itcast, self).__init__()
		self.subject1 = subject1
		self.subject2 = "cpp"

	def __getattribute__(self,obj):
		print("===>1%s"%obj)
		if obj == "subject1":
			print("log subject1")
			return "redirect python"
		else:
			temp = object.__getattribute__(self,obj)
			print("===>2%s"%str(temp))
			return temp	

	def show(self):
		print("This is Itcast")


s = Itcast("Python3")

print(s.subject1)
print(s.subject2)

#s.show() #先获取show属性对应的结果，是个方法，后调用方法