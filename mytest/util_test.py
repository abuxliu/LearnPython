#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author   :

# 测试工具包：project_utils.py

# 引入工具模块
import project_utils as pju

# to_json
# 返回json格式的数据
# pju.to_json(succ=False,stmt='错误信息')

# datestr_to_timestamp
# 字符形式的日期转成时间戳
tm = pju.datestr_to_timestamp('2020-02-02 12:00:00')
print(tm)

# timestamp_to_datestr
# 时间戳转成日期字符串
str = pju.timestamp_to_datestr(tm,format='%Y-%m-%d')
print(str)

# now_timestamp
# 获得当前的时间戳，单位秒
tm = pju.now_timestamp()
print(tm)

# md5_encode
# 字符串的MD5加密，一般用于密码的保存
str_md5 = pju.md5_encode('123456')
print(str_md5)

# base64_encode
# base64 加密
str_base64 = pju.base64_encode('123456')
print(str_base64)

# base64_decode
# base64 解密
str = pju.base64_decode(str_base64)
print(str)

# gnr_check_code
# 产生验证码，4位，大写
str = pju.gnr_check_code()
print(str)

# get_project_dir
# 获得项目的所在文件夹路径，作为其它资源的根目录
root = pju.get_project_dir()
print(root)



