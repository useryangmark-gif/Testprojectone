# 需要导入库 pymysql
import pymysql
# 需要导入库 pymysql
import pymysql						# 打开数据库连接
db=pymysql.connect(host="47.106.196.30",user="test_soc_vodesho",db="test_soc_vodesho",passwd="zFEFtLWi8E3GbDe5",port=3306,charset="utf8")
# 使用 cursor() 方法创建一个游标对象 cursor,游标是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果
# #创建游标对象
cursor=db.cursor()
#使用execute()方法执行SQL语句
cursor.execute("SELECT * from user_complementaries")     #获取单条数据
# print(cursor.fetchone())           #获取N条数据
# print(cursor.fetchmany(2))      #获取所有数据，序列形式
data = cursor.fetchall()
print(data)