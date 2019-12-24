# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 14:26
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : urlopen.py
# @Software: PyCharm

from  urllib import request

resp=request.urlopen('http://www.baidu.com')
# print(resp.read()) # 读取所有
# print(resp.read(10)) # 读取指定字节
# print(resp.readline()) # 读取多行
# print(resp.readlines()) # 读取多行
print(resp.getcode()) # 获取响应状态码

# 直接下载代码
# request.urlretrieve("https://www.baidu.com/",'baidu.html')
# 直接下载图片
request.urlretrieve("https://www.baidu.com/img/bd_logo1.png",'bd_logo1.png')