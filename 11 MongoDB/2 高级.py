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

$group 管道
aggregate接受数组[]
db.stu.aggregate([
	{$group:
		{
		_id:"$gender",
		counter:{$sum:1}
		}
	}
]) 

group表示分组，counter相当于sql里的as... 
sum:1有一行统计一次 gender此处为属性需要加$

db.stu.aggregate([
	{$group:
		{
		_id:"$gender",
		counter:{$push:"age"}
		}
	}
]) 

基于gender分组之后，将所有检索的gender存储到一个数组中
_id 表示分组的依据

db.stu.aggregate([
	{$group:
		{
		_id:"$gender",
		counter:{$push:"$$root"}
		}
	}
]) 
基于gender分组之后，将所有检索的所以有内容存储到一个数组中

db.stu.aggregate([
	{$group:
		{
		_id:null,
		counter:{$sum:1},
		avg_age:{$avg:"$age"}
		}
	}
])
group by null 集合中所有文档分为一组

$match 管道：过滤，相当于where
db.stu.aggregate([
	{$match:{age:{$gt:20}}},
	{$group:
		{
		_id:"$gender",
		counter:{$sum:1}
		}
	}
]) 

后面括号中相当于find中的语句,先筛选后聚合，相当于sql中的先where后groupby

$project 管道：过滤，相当于select
db.stu.aggregate([
	{$match:{age:{$gt:20}}},
	{$group:
		{
		_id:"$gender",
		counter:{$sum:1}
		}
	},
	{$project:
		{
		_id:0,
		counter:1
		}
	}
]) 

$sort 管道：排序，相当于order by
db.stu.aggregate([
	{$match:
		{
		age:{$gt:20}
		}
	},
	{$group:
		{
		_id:"$gender"
		counter:{$sum:1}
		}
	},
	{$project:
		{
		_id:0,
		counter:1
		}
	},
	{$sort:
		{
		counter:1
		}
	}
])

$skip和limit管道：相当于limit
db.stu.aggregate([
	{$match:{age:{$gt:20}}},
	{$group:
		{
		_id:"$gender",
		counter:{$sum:1}
		}
	},
	{$project:
		{
		_id:0,
		counter:1
		}
	},
	{$sort:
		{
		counter:1
		}
	},
	{$skip:1}
	{$limit:1}
])

----------------------------------------------------------------------
性能分析：
db.stu.find().explain(executionStats)
建立索引：
db.stu.ensureindex({name:1})
联合索引：
db.stu.ensureindex({name:1},{age:1})
查看索引：
de.stu.getindex()

----------------------------------------------------------------------
安全性流程：
超级管理员权限-->需要修改配置文件，启用身份验证-->重启服务
-->超级管理员登陆-->创建普通用户-->普通用户登陆
db.createUser(
	{
	user:'admin',
	pwd:'123456',
	roles:
	[{role:'root',db:'admin'}]
	}
)

db.createUser(
	{
	user:'admin',
	pwd:'123456',
	roles:
	[{role:'readwrite',db:'python3'}]
	}
)

mongo -u admin -p 123456 --authenticationDatabase admin