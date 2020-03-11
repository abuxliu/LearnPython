#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author   :

# 第一个最小的flask程序

#导入Flask的核心模块
from flask import Flask
# 导入 flask 中的 request对象，用于接受网页参数
from flask import request

#创建Flask应用的核心对象 app
app = Flask(__name__)

#使用app创建路由，为该函数设定 URL
@app.route('/')
def hello_word():
	#定义要返回给浏览器的html格式字符串
	html = 'hello world! hello Flask!'
	
	#将组装完成的字符串返回给浏览器
	return html
	
#接受浏览器参数，a=矩形的长，b=矩形的宽，返回矩形的面积
#定义路由函数时候，指定运行的方式，不指定则默认为：GET
#可以给URL指定一个统一的后缀名，如 .do
@app.route('/rectarea.do',methods=['GET','POST'])
def rectangle_area():
	if request.method == 'POST':
		# POST方式，使用 request.form 来获得参数
		a = request.form.get('a')
		b = request.form.get('b')
	else:
		# GET方式，使用 request.args 来获得参数
		a = request.args.get('a')
		b = request.args.get('b')
		
	# 如果没有得到需要的参数，则返回错误信息
	if a is None:
		return '缺少必要参数 a'
		
	if b is None:
		return '缺少必要参数 b'
		
	# 定义返回的html，从页面获得的参数都是字符型，需要转数值再计算面积
	html = '矩形长：{}，宽：{}，面积：{}'.format(a,b,int(a)*int(b))
		
	return html
	
if __name__ == '__main__':
	#应用启动
	app.run(debug=True,port=5000)