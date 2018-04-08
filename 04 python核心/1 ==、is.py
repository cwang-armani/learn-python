a = [11,22,33]
b = [11,22,33]
c = a
print(id(a))
print(id(b))
print(id(c))

print(a == b)#指向所指向的对象，值相等
print(a is b)
print(a is c)#a与c指向同一个对象

print("--------------")

a = 100
b = 100

print(a == b)
print(a is b)

print("--------------")

c = 100111
d = 100111

print(c == d)
print(c is d)