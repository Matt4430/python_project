#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :百度首页.py
# @Time      :2022/1/20 16:12
# @Author    :杨晓东

import requests
from lxml import etree



def get_baidu():
    url = 'https://www.baidu.com/'
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    req = requests.get(url,headers=headers)
    text = req.text
    ht = etree.HTML(text)
    print(ht.xpath('//*[@class="title-content-title"]/text()'))


if __name__ == "__main__":
    get_baidu()
