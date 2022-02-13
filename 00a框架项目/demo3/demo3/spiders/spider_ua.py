#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy


class TupianSpider(scrapy.Spider):
    name = 'spider_ua'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/get']

    def parse(self, response):
        print(response.text)
