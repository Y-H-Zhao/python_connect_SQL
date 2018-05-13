# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:43:37 2018

@author: ZYH
"""

# 连接数据库
import pymssql
 

def Mssql():
    # 连接数据库
    db = pymssql.connect(host="localhost",user="sa",password="ncepumath123456",database="ZZ",as_dict=True)
    #as_dict=True以字典方式返回，否则是元组
    #cursor()方法获取操作游标 
    cursor = db.cursor()
    try:
        return(db, cursor)
    except:
        print("数据库访问失败")
        

# 增
def Insert(db, cursor):
    # \换行
    sql = "insert into [ZZ].[dbo].[USA]([state],[Murder],[Assault],[UrbanPop],[Rape]) \
    values('Alabama', 13.2, 236, 58, 21.2)"
    # 执行SQL语句
    cursor.execute(sql)
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    db.commit()

# 删
def Delect(db, cursor):
    sql = "DELETE FROM [ZZ].[dbo].[USA] WHERE state = 'Alabama'"
    cursor.execute(sql)
    db.commit()

# 查
def Select(db, cursor):
    sql = "SELECT * FROM [ZZ].[dbo].[USA]"
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    return results

# 改
def Update(db, cursor):
    sql = "UPDATE [ZZ].[dbo].[USA] SET state = 'Alabama' WHERE [Murder] = 13.2"
    cursor.execute(sql)
    db.commit()

# 关闭数据库连接
def Close(db, cursor):
    cursor.close()
    db.close()

#运行函数-从链接到关闭
(db, cursor) = Mssql()

print("\n-------------数据库初始状态 in result1-------------")
#print(Select(db, cursor))
#返回list,list中元素为字典类型，每行为一个字典元素，列名为关键字
result1=Select(db, cursor)

Insert(db, cursor)
print("\n-------------数据库插入数据 in result2-------------")
#print(Select(db, cursor))
result2=Select(db, cursor)

Update(db, cursor)
print("\n-------------数据库修改数据 in result3-------------")
#print(Select(db, cursor))
result3=Select(db, cursor)

Delect(db, cursor)
print("\n-------------数据库删除数据 in result4-------------")
#print(Select(db, cursor))
result4=Select(db, cursor)

Close(db, cursor)
'''
#简单点就是下面这样
import pymssql
db = pymssql.connect(host="localhost",user="sa",password="ncepumath123456",database="ZZ",as_dict=True)
#as_dict=True以字典方式返回，否则是元组
#cursor()方法获取操作游标 
cursor = db.cursor()
sql = "SELECT * FROM [ZZ].[dbo].[USA]"
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
# \换行 
sql = "insert into [ZZ].[dbo].[USA]([state],[Murder],[Assault],[UrbanPop],[Rape]) \
    values('Alabama', 13.2, 236, 58, 21.2)"
# 执行SQL语句
cursor.execute(sql)
cursor.close()
db.close()
'''
