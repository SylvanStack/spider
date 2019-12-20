import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import requests
import json


class Login_vpn:
    """
    登陆VPN
    """

    def __init__(self):
        """
        初始化数据
        """
        self.browser = webdriver.Chrome()
        self.get_vpn_url = 'https://zckj.webvpn.tjise.edu.cn/'
        self.post_vpn_url = 'https://zckj.webvpn.tjise.edu.cn/userLogin/userLogin'
        self.vpn_url = 'https://webvpn.tjise.edu.cn/'

    def login_vpn_get_cookie(self):
        """
        登陆vpn
        :return: 返回cookie
        """
        try:
            self.browser.get(self.vpn_url)
            # 登陆vpn
            input_vpn_username = self.browser.find_element_by_id('user_login')
            input_vpn_pwd = self.browser.find_element_by_id('user_password')
            input_vpn_username.send_keys('ssqy024')
            input_vpn_pwd.send_keys('Tjise@1163')
            input_vpn_pwd.send_keys(Keys.ENTER)
            WebDriverWait(self.browser, 30)
            return self.browser.get_cookies()
        except TimeoutException:
            print('Time Out')
        except NoSuchElementException:
            print('No Element')

    def close_browser(self):
        self.browser.close()


class Login_Sign:
    """
    登陆签到网站
    """

    def __init__(self):
        """
        初始化数据
        """
        self.post_url = 'https://zckj.webvpn.tjise.edu.cn/userLogin/userLogin'
        self.post_sign_url = 'https://zckj.webvpn.tjise.edu.cn/sign/sign'
        self.post_signRecord_url = 'https://zckj.webvpn.tjise.edu.cn/sign/signRecord'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
            'Referer': 'https://zckj.webvpn.tjise.edu.cn/',
            'Host': 'zckj.webvpn.tjise.edu.cn',
            'Cookie': 'TGC=eyJhbGciOiJIUzUxMiJ9.ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1USTRRMEpETFVoVE1qVTJJbjAuLnJ1cHdUTVRJOHphM3Z6Rjduem1RZncueEwzX212WXIzbWdoNWUxeHNlVU43ZkF4ck1QdjRRUXlRM1BSMEktdDU4S0JJWlVNSEJYbC1NREtFUDE0SVNBblpYdnVXbG5XVS1fU1FJRXIxWmIwaGRwYkN0X2t1OXRKeXd5cE5oSFhsWXlDUVRMUndlVVdma1c3N1RMR2x3dDRLazJDUVE2b2pFT2c5YzAwWTFWZ3hJczZ6LUQ0WGpoWU9kYTg4ZVR0SHIyWXBUTkZGTFhjOU9hQk8xYlVLd3RsUkprVU1CRjQ4elJ6R0xIbGFMZ0VTUXpMTmxZNmlicEw0cG5kZDltaUlXYWM0YkpzRWRwQkFuN1dFSldPVlE4N296ZGVKczRVVWpMUlg2Y2RJZWdDZncuNFNBN0F5MTRPT084d24xNmozdEgxZw.31Wy7J_5KkT6Xzund6xBzngeiHqn8RXyK0drpVdYciNCgdh8k5Wd_DVPkmquMqZTGnesjRhWQS4dSAYnodSGDA; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic3NxeTAyNCIsImlhdCI6MTU3NjgwMzA1MiwiZXhwIjoxNTc2ODg5NDUyfQ.NJZyadnVMI3c4CZFBMT9RRgYo8GN68MM_x4W3wviuGE; webvpn_username=ssqy024%7C1576803052%7C90527cd10c9303b79330e7d5730b0ce256b66990; SESSION=7046d40a-26ad-467e-82cf-ce9d9da71aed',
            'Origin': 'https://zckj.webvpn.tjise.edu.cn'
        }
        self.session = requests.Session()
        self.sign_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Referer': 'https://zckj.webvpn.tjise.edu.cn/view/index/index',
            'Host': 'zckj.webvpn.tjise.edu.cn',
            'Cookie': 'TGC=eyJhbGciOiJIUzUxMiJ9.ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1USTRRMEpETFVoVE1qVTJJbjAuLnJ1cHdUTVRJOHphM3Z6Rjduem1RZncueEwzX212WXIzbWdoNWUxeHNlVU43ZkF4ck1QdjRRUXlRM1BSMEktdDU4S0JJWlVNSEJYbC1NREtFUDE0SVNBblpYdnVXbG5XVS1fU1FJRXIxWmIwaGRwYkN0X2t1OXRKeXd5cE5oSFhsWXlDUVRMUndlVVdma1c3N1RMR2x3dDRLazJDUVE2b2pFT2c5YzAwWTFWZ3hJczZ6LUQ0WGpoWU9kYTg4ZVR0SHIyWXBUTkZGTFhjOU9hQk8xYlVLd3RsUkprVU1CRjQ4elJ6R0xIbGFMZ0VTUXpMTmxZNmlicEw0cG5kZDltaUlXYWM0YkpzRWRwQkFuN1dFSldPVlE4N296ZGVKczRVVWpMUlg2Y2RJZWdDZncuNFNBN0F5MTRPT084d24xNmozdEgxZw.31Wy7J_5KkT6Xzund6xBzngeiHqn8RXyK0drpVdYciNCgdh8k5Wd_DVPkmquMqZTGnesjRhWQS4dSAYnodSGDA; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic3NxeTAyNCIsImlhdCI6MTU3NjgwMzA1MiwiZXhwIjoxNTc2ODg5NDUyfQ.NJZyadnVMI3c4CZFBMT9RRgYo8GN68MM_x4W3wviuGE; webvpn_username=ssqy024%7C1576803052%7C90527cd10c9303b79330e7d5730b0ce256b66990; SESSION=7046d40a-26ad-467e-82cf-ce9d9da71aed',
            'Origin': 'https://zckj.webvpn.tjise.edu.cn'
        }

    def login_site(self, data, name):
        response = self.session.post(url=self.post_url, data=data, headers=self.headers)
        if response.status_code == 200:
            print(name + "登陆成功！")

    def sign_site(self, name):
        response_signRecord = requests.post(url=self.post_signRecord_url, headers=self.sign_headers)
        response_sign = requests.post(url=self.post_sign_url, headers=self.sign_headers)
        if response_sign.status_code == 200 and response_signRecord.status_code == 200:
            result = json.loads(response_sign.text)
            print(name + result["message"])


def init_data():
    data = [
        {
            "name": "韩思远",
            "login_data": {
                'userId': 'MTc2OTU1MzgwNTM=',
                'pwd': 'U1FMU2VydmVyMjAxNA==',
                'name': 'MTc2OTU1MzgwNTM='
            }
        },
        {
            "name": "张翔宇",
            "login_data": {
                'userId': 'MTMwMDEzNjA3ODg=',
                'pwd': 'Z3h6Y2xtMjAxNw==',
                'name': 'MTMwMDEzNjA3ODg ='
            }
        },
        {
            "name": "李赛",
            "login_data": {
                'userId': 'MTM4MjAzMjE2NTU=',
                'pwd': 'bGlzYWk1MjA=',
                'name': 'MTM4MjAzMjE2NTU='
            }
        },
        {
            "name": "王姝琪",
            "login_data": {
                'userId': 'MTM2NTIxMDU5NDg=',
                'pwd': 'MTM2NTIxMDU5NDh3c3E=',
                'name': 'MTM2NTIxMDU5NDg='
            }
        },
        {
            "name": "庄莹莹",
            "login_data": {
                'userId': 'MTUwMjI1MDkwMDg=',
                'pwd': 'UmcxNTAyMjUwOTAwOA==',
                'name': 'MTUwMjI1MDkwMDg='
            }
        },
        {
            "name": "周彦冰",
            "login_data": {
                'userId': 'MTg5MDM4MzU3NjE=',
                'pwd': 'MTk5NzY3enli',
                'name': 'MTg5MDM4MzU3NjE='
            }
        },
        {
            "name": "程玺",
            "login_data": {
                'userId': 'MTM4MjE5MTExNjM=',
                'pwd': 'ODU1NnoxODU=',
                'name': 'MTM4MjE5MTExNjM='
            }
        },
        {
            "name": "齐之健",
            "login_data": {
                'userId': 'MTgyMDI1NTYwMTY=',
                'pwd': 'MTIzNDU2QWE=',
                'name': 'MTgyMDI1NTYwMTY='
            }
        },
        {
            "name": "刘纾羽",
            "login_data": {
                'userId': 'MTM1MTI4MDgxNjY=',
                'pwd': 'eHk4NDI4Nzc3OA==',
                'name': 'MTM1MTI4MDgxNjY='
            }
        },
        {
            "name": "要彪",
            "login_data": {
                'userId': 'MTM2NTIwMzU3MTc=',
                'pwd': 'cmcxMTExMTE=',
                'name': 'MTM2NTIwMzU3MTc='
            }
        },
        {
            "name": "江越",
            "login_data": {
                'userId': 'MTU5MjIwNjM1MTE=',
                'pwd': 'cmcxMTExMTE=',
                'name': 'MTU5MjIwNjM1MTE='
            }
        },
        {
            "name": "李林",
            "login_data": {
                'userId': 'MTM5MjAwOTYxMjM=',
                'pwd': 'cmcxMTExMTE=',
                'name': 'MTM5MjAwOTYxMjM='
            }
        },
        {
            "name": "王晓东",
            "login_data": {
                'userId': 'MTM4MjE1NzgxODE=',
                'pwd': 'cmcxMTExMTE=',
                'name': 'MTM4MjE1NzgxODE='
            }
        },
        {
            "name": "张洪亮",
            "login_data": {
                'userId': 'MTg2MjI0NTIxMDA=',
                'pwd': 'cmcxMTExMTE=',
                'name': 'MTg2MjI0NTIxMDA='
            }
        },
    ]

    return data


if __name__ == "__main__":

    data = init_data()
    # vpn_login = Login_vpn()

    count = 0
    try:
        for one_data in data:   
            sign_login = Login_Sign()
            sign_login.login_site(data=one_data["login_data"], name=one_data["name"])
            sign_login.sign_site(name=one_data["name"])
            count += 1
            time.sleep(10)
    finally:
        # vpn_login.close_browser()
        print("共" + str(count) + "人签到." + "拜拜！")
