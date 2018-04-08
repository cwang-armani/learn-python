a = (11,22,33)
b = [11,22,33]
c={11,22,33}
print(type(a))
print(type(b))
print(type(c))

#排重
a=(11,22,33,11,22,33,44,55,66)
b=[]
for i in a:
	if i not in b:
		b.append(i)
print(b)

f=set(a)
print(f)

c=tuple(f)
print(c)