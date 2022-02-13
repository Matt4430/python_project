import fake_useragent
from fake_useragent import UserAgent

# 实例化 user-agent 对象
ua = fake_useragent.UserAgent()
for i in range(100):
    print(UserAgent().random)
    # print(type(ua.random))
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36
# print(ua.random)  # Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)
# print(ua.random)  # Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36
