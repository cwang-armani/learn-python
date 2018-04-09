实体与实体之间有3种对应关系，这些关系也需要存储下来

函数：在开发中需要对存储的数据进行一些处理，用到内置的一些函数

视图：用于完成查询语句的封装

事务：可以保证复杂的增删改操作有效
---------------------------------------------------------
连接查询：

连接查询分类如下：
表A inner join 表B：表A与表B匹配的行会出现在结果中
表A left join 表B：表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
表A right join 表B：表A与表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充
在查询或条件中推荐使用“表名.列名”的语法
如果多个表中列名不重复可以省略“表名.”部分

select students.name,subject.name,score.score 
from score
inner join students on score.stuid = students.id
inner join subject on score.subid = subject.id;

select students.name,subject.name,score.score 
from score
join students on score.stuid = students.id
join subject on score.subid = subject.id;

select students.name,`subject`.`name`,score.score 
from students
LEFT JOIN score on students.id = score.stuid
LEFT JOIN `subject` on `subject`.id = score.subid

SELECT students.`name`,avg(score.score)
from students 
JOIN score on score.stuid=students.id
GROUP BY students.id
HAVING avg(score.score)>=90;
ORDER BY avg(score.score) DESC

---------------------------------------------------------
自关联查询：多表数据汇集于一个表，节省开销，物理上一张表，逻辑上多张表，结构类似
SELECT province.id as province_id,province.name,city.id as city_id,city.name 
from areas as province
INNER JOIN areas as city on province.id=city.pid
where province.pid is NULL

SELECT city.id,city.name,distrinct.id,distrinct.name 
from areas as city
join areas as distrinct on city.id = distrinct.pid
WHERE city.name = '北京市'

---------------------------------------------------------
视图：用于完成查询语句的封装

create VIEW as v_city_search as
SELECT city.id,city.name,distrinct.id,distrinct.name 
from areas as city
join areas as distrinct on city.id = distrinct.pid
WHERE city.name = '北京市'
---------------------------------------------------------
事务：
当一个业务逻辑需要多个sql完成时，如果其中某条sql语句出错，则希望整个操作都退回
使用事务可以完成退回的功能，保证业务逻辑的正确性

事务四大特性(简称ACID)
原子性(Atomicity)：事务中的全部操作在数据库中是不可分割的，要么全部完成，要么均不执行
一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行的结果相一致
隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事务必须是透明的
持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不被丢失，即使数据库出现故障
要求：表的类型必须是innodb或bdb类型，才可以对此表使用事务

查看表的创建语句

---------------------------------------------------------
索引：
show index from students