import requests
import re

post_url = 'https://webvpn.tjise.edu.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Cookie': 'SERVERID=Server1; TGC=""; _webvpn_key=eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoic3NxeTAyNCIsImlhdCI6MTU3NTQ0MzQyOCwiZXhwIjoxNTc1NTI5ODI4fQ.0bff7dJVhD-zYprdF_NnY1EK3aJy55e61jXpPvL2kno; webvpn_username=ssqy024%7C1575443428%7Ca6855eb8527aebbd9e3db59d99bbacd849fdae12; _astraeus_session=clI5Kzk1dGt0Q2xhTmZ6QU9mWmx1RFZzM1JxNUkwTkJxR0dHd1BkWnlYOWFmU1NKZStpSjhGR1lQN2s1UlordW4ySENZUHR6eWhwcmhxbmJQUnA1U0NzM0JmZTExU0Myd1RmZENiNjlRaUFXNzVVazF1UksyNmJQc1NZaHJmc0plV0s2VE1WR0JPWHp4TXJOdnRaMXNNbENoaHdVLy9raklsUk9qeHVENHVRK3luRGtCSnYyZU1ESFZsS1lqMVVrK0x1OVAzcDNLbTBZcmVoWmpXRzVCOGFpVk53cndORnI5M2UwTlhzaTdhWlFiQi9xa2s0T1JKb28zREJYeUFmUVlhak9zc3R2cDM1MTZUNkp2WHNyMllZcnFWeE5tZzJ1TjUvSlg4R1VUbFE3WWtqRzZvaTlaTVJLRENreG1xeGNqWnNIZGZaMjlsWVFJZlhPY004b2xURmpORzIyajkvMXdXZTN3Q3NkbkU1QzEzUGZYcURGc3piQ2dPb3h6TUhXLS1yeWx1OStPOStaajQvaUJ4TTh5cDBnPT0%3D--420e5b6cefd611fe8bc55ec6ba732bc65be399ff',
    'Host':'webvpn.tjise.edu.cn',
    'Referer': 'https://webvpn.tjise.edu.cn/users/sign_in',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1'
}
response = requests.get(post_url, headers=headers)
print(response.text)