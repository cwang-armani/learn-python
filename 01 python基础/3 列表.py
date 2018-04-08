names=["laowang","laoliu","laoli"]
names.append("laozhao") #插在最后 names.pop最后一个删除 两者对应
print(names)
names.insert(0,"pig") #插在某个位置
print(names)
names2=["laosi","laoliu"]
names.extend(names2)
print(names)
names.remove("laowang")# del names[0]
print(names)
print(names[2:5])
print(names[::-1]) #列表也有字符串的性质 逆序 切片等