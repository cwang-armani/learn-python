import re
s = """<p>岗位职责：</p> 
<p>完成推荐算法、数据统计、接⼝、后台等服务器端相关⼯作</p> 
<p>必备要求：</p> 
<p>良好的⾃我驱动⼒和职业素养，⼯作积极主动、结果导向</p> 
<p>技术要求：</p> 
<p>1、⼀年以上Python开发经验，掌握⾯向对象分析和设计，了解设计模式</p> 
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p> 
<p>3、掌握关系数据库开发设计，掌握SQL，熟练使⽤MySQL/PostgreSQL中的⼀种<br></p> 
<p>4、掌握NoSQL、MQ，熟练使⽤对应技术解决⽅案</p>"""

a = re.sub(r"<.+?>","",s)
print(a)

# 采用？关闭贪婪模式
s = re.match(r"(.+?)(\d+-\d+-\d+-\d+?)","This is a phone number 234-234-33-543433")
print(s.groups())

s1 = """<img	data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"	src="https://rpic.douyuc dn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"	st yle="display:	inline;">
"""
result = re.search(r"https.+?\.jpg",s1)
print(result.group())

s2 ="""http://www.interoem.com/messageinfo.asp?id=35 http://3995503.com/class/class09/news_show.asp?id=14 http://lib.wzmc.edu.cn/news/onews.asp?id=769 http://www.zy-ls.com/alfx.asp?newsid=377&id=6 http://www.fincm.com/newslist.asp?id=415"""
result2 = re.search(r"http.+?(\.com|\.cn)",s2)
print(result2.group())

result3 = re.sub(r"(http://.+?/)(.+)",lambda x:x.group(1),s2)
print(result3)