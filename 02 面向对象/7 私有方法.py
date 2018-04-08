class Msg():
	
	#私有方法
	def __send_msg(self):
		print("正在发送短信")
	
	#共有方法
	def send_msg(self,money):
		if money>0:
			'''注意加括号，满足条件采用公有方法 调用私有方法'''
			self.__send_msg() 
		else:
			print("余额不足")
		
msg=Msg()
a = 0
msg.send_msg(a)	

b = 200
msg.send_msg(b)	