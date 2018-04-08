
def test(a,b,function):
	result=function(a,b)
	return result

num=test(11,32,lambda x,y:x-y)
print(num)


#动态语言

def test(a,b,function):
	result=function(a,b)
	return result
func_new=input("qingshuruniminghanshu:")
func_new=eval(func_new)

num=test(11,32,func_new)
print(num)