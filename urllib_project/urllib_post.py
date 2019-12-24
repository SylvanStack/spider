# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 14:22
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : urllib_post.py
# @Software: PyCharm

import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())