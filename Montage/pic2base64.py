#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:beiliangshizi - huangjunjie3@jd.com
# datetime:2019/6/28 20:09

import base64
f = open('b.jpg','rb')            #二进制方式打开图文件
ls_f = base64.b64encode(f.read())     #读取文件内容，转换为base64编码
f.close()
print(ls_f)