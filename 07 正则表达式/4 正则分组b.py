import re

#匹配0-100所有数字
a = re.match(r"[1-9]{1}\d?$|0$|100$","033")
print(a)
#把0包含进去
b = re.match(r"[1-9]?\d?$|100$","10")
print(b)

#括号分组
c = re.match(r"(<html>)(.*)(</html>)","<html>匹配分组</html>")
print(c.group(3))
print(c.groups())

s = "<html><h1>itcast</h1></html>"
z = re.match(r"<.+><.+>.+</.+></.+>",s)
print(z.group())
#引用分组数字 匹配字符串
s1 = "<html><h1>itcast</h1></html>"
z1 = re.match(r"<(.+)><(.+)>(.+)</\2></\1>",s1)
print(z1.group())

s2 = "<h333><html>itcast</h333></html>"
z2 = re.match(r"<(.+)><(.+)>(.+)</\1></\2>",s2)
print(z2.group())

print("-"*20)

#此例中 . 需要转译一哈
p = r"(\w+)@(163|qq|sina|yahoo|gmail|)\.(com|net|cn)$"
m = re.match(p,"wangnima@qq.com")
print(m.group())

print("-"*20)
# P要大写
s3 = "<h333><html>itcast</h333></html>"
z3 = re.match(r"<(?P<name1>.+)><(?P<name2>.+)>(.+)</(?P=name1)></(?P=name2)>",s2)
print(z3.group())