class Person(object):
	"""定义人类"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name
		#保存枪的引用
		self.gun = None
		#人物的血量
		self.hp = 100

	def __str__(self):
		if self.gun:
			return"%s的血量为%d，他有枪%s"%(self.name,self.hp,self.gun)
		else:
			if self.hp > 0:
				return"%s的血量为%d，他没有枪"%(self.name,self.hp)
			else:
				return"%sgg了........"%(self.name)		


	def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
		'''把子弹装入弹夹中'''
		#弹夹保存子弹（子弹）
		dan_jia_temp.baocun_zidan(zi_dan_temp)

	def anzhuang_danjia(self,gun_temp,dan_jia_temp):
		'''弹夹安装到枪中'''
		gun_temp.baocun_danjia(dan_jia_temp)

	def naqiang(self,gun_temp):
		#老王拿起一把枪 gun_temp=ak47
		self.gun = gun_temp

	def fire(self,enemy):
		self.gun.open_fire(enemy)

	def diaoxue(self,sha_shang_li):
		#根据杀伤力掉血
		self.hp -= sha_shang_li


class Gun(object):
	"""docstring for Gun"""
	def __init__(self, name):
		super (Gun, self).__init__()
		self.name = name#记录枪的类型
		self.danjia = None#记录弹夹的引用

	def __str__(self):
		if self.danjia:
			return"枪的信息为：%s , %s"%(self.name,str(self.danjia))
		else:
			return"枪里没有子弹"
	def baocun_danjia(self,dan_jia_temp):
		'''属性保存弹夹对象的引用'''
		self.danjia = dan_jia_temp

	def open_fire(self,enemy):
		#枪从弹夹获取一发子弹击中敌人 先从弹夹取子弹 让子弹打敌人
		#弹出子弹 弹夹.弹子弹
		zidan_temp = self.danjia.tanchu_zidan()

		if zidan_temp:
			zidan_temp.dazhong(enemy)
		else:
			print("么子弹了")


class Danjia(object):
	"""Danjia"""
	def __init__(self, max_num):
		super(Danjia, self).__init__()
		self.max_num = max_num#子弹数目
		self.zidan_list = []#用来记录所有子弹的引用

	def __str__(self):
		return "弹夹的信息为：%d/%d"%(len(self.zidan_list),self.max_num)

	def baocun_zidan(self,zi_dan_temp):
		'''将子弹保存进弹夹'''
		self.zidan_list.append(zi_dan_temp)

	def tanchu_zidan(self):
		#弹出最上面的子弹
		if self.zidan_list:
			return self.zidan_list.pop()
		else:
			return None

		
class Zidan(object):
		"""Zidan"""
		def __init__(self, sha_shang_li):
			super(Zidan, self).__init__()
			self.sha_shang_li = sha_shang_li#子弹杀伤力
		
		def dazhong(self,enemy):
			#让敌人掉血
			#敌人.掉血（子弹威力）
			enemy.diaoxue(self.sha_shang_li)
		





def main():
	"""用来控制整个程序的流程"""

	#1创建老王
	laowang = Person("老王")
	#2创建抢
	ak47 = Gun("ak47")
	#3创建弹夹
	dan_jia = Danjia(20)
	#4创建一些子弹
	for i in range(20):
		zi_dan = Zidan(30)

		#5老王把子弹装进弹夹
		#老王安装子弹到弹夹中（弹夹，子弹）
		laowang.anzhuang_zidan(dan_jia,zi_dan)

	#6老王把弹夹安装到抢里
	#老王安装弹夹到抢中（枪，子弹）
	laowang.anzhuang_danjia(ak47,dan_jia)

	#test 弹夹
	#print(dan_jia)
	#test 枪
	#print(ak47)

	#7老王拿枪 
	laowang.naqiang(ak47)
	#测试老王拿枪
	print(laowang)
	#8创建敌人
	laosong = Person("隔壁老宋")
	print(laosong)
	#9老王开枪打敌人
	#老王.开枪（老宋）
	laowang.fire(laosong)
	print(laosong)
	print(laowang)
	laowang.fire(laosong)
	print(laosong)
	print(laowang)
	laowang.fire(laosong)
	print(laosong)
	print(laowang)
	laowang.fire(laosong)
	print(laosong)
	print(laowang)
	laowang.fire(laosong)
	print(laosong)
	print(laowang)



if __name__ == '__main__':
	main()
