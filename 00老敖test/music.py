# -*- coding: utf-8 -*-
import urllib.request
import requests
from lxml import etree
import json
import jsonpath
params={
        'input':'晴天',
        'filter':'name',
        'type':'kuwo',
        'page':1
    }

headers={'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',}
url='http://music.onlychen.cn/'
response=requests.post(url,data=params,headers=headers)
data = response.json()
print(data)
# url=jsonpath.jsonpath(data,'$..url')[0]
# print(url)
# title=jsonpath.jsonpath(data,'$..title')[0]
# print(title)