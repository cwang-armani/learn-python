# coding:utf-8
import pymysql
class MySQLHelper(object):
	'''封装python3与SQL的交互'''
	def __init__(self,host,user,password,databse):
		self.host=host
		self.user=user
		self.password=password
		self.database=databse
		self.port = 3306
		self.charset = "utf8"

	def cud(self,cud_sql):
		self.connect()
		try:
			self.cursor.execute(cud_sql)
				# 如有异常进行回滚操作
		except Exception as message:
			print(message)
			self.conn.rollback()
		else:
			self.conn.commit()

	def search(self,search_sql):
		# 实现数据的增删改查
		self.connect()

		try:
			self.cursor.execute(search_sql)
			for result in self.cursor.fetchall():
				id = result[0]
				name = result[1]
				gender = result[2].decode("utf-8")
				birthday = result[3]
				isDelete = result[4].decode("utf-8")
				# 打印结果
				print(id, name, gender, birthday, isDelete)

		except Exception as message:
			print(message)

		self.close()

	def connect(self):
		# 链接数据库
		self.conn = pymysql.connect(
			host=self.host,user=self.user,password=self.password,
			database=self.database,port=self.port,charset=self.charset)

		self.cursor = self.conn.cursor()

	def close(self):
		# 关闭数据库
		self.cursor.close()
		self.conn.close()

if __name__ == "__main__":
	# 初始化
	my_sql = MySQLHelper("localhost","root","123456","python3")
	cud_sql = '''update students set isDelete = 1 where id = 5'''
	my_sql.cud(cud_sql)
	# 查询并返回查询结果，未查询到时返回空元组
	search_sql = '''select * from students WHERE id > 4 AND gender = 0'''
	my_sql.search(search_sql)