
import requests

# 访问测试
url = "http://183.230.147.88:8081/"
r = requests.get(url)
print("状态码：",r)
print("网页内容：",r.text)