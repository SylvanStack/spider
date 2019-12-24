# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 16:09
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : proxy.py
# @Software: PyCharm

import requests
import json

proxies = {'http': 'http://221.6.138.154:41880'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
url = 'http://httpbin.org/ip'
result = requests.get(url, headers=headers, proxies=proxies)
# result = requests.get(url, headers=headers)
print(result.content.decode())

# with open('proxy-ip.html','w',encoding='utf-8') as f:
#     f.write(result.content.decode())
