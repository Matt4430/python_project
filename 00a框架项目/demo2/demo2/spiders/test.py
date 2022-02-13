#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :music_rename.py
# @Time      :2022/1/23 13:59
# @Author    :杨晓东
# @email     :lzj155@foxmail.com
# @homepage  :www.demo443.com

import requests
from lxml import etree




def matt():
    url = 'http://www.ccgp.gov.cn/cggg/zygg/gkzb/202201/t20220124_17548466.htm'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
    req = requests.get(url,headers=headers)
    req.encoding = "utf-8"
    # print(req.text)
    text = req.text
    print(req.status_code)
    ht = etree.HTML(text)
    print(text)
    a = ht.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[3]/td[2]//text()')
    # for i in a:
    #     print('iiiiiiiiiiiii',i)
    #     b = i.xpath('//text()')
    #     print(b)
    a1_url = ht.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[22]/td[2]/*[@class="bizDownload"]/@href')
    # fujian_url_1 = ht.urljoin(a1_url)
    fu_name_1 = ht.xpath(
                        '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[22]/td[2]//text()')[0]
    附件1 = str(fu_name_1) + '-' + str(a1_url)

    print('aaaaaaaaaaa',a)
    print(url)
    print('附件1附件1附件1附件1附件1',附件1)


if __name__ == "__main__":
    matt()
