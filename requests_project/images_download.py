# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 17:21
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : images_download.py
# @Software: PyCharm
import requests

response = requests.get('https://2.python-requests.org//zh_CN/latest/_static/requests-sidebar.png')

print(response.content)

with open('./request.png','wb')as f:
    f.write(response.content)
