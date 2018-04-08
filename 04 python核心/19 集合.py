#采用集合排重
a=[11,22,33,44,11,22,33,55,66,77]
b=set(a)
a=sorted(list(b))
print(a)
print("--"*10)

#采用集合求 交集 并集 差集
A="dawdawilhfuiasgdawdg"
B=set(A)

C="doaiwhdujadsdhoi"
D=set(C)

#求交集
print(sorted(B&D))
print("--"*10)
#求并集
print(sorted(B|D))
print("--"*10)
#求差集
print(sorted(B-D))
print("--"*10)
#求对称差集
print(sorted(B^D))
print("--"*10)