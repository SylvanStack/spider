# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:33
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : fanyi.py
# @Software: PyCharm
import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
data = {
    'from': ' zh',
    'to': 'en',
    'query': '你好',
    'token': 'cf236a517c7cd6f9497578596ea6d399',
    'sign': '232427.485594'
}
url = 'https://fanyi.baidu.com/basetrans'

response = requests.post(url, headers=headers, data=data)

dict_ret = json.loads(response.content.decode())
print(dict_ret)
