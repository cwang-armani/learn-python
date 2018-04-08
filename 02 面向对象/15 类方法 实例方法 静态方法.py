class Game():
	num = 0

	#实例方法
	def __init__(self):
		self.name = "laowang"
		self.num = 50

	#类方法，对类属性进行更改
	@classmethod
	def add_num(cls):
		cls.num = 100

	#静态方法 完成一个与类和实例都没关系的方法,可以不传入任何参数
	@staticmethod
	def print_meun():
		print("---666---")

game=Game()

#调用类方法的两种形式
game.add_num()
Game.add_num()
print(Game.num)
print(game.num)

game.print_meun()
Game.print_meun()
