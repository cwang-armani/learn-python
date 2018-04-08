import copy

#浅拷贝，仅指向地址
a = [11,22,33]
b = a
print(id(a))
print(id(b))

#深拷贝，内容一样，地址不一样
print('-------------')
c = copy.deepcopy(a)
print(id(a))
print(id(b))
print(id(c))

print('-------------')
a.append(44)
print(a)
print(b)
print(c)