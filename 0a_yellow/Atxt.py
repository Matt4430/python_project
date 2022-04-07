#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py_venv -> Atxt.py
# @IDE       :PyCharm
# @Time      :2022/4/4 21:39
# @Author    :杨晓东
# @email     :lzj155@foxmail.com
# @homepage  :www.demo520.com

import requests
from lxml import etree


def run(head='https://yazhouse8.com/'):
    url = 'https://yazhouse8.com/article/{}.html'
    b = 0
    c = 0
    for j in range(32508,999999999):
        c += 1
        try:
            proxy = '127.0.0.1:4780'
            proxies = {
                'http': 'http://' + proxy,
                'https': 'http://' + proxy
            }

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
            req = requests.get(url.format(j), headers=headers, proxies=proxies)
            # print(req.text)
            # req.encoding = 'utf-8'
            html = etree.HTML(req.text)
            with open('./A小说.txt', 'a', encoding='utf-8') as f:
                # print(html)
                h1 = html.xpath('/html/body/div[1]/div/div[2]/h1/text()')[0]
                print('标题： ', h1)
                f.write('\t' + '第{}章_'.format(c) + h1 + '\n')
                print('标题已写入....')
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
                print('下一页链接： ', url.format(j + 1))
                print(h1 + '  已写入....')
                print('已经爬取了 {} 章小说'.format(c))
        except:
            try:
                proxy = '127.0.0.1:4780'
                proxies = {
                    'http': 'http://' + proxy,
                    'https': 'http://' + proxy
                }

                headers = {
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
                req = requests.get(url.format(j), headers=headers, proxies=proxies)
                # print(req.text)
                # req.encoding = 'utf-8'
                html = etree.HTML(req.text)
                with open('./A小说.txt', 'a', encoding='utf-8') as f:
                    # print(html)
                    h1 = html.xpath('/html/body/div[1]/div/div[2]/h1/text()')[0]
                    print('标题： ', h1)
                    f.write('\t' + '第{}章_'.format(c) + h1 + '\n')

                    print('标题已写入....')
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
                    print('下一页链接： ', url.format(j + 1))
                    print(h1 + '  已写入....')
                    print('已经爬取了 {} 章小说'.format(c))

            except:
                c -= 1
                b += 1
                print("第  {}  本小说异常....".format(c))
                continue
    print("共  {}  本小说异常....".format(b))


if __name__ == "__main__":
    url = 'https://yazhouse8.com/article/32508.html'
    run()
