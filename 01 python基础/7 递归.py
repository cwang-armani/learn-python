def get_nums(a):
	if a>1:
		return a*get_nums(a-1)
	else:
		return a

b=get_nums(3)
print(b)