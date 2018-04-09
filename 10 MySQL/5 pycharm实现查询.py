# coding:utf-8
import pymysql
try:
    # 配置连接参数
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        database="python3",
        user="root",
        password="123456",
        charset="utf8")

    # 调用connect中的cursor方法
    cursor = conn.cursor()
    sql = '''select * from students WHERE id > 2 AND gender = 0'''
    # 执行sql语句
    cursor.execute(sql)
    
    # 打印各字段的结果
    # fetchall()执行查询时，获取结果集的所有行
    # 一行构成一个元组，再将这些元组装入一个元组返回
    for result in cursor.fetchall():
        id = result[0]
        name = result[1]
        gender = (result[2].decode("utf-8"))
        birthday = result[3]
        isDelete = (result[4].decode("utf-8"))

        print(id,name,gender,birthday,isDelete)

    cursor.close()

    conn.close()

except Exception as message:
    print(message)
