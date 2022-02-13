#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :run_zhaobiao.py
# @Time      :2022/2/7 11:40
# @Author    :杨晓东
# @email     :lzj155@foxmail.com

from scrapy import cmdline


def run():
    # 方式一：注意execute的参数类型为一个列表
    cmdline.execute('scrapy crawl zhaobiao'.split())


if __name__ == "__main__":
    run()
