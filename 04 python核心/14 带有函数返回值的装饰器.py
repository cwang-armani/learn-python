def func(functionName):
	
	def func_in():
		x = functionName()
		return x
	return func_in

@func
def test():
	return "haha"

result = test()
print(result)