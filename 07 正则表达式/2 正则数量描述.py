import re

a = re.match("1[34578]","18")
print(a)

b = re.match("1[^34578]","19")# ^表示取反 \d 0-9 \D ^0-9 \w a-z
print(b)

c = re.match("1[a-z5-9]","1a")# -表示范围
print(c)

d = re.match("1[34578]\d*","14445645644")# \d*表示无穷个\d
print(d)

e = re.match("\d+","14445645644")# *至少出现一次
print(e)

f = re.match("\d?\d[^a-z]","44445645644")# ?出现1或0次
print(f)

g = re.match("[1-3]{3,5}","333343344")# ?出现1或0次
print(g)