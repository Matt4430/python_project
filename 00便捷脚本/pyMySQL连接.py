"""
一、python实现用户登陆

1、连接、关闭（游标）
execute():SQL注入
101.34.178.236:matt:1230
"""
import pymysql
# ip = input('ip:')
# user = input('username:')
# pwd = input('password:')
# ip = '101.34.178.236'
ip = "localhost"
user = 'root'
pwd = '1234'

# 打开数据库连接
db = pymysql.connect(ip, user, pwd, "matt")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("show databases;")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()