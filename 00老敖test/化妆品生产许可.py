#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :化妆品生产许可.py
# @Time      :2022/1/20 14:49
# @Author    :杨晓东

import requests
from lxml import etree

url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    ,'X-Frame-Options': 'SAMEORIGIN',
    'Cookie': 'JSESSIONID=02A452CA7FFCCE6D3B9B463560CFA509; acw_tc=3ccdc14d16426592548848489e70fdd4b8e8fd0694560226228575eadc829a; JSESSIONID=8ACCE1D53890F97D6F0B880E861686EB',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
req = requests.post(url,headers=headers)

req_html = etree.HTML(req.text)
print(req_html)
print(req.text)

# name = req_html.xpath('//*[@id="gzlist"]/li[1]/dl/a/text()')
# print(name)