class Sweetpotato():
	def __init__(self):
		#面向对象，属性才能保存值
		self.cookedstring = "生的"
		self.cookedlevel = 0
		self.condimen = []

	def __str__(self):
		return "地瓜的状态是：%s(%d) 味道是：%s" %(self.cookedstring,self.cookedlevel,str(self.condimen))
		#注意列表的生成方式


	def cook(self,time):
		#把时间扔到属性里去，下次调用
		self.cookedlevel += time
		
		#注意elif 和else的区别
		if self.cookedlevel>=0 and self.cookedlevel<3:
			self.cookedstring = "生的"
		elif self.cookedlevel>=3 and self.cookedlevel<5:
			self.cookedstring = "半生不熟"
		elif self.cookedlevel>=5 and self.cookedlevel<8:
			self.cookedstring = "熟了"
		elif self.cookedlevel>=8:
			self.cookedstring = "成碳了"

	def addcondiments(self,ingredient):
		self.condimen.append(ingredient)



#创建地瓜对象
di_gua=Sweetpotato()
print(di_gua)

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)

di_gua.addcondiments("孜然")
di_gua.cook(1)
print(di_gua)

di_gua.addcondiments("番茄酱")
di_gua.cook(1)
print(di_gua)

di_gua.addcondiments("辣椒")
di_gua.cook(1)
print(di_gua)

di_gua.addcondiments("芥末")
di_gua.cook(1)
print(di_gua)

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)