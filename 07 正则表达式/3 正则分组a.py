import re
a = re.match(r"^1[35678]\d{9}$","adwdwad15901113096")
print(a)

b = re.match(r"\w+\s\bve\b","ho ve r")
print(b)

c = re.match(r".+\bve\b","ho ve r")
print(c)

d = re.match(r".+\Bve\B","hover")
print(d)
