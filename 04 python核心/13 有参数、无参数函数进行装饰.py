def func(function_name):

	def fun_in(*args):
		function_name(*args)
	return fun_in

#test=func(test) test指向内部函数fun_in（注意引用函数的接收数目）
@func
def test(a,b,c,d,e):
	print("---test---a=%d,b=%d,c=%d,d=%d,e=%s---"%(a,b,c,d,str(e)))

test(11,22,33,44,'ddddd')
