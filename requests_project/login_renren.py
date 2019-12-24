# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 16:45
# @Author  : SiYuan Han
# @Email   : 422295068@qq.com
# @File    : login_renren.py
# @Software: PyCharm
import requests

session = requests.session()
post_url = 'http://www.renren.com/ajaxLogin/login'
# proxies = {'http': 'http://221.6.138.154:41880'}
data = {
    'email': 17695538053,
    'password': 'SQLServer2014'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'Cookie': 'anonymid=jzb08knxqjqzu8; depovince=TJ; _r01_=1; ick_login=720b1931-4a91-40ff-9fb2-045e7b6f70df; ick=8534b0e6-3fbb-48f0-89cb-2056dea89bf8; XNESSESSIONID=24cb9dd958dc; JSESSIONID=abc0mRPYgcbh47ygdtpYw; wp_fold=0; jebecookies=05ed60fc-4be7-4d76-802e-d33726d3f8a4|||||; _de=BE9BD5302B154564B4DBCBAA039A711F; p=2063081485c3bf7d504d9dd2bca045813; first_login_flag=1; ln_uact=17695538053; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=1a0692301f829ecef215a210a6e0d5fb3; societyguester=1a0692301f829ecef215a210a6e0d5fb3; id=971915203; xnsid=70af1806; ver=7.0; loginfrom=null; vip=1'
}
# result = session.post(post_url, headers=headers, data=data, proxies=proxies)
# result = session.post(post_url, headers=headers, data=data)
# r = session.get('http://www.renren.com/971915203', headers=headers)
#


# result = requests.get('http://www.renren.com/971915203', headers=headers)
#
# with open('renren.html', 'w', encoding='utf-8') as f:
#     f.write(result.content.decode())

cookies = 'anonymid=jzb08knxqjqzu8; depovince=TJ; _r01_=1; ick_login=720b1931-4a91-40ff-9fb2-045e7b6f70df; ick=8534b0e6-3fbb-48f0-89cb-2056dea89bf8; XNESSESSIONID=24cb9dd958dc; JSESSIONID=abc0mRPYgcbh47ygdtpYw; wp_fold=0; jebecookies=05ed60fc-4be7-4d76-802e-d33726d3f8a4|||||; _de=BE9BD5302B154564B4DBCBAA039A711F; p=2063081485c3bf7d504d9dd2bca045813; first_login_flag=1; ln_uact=17695538053; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=1a0692301f829ecef215a210a6e0d5fb3; societyguester=1a0692301f829ecef215a210a6e0d5fb3; id=971915203; xnsid=70af1806; ver=7.0; loginfrom=null; vip=1'
cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split('; ')}
print(cookies)

result = requests.get('http://www.renren.com/971915203', headers=headers,cookies=cookies)