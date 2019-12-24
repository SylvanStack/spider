# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 13:51
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : httpbin.py
# @Software: PyCharm
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

baidu_url = "https://www.baidu.com/s?"
params = {'wd': 'python'}
response = requests.get(baidu_url, params=params, headers=headers)
response.encoding = 'utf-8'
print(response.request.url)
with open("python.html", "w", encoding='utf-8') as f:
    f.write(response.text)

