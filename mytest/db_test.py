#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author   :

# 测试数据库操作，数据库文件: ./mytest.db
'''
数据库结构：
CREATE TABLE "ztest" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"code"	TEXT,
	"name"	TEXT,
	"age"	INTEGER
)
'''

# 引入 os 模块，获得当前路径
import os
#引入 sqlite3模块，操作数据库
import sqlite3

#获得当前文件夹，绝对路径
cur_dir = os.path.dirname(os.path.abspath(__file__))
#如果存在windows中的\\路径字符，需要替换为 /
if cur_dir.find('\\')!=-1:
	cur_dir = cur_dir.replace('\\','/')
#数据库文件的路径
db_path = cur_dir+'/mytest.db'
print('数据库文件路径：'+db_path)

#测试select语句
def test_select():
	#打开数据库链接
	conn = sqlite3.connect(db_path)
	#获得数据库访问的游标
	cursor = conn.cursor()
	#组装sql语句，select语句如果比较长，建议三个引号的多行字符串使用
	#sql语句可以使用占位符，问号? 或者名称 :name 方式，一般 ? 方式使用的较多
	# 使用 ? 作为占位符，第二个数据参数必须是：元组
	# 使用 :name 作为占位符，第二个参数必须是：字典
	sql = '''
	select * from ztest where name like :name
	'''
	# 返回查询的结果集对象
	# result_set.fetchone: 返回查询结果的第1条，元组
	# result_set.fetchall: 返回所有的结果，列表[元组]
	result_set = cursor.execute(sql,{'name':'%张%'})
	for row in result_set:
		print(row,type(row))
		
	# 一般会把查询的结果组装成字典的列表，便于后续的数据操作
	sql = '''
		select id,code,name,age from ztest where name like ? 
		order by code limit 10 offset 0
	'''
	result_all = cursor.execute(sql,('%李%',)).fetchall()
	# 定义结果集的列表，内部放置记录的字典
	rows = []
	for line in result_all:
		record = {}
		record['id'] = line[0]
		record['code'] = line[1]
		record['name'] = line[2]
		record['age'] = line[3]
		# 将本行记录插入到结果集列表中
		rows.append(record)
		
	print(rows)
	
	# 查询表中记录的条数
	sql = 'select count(*) from ztest'
	result_one = cursor.execute(sql).fetchone()
	total = result_one[0]
	print('total: {}'.format(total))
	
	#关闭本次链接，必须
	conn.close()
	
def test_insert():
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()
	sql = '''
	insert into ztest(code,name,age) values(?,?,?)
	'''
	
	#insert,update,delte, 没有返回结果，直接执行即可
	cursor.execute(sql,('a0002','李四',25))
	
	#insert,update,delte, 必须做 提交
	conn.commit()
	
	conn.close()
	
def test_update():
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()
	sql = '''
	update ztest set age=? where id=?
	'''
	cursor.execute(sql,(28,2))
	
	conn.commit()
	conn.close()
	
def test_delete():
	conn = sqlite3.connect(db_path)
	cursor = conn.cursor()
	sql = '''
	delete from ztest where id=?
	'''
	# 注意，? 只有一个的时候，也需要元组形式，加逗号 ：(2,)
	cursor.execute(sql,(2,))
	
	conn.commit()
	conn.close()
	
	
if __name__ == '__main__':
	# test_insert()
	test_select()
	