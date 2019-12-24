
from yanxuan.settings import USER_AGENT as ua
import random

class UserAgentSpiderMiddleware(object):
    """
          给每一个请求随机切换一个User-Agent
    """

    def process_request(self, request, spider):
        user_agent = random.choice(ua)
        request.headers['User-Agent'] = user_agent
