def test():
	i = 0
	while i < 5:
		if i == 0:
			temp = yield i 
		else:
			yield i
		i += 1

t = test()
#生成器必须由对象接，进行迭代
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))