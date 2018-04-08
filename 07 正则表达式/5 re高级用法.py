import re

#此例中 . 需要转译一哈
p = r"(\w+)@(163|qq|sina|yahoo|gmail|)\.(com|net|cn)$"
m = re.match(p,"wangnima@qq.com")
print(m.group())

print("-"*20)
# P要大写
s3 = "<h333><html>itcast</h333></html>"
z3 = re.match(r"<(?P<name1>.+)><(?P<name2>.+)>(.+)</(?P=name1)></(?P=name2)>",s3)
print(z3.group())

# search直至搜寻到字符串位置
s4 = "<h333><html>itcast</h333></html>"
z4 = re.search(r"itcast",s4)
print(z4.group())

s5 = "itcast</h333><html>itcast</h333></html>"
z5 = re.findall(r"\w+</h333>",s5)
#多个匹配以列表的形式接收
print(z5[0],z5[1])

# sub将匹配到的数据进行替换
result = re.sub(r"php","python","itcast python cpp php python")
print(result)

print("-"*20)

def replace(res):
	print(res.group())
	r = int(res.group())+50
	return str(r)

result2 = re.sub(r"\d+",replace,"python=1000,php=0")
print(result2)