a = [x*2 for x in range(0,8,2)]
print(a)
print("-"*10)

'''
列表生成式，可以创建列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。这种一边循环一边计算的机制，称为生成器（Generator）。
'''

#创建生成器,只是创建了一个方法，使用next是才会不断生成数值

#方法1：
b = (x*2 for x in range(10))
#print(b)
print(next(b))
print(next(b))
print(next(b))

print("*"*10)


#1创建斐波那契数列
def creat_num():
	a,b = 0,1
	for i in range(5):
		print(b)
		a,b = b,a+b

creat_num()
print("-"*10)

#2创建斐波那契数列
#函数中出现yield则变为生成器，不再是函数执行，返回的是对象,必须找一个变量来接受
'''
这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''
def creat_num():
	a,b = 0,1
	for i in range(5):
		yield(b)
		a,b = b,a+b
#创建了生成器对象 next(a)等价于a.__next__()
a = creat_num()
for i in range(5):
	print(next(a))

'''另一种循环方法
for num in a:
	print(num)
'''