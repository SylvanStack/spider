# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 13:44
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : intro.py
# @Software: PyCharm

import urllib.parse
import urllib.request

# 完整urlopen
# urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))

print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())