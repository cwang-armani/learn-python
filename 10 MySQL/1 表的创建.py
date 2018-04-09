数据库命令：
创建create database 数据库名 charset=utf8;
删除drop database 数据库名;
查看所有数据库：show databases;
使用数据库：use 数据库名;
----------------------------------------
表命令：
create table 表名(列...);
唯一标识的要求：id
	类型：int unsigned
	约束1：not null
	约束2：primary key
	约束3：auto_increment
列的格式：列的名称 类型 约束

create table students(
    -> id int not null primary key auto_increment,
    -> name varchar(10) not null,
    -> gender bit default 1,
    -> birthday datetime,
    -> isDelete bit default 0,
    -> );

查看创建语法:show create table students;

查看表:show tables;

查看表结构:desc students;

修改表：alter table students add|modify|drop 列名 类型 约束;

mysql> alter table students add isDelete bit default 0;

删除表：drop table 表名;
----------------------------------------
添加数据：(必然会新增一行)
mysql> insert into students values(0,'郭靖',1,'1990-1-1',0);
mysql> insert into students(name,gender) values('黄蓉',0);
mysql> insert into students(name,gender,birthday) values('杨过',0,'1989-03-20');

修改数据：
mysql> update students set birthday='1990-1-1' where id = 2;

删除数据：
delete from students where id = 3

逻辑删除，并查看：
mysql> update students set isDelete=1 where id=3;
mysql> update students set isDelete=1 where id=3;

备份：
mysql> mysqldump -uroot -p students > ~Desktop/bak.sql

恢复：
mysql -uroot -p py31 < bak.sql
----------------------------------------
外键设置：
create table course(  
course_id varchar(20),  
deptnames varchar(20),  
credits int,  
foreign key(deptnames) references department(dept_name));  


create table scores(
id int primary key auto_increment,
stuid int,
subid int,
score decimal(5,2),
foreign key(stuid) references students(id),
foreign key(subid) references subjects(id)
);


外键的级联操作

在删除students表的数据时，如果这个id值在scores中已经存在，则会抛异常
推荐使用逻辑删除，还可以解决这个问题
可以创建表时指定级联操作，也可以在创建表后再修改外键的级联操作
语法

alter table scores add constraint stu_sco foreign key(stuid) references students(id) on delete cascade;
级联操作的类型包括：
restrict（限制）：默认值，抛异常
cascade（级联）：如果主表的记录删掉，则从表中相关联的记录都将被删除
set null：将外键设置为空
no action：什么都不做