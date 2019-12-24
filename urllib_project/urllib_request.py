# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 14:31
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : urllib_request.py
# @Software: PyCharm

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey',
    'sex': '男'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))