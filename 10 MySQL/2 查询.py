查询：

删除重复的数据：
distinct
mysql> select distinct gender from students;
mysql> select distinct name,gender from students;

模糊查询：
like  _任意1字符  %任意多字符
mysql> select * from students where name like '小%';
mysql> select * from students where name like '小__';

范围查询：
between and，in

判空：
is null, is not null

优先级：
小括号 not 比较运算符（包括between and,in） 逻辑运算符
and比or先运算 如果希望先算or 配合括号使用

---------------------------------------------------------
聚合：原始语句看不到了，只能达到聚合结果
count()计算行
max min sum avg 计算字段

mysql> select * from students where id = (select max(id) from students);
mysql> select avg(id) from students where gender = 0 and isDelete = 0;

---------------------------------------------------------
分组：非聚合字段不能出现在结果之中
select 列1,列2,聚合... from 表名 group by 列1,列2,列3...
mysql> select gender,count(*) from students group by gender;

筛选：
select 列1,列2,聚合... from 表名 where

group by 列1,列2,列3...
having 列1,...聚合...

where是对from后面指定的表进行数据筛选，属于对原始数据的筛选
having是对group by的结果进行筛选

mysql> select gender,count(*) from students group by gender having gender = 0;

---------------------------------------------------------
select * from 表名
order by 列1 asc|desc,列2 asc|desc,...
将行数据按照列1进行排序，如果某些行列1的值相同时，则按照列2排序，以此类推
mysql> select * from students where isDelete=0 and gender=0 order by birthday desc;

---------------------------------------------------------
分页：
select * from 表名
limit start,count
从start开始，获取count条数据
start索引从0开始

mysql> select * from subject limit 1,2;
mysql> select * from subject limit (n-1)*m,m
每页显示m条数据，当前显示第n页

---------------------------------------------------------
执行顺序为：
from 表名
where ....
group by ...
select distinct *
having ...
order by ...
limit star,count
实际使用中，只是语句中某些部分的组合，而不是全部