#遍历生成的列表 用法类似于切片 返回值为列表
#风险：内存占用可能会太大
for i in range(10,18,2):
	print(i)

a = [i for i in range(0,6)]
print(a)

b = [11 for i in range(0,6)]
print(b)

c = [i for i in range(0,10) if i%2==0]
print(c)

#for循环嵌套
d = [(i,j) for i in range(3) for j in range(2)] 
print(d)