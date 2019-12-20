from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import requests

browser = webdriver.Chrome()
try:
    get_url = 'https://zckj.webvpn.tjise.edu.cn/'
    post_url = 'https://zckj.webvpn.tjise.edu.cn/userLogin/userLogin'
    vpn_url = 'https://webvpn.tjise.edu.cn/'
    browser.get(vpn_url)
    # 登陆vpn
    input_vpn_username = browser.find_element_by_id('user_login')
    input_vpn_pwd = browser.find_element_by_id('user_password')
    input_vpn_username.send_keys('ssqy024')
    input_vpn_pwd.send_keys('Tjise@1163')
    input_vpn_pwd.send_keys(Keys.ENTER)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
        'Referer': 'https://zckj.webvpn.tjise.edu.cn/',
        'Host': 'zckj.webvpn.tjise.edu.cn',
        'Cookie': 'TGC=""; SESSION=deee4f85-cb17-4f7e-baec-99bd5de9b4a3; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic3NxeTAyNCIsImlhdCI6MTU3NTQ0MzU1MSwiZXhwIjoxNTc1NTI5OTUxfQ.jdCiU3ddHsvX_VKngJM-XRQcquXBBzdFXdeShPvikfM; webvpn_username=ssqy024%7C1575443551%7C9e28d2f6d3927b26bb4a55afef8c31b48466c1e1',
        'Origin': 'https://zckj.webvpn.tjise.edu.cn'
    }
    hansiyuan_post_data = {
        'userId': 'MTc2OTU1MzgwNTM=',
        'pwd': 'U1FMU2VydmVyMjAxNA==',
        'name': 'MTc2OTU1MzgwNTM='
    }

    response = requests.post(url=post_url, data=hansiyuan_post_data, headers=headers)
    if response.status_code == 200:
        print("韩思远签到成功！")
    WebDriverWait(browser, 60)
    print("拜拜！")
except TimeoutException:
    print('Time Out')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
