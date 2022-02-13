#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :music_rename.py
# @Time      :2022/1/23 13:59
# @Author    :杨晓东
# @email     :lzj155@foxmail.com
# @homepage  :www.demo443.com

import time

import requests

url = 'http://www.abc.com/test.html'

last_modified = ''


def get_page():
    global last_modified
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3','Connection': 'keep-alive'}

    if last_modified:
        headers['If-Modified-Since'] = last_modified
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        if last_modified and last_modified is not res.headers['Last-Modified']:
            print('page has changed\r')
            return False

        last_modified = res.headers['Last-Modified']

    elif res.status_code == 304:
        print('normal\r')
        return True

if __name__ == '__main__':

    while 1:
        result = get_page()
        if result:
            time.sleep(2)
        else:
            break
