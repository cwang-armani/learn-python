import re
s = """<p>岗位职责：</p> 
<p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p> 
<p>必备要求：</p> 
<p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p> 
<p>技术要求：</p> 
<p>1、⼀年以上Python开发经验，掌握⾯向对象分析和设计，了解设计模式</p> 
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p> 
<p>3、掌握关系数据库开发设计，掌握SQL，熟练使⽤MySQL/PostgreSQL中的几种<br></p> 
<p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>"""

a = re.sub(r"</?\w+>","",s)
print(a)

print("-"*20)
b = re.split(r",| |-","php,python cpp-php")
print(b)