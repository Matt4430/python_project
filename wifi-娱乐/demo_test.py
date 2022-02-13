
import requests
import random
import re
# 访问测试
url = "http://proxy.httpdaili.com/apinew.asp?sl=3&noinfo=true&text=1&ddbh=1420927609453534893"
r = requests.get(url)
print("状态码：",r)
print(r.text)
t = r.text
# t = str(t)
ip = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
print(ip)
print(type(ip))
# c = ''.join(t[0:18])
# d = ''.join(t[18:38])
# e = ''.join(t[37:])
# print(c)
# print(d)
# print(e)

# a = random.random()
# print(a)