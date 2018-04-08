class Home():
	
	def __init__(self,new_area,new_type,new_addr):
		self.area = new_area
		self.type = new_type
		self.addr = new_addr
		self.left_area = new_area
		self.contain_item = []
	
	def __str__(self):
		message = "area=%d,left.area=%d,type=%s,addr=%s\n"%(self.area,self.left_area,self.type,self.addr)
		message += "There are:%s"%(str(self.contain_item))
		return message

	def add_item(self,forniture):
		self.left_area -= forniture.get_area() #此处逻辑很重要 foniture=bed1 bed2  
		self.contain_item.append(forniture.get_name())

class Bed():
	
	def __init__(self, new_name,new_area):
		self.name = new_name
		self.area = new_area
	
	def __str__(self):
		return "%s占用的面积是：%d"%(self.name,self.area)

	def get_area(self):
		return self.area
	
	def get_name(self):
		return self.name
		

fangzi=Home(129,"3 and 1","Beijing")
print(fangzi)

bed1=Bed("大床",5)
print(bed1)
fangzi.add_item(bed1)
print(fangzi)

bed2=Bed("小床",3)
print(bed2)
fangzi.add_item(bed2)
print(fangzi)