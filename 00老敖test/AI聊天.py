from time import sleep
import requests
import urllib.request
from urllib import *
x = input("主人：")
while True:
    x = urllib.parse.quote(x)
    res = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + x)
    res = res.json()
    print("机器人小云0：{} ".format(res["content"]))
    s = res["content"]
    resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s})
    resp.encoding = 'utf8'
    resp = resp.json()
    # sleep(1)
    print('机器人菲菲111111：', resp['content'])
