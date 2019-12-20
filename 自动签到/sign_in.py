import requests
import re


class LoginVPN(object):
    """
    登陆Vpn
    """

    def __init__(self):
        self.headers = {
            'Referer': 'https://webvpn.tjise.edu.cn/users/sign_in',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'Host': 'webvpn.tjise.edu.cn',
            'Origin': 'https://webvpn.tjise.edu.cn',
            'Connection': 'keep-alive'
        }
        self.get_url = 'https://webvpn.tjise.edu.cn/users/sign_in'
        self.post_url = 'https://webvpn.tjise.edu.cn/users/sign_in'
        self.get_upate_url = 'https://webvpn.tjise.edu.cn/vpn_key/update'
        self.session = requests.Session()

    def get_authenticity_token(self):
        """
        获取表单所需数据 authenticity_token
        :return: authenticity_token
        """
        response = self.session.get(url=self.get_url, headers=self.headers,allow_redirects = False)
        authenticity_token = re.findall('name=.*csrf-token.*content=(.*?)/>', response.text)[0].replace('"', '')
        return authenticity_token

    def login(self, username, password):
        post_data = {
            'commit': '登录 Login',
            'utf8': '✓',
            'authenticity_token': self.get_authenticity_token(),
            'user[login]': username,
            'user[password]': password,
            'user[dymatice_code]': 'unknown'
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        response= self.session.get(url=self.get_upate_url, headers=self.headers)
        print(response.text)
        if response.status_code == 200:
            print(response.text)


if __name__ == "__main__":
    loginVPN = LoginVPN()
    print(loginVPN.get_authenticity_token())
    print('-'*50)
    loginVPN.login(username='ssqy024', password='Tjise@1163')
