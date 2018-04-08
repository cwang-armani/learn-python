#copy可以判断数据是否为可变类型还是不可变类型，有不同的处理方式
import copy
a = [11,22,33]
b=[44,55,66]

#列表，可变对象，copy对象与原对象地址不同
c = [a,b]
e = copy.copy(c)
f = copy.deepcopy(c)

a.append(666)

print(c)
print(e[0])
print(f[0])
print(id(c))
print(id(e))
print(id(f))

print('---------')
a1 = [11,22,33]
b1 =[44,55,66]

#元组，只读类型,copy对象与原对象地址相同
c1 = (a1,b1)
g = copy.copy(c1)
h = copy.deepcopy(c1)

a1.append(666)

print(c1)
print(g[0])
print(h[0])
print(id(c1))
print(id(g))
print(id(h))