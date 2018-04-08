try:
	11/0
	#open("xxx.txt")
	#try子句中，出现异常，则后续子句不执行
	print("1")

#except (NameError,FileNotFoundError):#元组 异常的名字 报错时候应该注意
	#print("找到异常位置")

except Exception as result:
	print("上面的except未捕获任何异常 此处exception会捕获到 异常的总称")
	print(result)
else:
	#try语句没有任何异常的时候执行else子句
	#else语句的存在必须以except语句为前提
	print("无异常执行此代码")

finally:
	#无论如何都要做的事情
	print(3)
