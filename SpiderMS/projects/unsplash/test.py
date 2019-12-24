# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 13:30
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : test.py
# @Software: PyCharm
from urllib.request import urlopen

real_url = 'https://unsplash.com/photos/SYIpxU6laA0/download' + "?force=true"
with urlopen(real_url) as result:
    # 读取图片数据
    data = result.read()
    # 打开图片文件
    with open("images/" + "hZvx336dhAg" + '.jpg', 'wb+') as f:
        # 写入读取的数据
        f.write(data)
