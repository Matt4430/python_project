#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py_venv -> 模板_格式_code.py
# @IDE       :PyCharm
# @Time      :2022/4/6 23:15
# @Author    :杨晓东
# @Email     :lzj155@foxmail.com
# @homepage  :www.demo520.com


import requests
from lxml import etree


def run():
    url = "https://www.baidu.com"
    proxy = '127.0.0.1:4780'
    proxies = {"http": "http://" + proxy, "https": "http://" + proxy}

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}
    req = requests.get(url, headers=headers, proxies=proxies)
    print(req.text)


if __name__ == "__main__":
    run()
