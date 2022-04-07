#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py_venv -> Mtxt.py
# @IDE       :PyCharm
# @Time      :2022/4/6 23:18
# @Author    :杨晓东
# @Email     :lzj155@foxmail.com
# @homepage  :www.demo520.com

import requests
from lxml import etree
import sys
import time


def run(url, head='https://yazhouse8.com/'):
    proxy = '127.0.0.1:4780'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
    req = requests.get(url, headers=headers, proxies=proxies, timeout=30)
    # print(req.text)
    # req.encoding = 'utf-8'
    html = etree.HTML(req.text)
    # print(html)
    aa = []
    for i in range(2, 55):
        url_1 = html.xpath('/html/body/div[1]/div/div[' + str(i) + ']/p/a/@href')
        if url_1 != aa:
            print(url_1, "不为空")

            # 详情页url
            new_url = head + ''.join(url_1)
            print(new_url)
            # 详情页保存函数
            data(new_url)
        else:
            print(url_1, "为空")
            continue

    n_url = html.xpath('/html/body/nav[2]/ul/li[2]/a/@href')
    next_url = head + ''.join(n_url)
    print(next_url)
    run(next_url)


def data(url, head='https://yazhouse8.com/'):
    global c
    global b
    try:
        proxy = '127.0.0.1:4780'
        proxies = {
            'http': 'http://' + proxy,
            'https': 'http://' + proxy
        }

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
        req = requests.get(url, headers=headers, proxies=proxies, timeout=30)
        # print(req.text)
        # req.encoding = 'utf-8'
        html = etree.HTML(req.text)
        with open('./M小说.txt', 'a', encoding='utf-8') as f:
            # print(html)
            h1 = html.xpath('/html/body/div[1]/div/div[2]/h1/text()')[0]
            print('标题： ', h1)
            if h1 == '游泳池的人妻':
                print("爬取完毕，自动退出....................................")
                exit(0)
            else:
                f.write('\t' + '第{}章_'.format(c) + h1 + '\n')

                print('第{}章_'.format(c) + h1 + '标题已写入....')
                content = html.xpath('/html/body/div[1]/div/div[2]/div[1]/div/text()')
                print(content)
                for i in content:
                    u = i.replace('\u3000', '').replace('\xa0', '').replace('==记住==', '').replace('网址:', '').replace(
                        '??', '')
                    print(u)
                    f.write(u + '\n')
                print("内容已写入.....")

                # next_url = html.xpath('/html/body/div[1]/div/div[2]/div[1]/div/ul/li/a[3]/@href')
                # nurl = head + ''.join(next_url)
                # url = nurl
                print('第{}章_'.format(c) + h1 + '标题已写入....')
                print('已经爬取了 {} 章小说'.format(c))
                c += 1
    except:
        try:
            proxy = '127.0.0.1:4780'
            proxies = {
                'http': 'http://' + proxy,
                'https': 'http://' + proxy
            }

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
            req = requests.get(url, headers=headers, proxies=proxies, timeout=30)
            # print(req.text)
            # req.encoding = 'utf-8'
            html = etree.HTML(req.text)
            with open('./M小说.txt', 'a', encoding='utf-8') as f:
                # print(html)
                h1 = html.xpath('/html/body/div[1]/div/div[2]/h1/text()')[0]
                print('标题： ', h1)
                if h1 == '游泳池的人妻':
                    print("爬取完毕，自动退出....................................")
                    exit(0)
                else:
                    f.write('\t' + '第{}章_'.format(c) + h1 + '\n')

                    print('第{}章_'.format(c) + h1 + '标题已写入....')
                    content = html.xpath('/html/body/div[1]/div/div[2]/div[1]/div/text()')
                    # print(content)
                    for i in content:
                        u = i.replace('\u3000', '').replace('\xa0', '').replace('==记住==', '').replace('网址:', '')
                        print(u)
                        f.write(u + '\n')
                    print("内容已写入.....")

                    # next_url = html.xpath('/html/body/div[1]/div/div[2]/div[1]/div/ul/li/a[3]/@href')
                    # nurl = head + ''.join(next_url)
                    # url = nurl
                    print('第{}章_'.format(c) + h1 + '标题已写入....')
                    print('已经爬取了 {} 章小说'.format(c))
                    c += 1

        except:

            print("第  {}  章小说异常....".format(c))
            b += 1

    print("共  {}  本小说异常....".format(b))


if __name__ == "__main__":
    url = 'https://yazhouse8.com/Ryuid.htm'
    # 异常计数
    b = 0
    # 章节计数
    c = 1

    run(url)
