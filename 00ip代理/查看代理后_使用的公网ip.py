#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :music_rename.py
# @Time      :2022/1/23 13:59
# @Author    :杨晓东
# @email     :lzj155@foxmail.com
# @homepage  :www.demo443.com

import requests
from lxml import etree
import ssl
import re


def ip_data():
    url = "http://proxy.httpdaili.com/apinew.asp?ddbh=1487181651686534893"
    r = requests.get(url)
    print("代理ip状态码：", r.status_code)
    t = r.text
    # 正则匹配ip段and端口号
    ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
    print('当前代理ip为：', ips[0])
    url2 = 'https://tool.lu/ip/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    # session = requests.Session()
    # session.trust_env = False
    # req = session.get(url=url, headers=headers, verify=False, timeout=20)
    req = requests.get(url=url2, headers=headers, proxies={"https": "http://" + ips[0]}, timeout=5)

    # 输出状态码
    print(req)

    html_ip = etree.HTML(req.text)

    # 测试代理ip是否能用
    data = html_ip.xpath('//*[@id="main_form"]/p[1]/text()')
    print(data)


if __name__ == '__main__':
    ip_data()
