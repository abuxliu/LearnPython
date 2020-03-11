#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author   :

# flask中配置和使用 Jinja2

# 导入Flask的核心模块
from flask import Flask
# 导入 flask 中的 request对象，用于接受网页参数
from flask import request
# 导入 render_template 模板调用方法
from flask import render_template
# 导入os模板，用于找到当前路径
import os
# 导入蓝图所在模块中的蓝图创建对象
from bp_admin import admin

# 当前目录
cur_dir = os.path.dirname(os.path.abspath(__file__))
# 将目录分隔符替换为 / , 以便兼容不同的操作系统
if cur_dir.find('\\')!=-1:
	cur_dir = cur_dir.replace('\\','/')
	
	
# 静态资源文件夹(static)和模板文件夹(templates)需要事先创建好

# 静态资源统一存放在: ./static 目录下
dir_static = cur_dir+'/static'

# Jinja2 需要的 html 模板统一放置在: ./templates 目录下
dir_templates = cur_dir+'/templates'

#创建Flask应用的核心对象 app
# 创建时候设置好两个目录，以及静态资源的前缀
# static_url_path='', 一般这样设置，访问静态资源直接从根目录开始 /js/aa.js
app = Flask(__name__,
	template_folder = dir_templates,
	static_folder = dir_static,
	static_url_path=''
)

# 将蓝图注册到app中
app.register_blueprint(blueprint=admin,url_prefix='/admin')

# 测试Jinja2模板的使用
@app.route('/jinja2.do')
def test_jinjia2():
	# 定义不同类型的python数据格式，传递给模板使用
	a=1
	b=3.14
	c='hello, 你好'
	d=['1111','2222','3333','4444']
	e={
		'code':'12345678',
		'name':'张三',
		'age':18
	}
	
	# 模板文件 test_jinjia2.html 放置在 ./templates 目录中
	# 使用 render_template 方法组装模板和数据，形成返回给浏览器的字符串
	# render_template方法的第一个参数是模板位置
	# 后续的参数就是数据内容了
	html = render_template('test_jinjia2.html',a=a,b=b,c=c,d=d,e=e)
	
	return html


if __name__ == '__main__':
	app.run(debug=True,port=5000)
