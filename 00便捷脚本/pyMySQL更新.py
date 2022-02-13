"""

数据库更新操作
更新操作用于更新数据表的数据，以下实例将 TESTDB 表中 SEX 为 'M' 的 AGE 字段递增 1：

"""
# !/usr/bin/python3

import pymysql

ip = "localhost"
user = 'root'
pwd = '1234'

# 打开数据库连接
db = pymysql.connect(ip, user, pwd, "matt")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print('ok')
except:
    # 发生错误时回滚
    db.rollback()
    print('on NO')

# 关闭数据库连接
db.close()

