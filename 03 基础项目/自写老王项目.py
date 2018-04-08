import random

class Person(object):
	"""docstring for Person"""
	def __init__(self, person_name):
		super(Person, self).__init__()
		self.person_name = person_name
		self.person_gun = None
		self.hp = 100
	
	def __str__(self):
		if self.person_gun:
			return "%s血量是%d，他有枪,%s"%(self.person_name,self.hp,str(self.person_gun))
		else:
			if self.hp >= 0:
				return "%s血量是%d，他没有枪"%(self.person_name,self.hp)
			else:
				return "%s挂了"%(self.person_name)

	def Install_bullint(self,charger_temp,bullint_temp):
		charger_temp.Save_bullint(bullint_temp)

	def Install_charger(self,gun_temp,charger_temp):
		gun_temp.Save_charger(charger_temp)

	def Catch_gun(self,gun_temp):
		self.person_gun = gun_temp

	def Openfire(self,enemy):
		self.person_gun.openfire(enemy)

	def down(self,bullint_hurt):
		self.hp -= bullint_hurt



class Gun(object):
	"""docstring for Gun"""
	def __init__(self, gun_name):
		super(Gun, self).__init__()
		self.gun_name = gun_name
		self.gun_list = None

	def __str__(self):
		if self.gun_list:
			return "枪的信息是：%s, %s"%(self.gun_name,str(self.gun_list))
		else:
			return "他没有枪"

	def Save_charger(self,charger_temp):
		self.gun_list = charger_temp

	def openfire(self,enemy):
		charger_t = self.gun_list.popping()
		#返回的是弹夹列表中 每个子弹的引用

		if charger_t:
			charger_t.kill(enemy)
		else:
			print("没有子弹了")


class Charger(object):
	"""docstring for Charger"""
	def __init__(self, charger_num):
		super(Charger, self).__init__()
		self.charger_num = charger_num
		self.charger_list = []

	def __str__(self):
		return "子弹的数目是：%d/%d"%(len(self.charger_list),self.charger_num)

	def Save_bullint(self,bullint_temp):
		self.charger_list.append(bullint_temp)

	def popping(self):
		if self.charger_list:
			return self.charger_list.pop()
			#删除一个子弹的引用 即弹出子弹 并返回
		else:
			return None


class Bullint(object):
	"""docstring for Bullint"""
	def __init__(self, bullint_hurt):
		super(Bullint, self).__init__()
		self.bullint_hurt = bullint_hurt

	def kill(self,enemy):
		enemy.down(self.bullint_hurt)
								

def main():

	#创建老王
	laowang = Person("老王")

	#创建枪
	gun = Gun("98k")

	#创建弹夹
	charger = Charger(20)

	#创建子弹
	for i in range(10):
		bullint = Bullint(random.randint(0,30))
		
		#老王把子弹装进弹夹
		laowang.Install_bullint(charger,bullint)

	#print(charger)
	#把弹夹装进枪
	laowang.Install_charger(gun,charger)
	#print(gun)
	#老王拿起枪
	laowang.Catch_gun(gun)
	#print(laowang)
	#创建敌人
	laozhao = Person("老赵")
	#print(laozhao)
	#老王开枪打老赵
	
	print(laowang)

	laowang.Openfire(laozhao)
	print(laozhao)
	laowang.Openfire(laozhao)
	print(laozhao)
	laowang.Openfire(laozhao)
	print(laozhao)
	laowang.Openfire(laozhao)
	print(laozhao)
	laowang.Openfire(laozhao)
	print(laozhao)
	laowang.Openfire(laozhao)
	print(laozhao)
	laowang.Openfire(laozhao)
	print(laozhao)

if __name__ == '__main__':
	main()