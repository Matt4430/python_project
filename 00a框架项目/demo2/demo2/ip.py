#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :music_rename.py
# @Time      :2022/1/23 13:59
# @Author    :杨晓东
# @email     :lzj155@foxmail.com
# @homepage  :www.demo443.com
import random

import requests
import re
def matt():
    url = 'http://proxy.httpdaili.com/apinew.asp?ddbh=1483645335587534893'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    r = requests.get(url,headers=headers)
    print("代理ip状态码：", r.status_code)
    t = r.text
    # 正则匹配ip段and端口号
    ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
    # print(ips[random.randint(0,1)])
    # proxy = {'http': ips[0]}
    # print("当前代理ip地址为：", proxy)

    return ips[random.randint(0,1)]


if __name__ == "__main__":
    matt()
