# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 14:59
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : fanyi.py
# @Software: PyCharm
import requests
import json


# 1. 获取语言类型
# 1.1 准备post url和数据
# 1.2 发送post请求
# 1.3 提取语言类型
# 2. 准备Post数据
# 3. 发送Post请求，获取响应数据
# 4. 提取翻译结果


class Fanyi:
    def __init__(self, trans_str):
        self.trans_str = trans_str
        self.lang_type_url = 'https://fanyi.baidu.com/langdetect'
        self.trans_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers).content.decode()
        return json.loads(response)

    def trasn_to(self, lan):
        to_lan = ''
        if lan == 'zh':
            to_lan = 'en'
        if lan == 'en':
            to_lan = 'zh'
        return to_lan


    def get_ret(self,dict_response):
        print(dict_response)
        # print(dict_response["trans_result"][0]["result"][0][1])



    def run(self):
        lang_type_data = {"query": self.trans_str}
        lang_response = self.parse_url(self.lang_type_url, lang_type_data)
        lan = lang_response["lan"]
        trans_data = {
            "query": self.trans_str,
            'from': lan,
            'to': self.trasn_to(lan),
            'simple_means_flag': '3',
            'sign': '232427.485594',
            'token': 'cf236a517c7cd6f9497578596ea6d399'
        }
        dict_response = self.parse_url(self.trans_url, data=trans_data)
        self.get_ret(dict_response)

if __name__ == '__main__':
    fanyi = Fanyi("你好")
    fanyi.run()
