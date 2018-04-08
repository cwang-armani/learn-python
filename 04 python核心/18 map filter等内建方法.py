'''映射函数 map(function, iterable, ...) 函数名字 可迭代对象'''
a = map(lambda x:x*x,[1,2,3])
print(list(a))

for temp in a:
	print(temp)

print("-"*20)

b = map(lambda x,y:x*y,[1,2,3],[4,5,6])
for temp2 in b:
	print(temp2)

print("*"*20)

def f(x,y):
	return (x,y)

l1 = [0,1,2,3,4,5,6,7]
l2 = ["M","T","W","T","W","S","S"]

c = list(map(f,l1,l2))
print(c)

for temp3 in c:
	print(temp3)

print("-"*20)

'''filter函数,筛选功能，会对指定序列执过滤操作'''
e = filter(lambda x:x%2, [1,2,3,4])
for temp4 in e:
	print(temp4)

print("*"*20)

'''reduce函数，reduce函数会对参数序列中元素进累积'''
from functools import reduce
f = reduce(lambda x,y:x+y, [1,2,3,4])
print(f)

#注意累积求和的顺序
g = reduce(lambda x,y:x+y, ["aa","bb","cc"],"dd")
print(g)

print("-"*20)

'''sorted函数，排序'''
h = [11,22,33,66,99,656,213123]
i = sorted(h,reverse=1)#倒序排列
print(i)
