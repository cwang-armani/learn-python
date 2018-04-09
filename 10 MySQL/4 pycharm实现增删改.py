# coding:utf-8
import pymysql
try:
    # 配置连接参数
    conn = pymysql.connect(host="localhost",port=3306,database="python3",
                         user="root",password="123456",charset="utf8")

    # 调用connect中的cursor方法
    cursor = conn.cursor()
    sql = 'insert into students(name,gender,birthday,isDelete) values("小二",0,"1988-9-8",0)'
    sql2 = 'update students set isDelete = 1 where id = 5'
    sql3 = 'delete from students where id = 5'
    # 执行sql语句
    cursor.execute(sql)
    cursor.execute(sql2)
    cursor.execute(sql3)
    # 默认处理事务
    conn.commit()
    cursor.close()

    conn.close()

except Exception as message:
    print(message)
