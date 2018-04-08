def func_args(arg):
	def func(function_name):
		def func_in():
			print("日志 arg = %s"%arg)
			if arg == "hehe":
				function_name() 
				function_name()
				
			else:
				function_name()
		return func_in
	return func 

#先执行@func_args("hehe")，返回了func的引用
#test=@func(test)

@func_args("hehe")
def test():
	print("---test---")

@func_args("haha")
def test2():
	print("---test2---")

test()
test2()