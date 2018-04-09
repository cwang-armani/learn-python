后来，随着访问量的上升
几乎大部分使用MySQL架构的网站在数据库上都开始出现了性能问题
web程序不再仅仅专注在功能上，同时也在追求性能。
程序员们开始大量的使用缓存技术来缓解数据库的压力，
优化数据库的结构和索引
----------------------------------------------------------------------
show dbs 显示数据库
use python3 使用数据库
show collections 显示数据库中的所有集合
db.dropDatabase()删除数据库，先要使用use命令
db.createCollection(name, options)

db.mycollection.drop()删除集合

option类型：
capped	Boolean	如果为true，则启用封顶集合当它达到其最大大小，会自动覆盖最早的条目。
如果指定true，则需要也指定size字段。

autoIndexID	Boolean	（可选）如果为true，自动创建索引_id字段, 默认值是false。

size	number	（可选）指定集合最大可使用字节。如果封顶如果是 true，那么你还需要指定这个字段。

max	number	（可选）指定封顶集合允许在文件的最大数量。
Size限制优先于此限制。如果一个封顶集合达到大小size限制，未达到文件的最大数量，
MongoDB删除旧的文件。如果您更喜欢使用max，
确保为上限的集合所需的大小限制，足以包含文档的最大数量。
----------------------------------------------------------------------
查询语句：GUI
db.sub.find() 显示集合所有内容
db.sub.find().pretty() 格式化显示集合
db.sub.find().limit(number) 显示多少条数据
db.sub.find().skip(number) 跳过多少条数据
db.sub.find().skip(number).limit(number) 不分先后顺序

db.sub.find({title:"mongoDB"}) 添加查询条件
----------------------------------------------------------------------
比较运算符：
db.sub.find({count:{$gt:2}})
{<key>:{$lt:<value>}} less than
{<key>:{$lte:<value>}} less than equals
{<key>:{$gt:<value>}} great than
{<key>:{$gte:<value>}} great than equals

----------------------------------------------------------------------
逻辑运算符：

and直接通用逗号链接即可
db.sub.find({title:"css",count:{$gt:2}})

or则用 $or:[{},{}] 表示or内的条件用逗号隔开
db.sub.find({$or:[{title:"css"},{count:{$gt:2}}]})

in和nin表示范围
db.sub.find({count:{$in:[1,3]}})

db.sub.find({$where:
	function(){return this.age>20}})

名字以g为开头的，包含某字母用大于等于
db.sub.find({$where:
	function(){return this.name.indexOf('g')==0}})

----------------------------------------------------------------------
投影：查询筛选某字段
db.sub.find({name:1,age:1})
----------------------------------------------------------------------
排序:1升序 -1降序
db.sub.find().sort({name:-1})
----------------------------------------------------------------------
聚合：
统计：
db.sub.find({gender:1}).count()
db.sub.find({gender:1},{age:{$gt:20}}).count()

管道：前一次命令的输出结果作为下一次的输入