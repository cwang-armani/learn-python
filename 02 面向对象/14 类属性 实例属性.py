class Tool(object):
	"""docstring for Tool"""
	num = 0
	def __init__(self, name):
		super(Tool, self).__init__()
		self.name = name
		
		#类属性+！
		Tool.num += 1


'''实例属性 和具体某个实例对象有关 并且 一个实例对象和另一个实例对象不共享属性'''
'''类属性 所属类对象 并且多个实例对象之间 共享一个类属性'''

tool1=Tool("铁锹")
tool2=Tool("兵工铲")
tool3=Tool("水桶")

print(Tool.num)
