nums=[123,525,23123,523,31,23,4,4124,53525]
nums.sort()
print(nums)

infors=[{"name":"laowang","age":18},{"name":"2hangsan","age":32},{"name":"wangwu","age":12}]
infors.sort(key=lambda x:x["name"])

print(infors)

for temp in infors:
	print(temp["name"])