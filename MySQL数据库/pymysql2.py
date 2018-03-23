# coding=utf-8
import pymysql

#导入pymysql驱动

connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '123456',
    db = 'test',                            #test1数据据分为:员工表emp,部门表dept.
    charset = 'utf8',
    cursorclass = pymysql.cursors.DictCursor     #返回结果为一个由字典元素构成的列表，每个字典为字段和值构成的键值对。
)
#上面执行完，相当与 mysql 的use test； 然后进入test数据库了

try:
    with connection.cursor() as cursor:                           # 得到游标
        cursor.execute('delete FROM dept;')  # 执行插入语句
        connection.commit()  # 提交
        sql = 'insert dept values(10,"开发部");'               #创建插入语句
        cursor.execute(sql)                                        #执行插入语句
        connection.commit()                                        #提交

    with connection.cursor() as cursor:
        sql = 'select * from dept;'
        cursor.execute(sql)
        result = cursor.fetchall()                                 #得到所有的查询记录  fetchone()得到一个数据。
        print(result)

finally:
    connection.close()


