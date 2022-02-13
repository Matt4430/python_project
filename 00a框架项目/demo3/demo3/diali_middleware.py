#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :music_rename.py
# @Time      :2022/1/23 13:59
# @Author    :杨晓东
# @email     :lzj155@foxmail.com
# @homepage  :www.demo443.com
import requests
import re

# 设置ip代理
class Daili_Middleware(object):
    def process_request(self, request, spider):
        url = "http://proxy.httpdaili.com/apinew.asp?ddbh=1487181651686534893"
        r = requests.get(url)
        print("代理ip状态码：", r.status_code)
        t = r.text
        # 正则匹配ip段and端口号
        ips = re.findall(r'[0-9]+(?:\.[0-9])+.+[0-9]{3}', t)
        print('当前代理ip为：',ips[0])
        # proxy = {'http': ips[0]}
        # print("当前代理ip地址为：", proxy)
        print('http://' + str(ips[1]))
        request.meta['proxy'] = 'http://' + str(ips[1])
