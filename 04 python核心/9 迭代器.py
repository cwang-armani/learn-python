#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
#列表 元组 字典 集合 字符串
#生成器(x for x in range(10))

'''判断一个对象是否为可迭代对象'''
a=(11,22,33)
from collections import Iterable
print(isinstance(a,Iterable))

'''判断一个对象是否为迭代器'''
from collections import Iterator
print(isinstance(a,Iterator))

print("-"*10)

#将可迭代对象转换为迭代器，占用空间会变小
b = iter(a)
print(next(b))
print(next(b))
print(next(b))