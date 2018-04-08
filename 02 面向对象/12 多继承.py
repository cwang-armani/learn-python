class Base():
	def test(self):
		print("---base--")

class A(Base):
	def test(self):
		print("---A--")

class B(Base):
	def test(self):
		print("---B--")

class C(A,B):
	def test(self):
		print("---C--")

c=C()
c.test()

#调用 方法是的搜索顺序 某类中找到方法 便停止搜索
print(C.__mro__)