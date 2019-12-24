# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 14:28
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : urllib_timeout.py
# @Software: PyCharm

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')