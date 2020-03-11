#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author   :


# 蓝图 构建在: /admin

#引入蓝图使用的模块
from flask import Blueprint,request,render_template

# 创建蓝图对象，名字一般和URL中的名字一致
admin = Blueprint('admin',__name__)

# 该模块中的路由定义必须使用蓝图对象

# 网址: http://localhost:5000/admin/list.do
@admin.route('/list.do')
def list():
	return '蓝图 bp_admin.py 中的 list 方法'
	
# 网址: http://localhost:5000/admin/save.do
@admin.route('/save.do',methods=['GET','POST'])
def save():
	a=1
	b=3.14
	c='hello, 你好'
	d=['1111','2222','3333','4444']
	e={
		'code':'12345678',
		'name':'张三',
		'age':18
	}
	return render_template('test_jinjia2.html',a=a,b=b,c=c,d=d,e=e)
	
	
	