import re

result = re.match("itcast","itcast.com")
print(result)

a = "itcastheima".startswith("itcast")
print(a)

# 匹配任意一个字符
b = re.match("...","acb")
print(b)

# 匹配任意一个数字
c = re.match("\d","1")
print(c)

# 匹配任意一个非数字
d = re.match("\D","d")
print(d)

# 匹配任意一个空白 如" " \n \t \r
e = re.match("\s"," a")
print(e)

# 匹配单词字符 大小写字母 数字
f = re.match("\w","_a")
print(f)

print("-*20")

#按顺序匹配
f = re.match("\w\W","a-")
print(f)