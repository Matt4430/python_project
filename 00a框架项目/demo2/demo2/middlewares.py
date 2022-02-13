#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import requests
import re

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

# 设置代理ip   settings中启用
class Demo2_ip(object):
    def process_request(self, request, spider):
        ip_list = [
            '114.239.127.217:4231',
            '119.112.83.122:4213',
            '119.7.146.196:4258',
            '114.239.1.197:4246',
            '125.79.200.146:4231',
            '42.56.236.255:4275'

        ]
        proxy = random.choice(ip_list)
        request.meta['proxy'] = proxy


class Demo2SpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Demo2DownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # 随机选中一个ip
        ip = random.choice(ipPool)
        print('当前ip', ip, '-----', count['count'])
        # 更换request的ip----------这句是重点
        request.meta['proxy'] = ip
        # 如果循环大于某个值,就清理ip池,更换ip的内容
        if count['count'] > 10:
            print('-------------切换ip------------------')
            count['count'] = 0
            ipPool.clear()
            ips = requests.get('http://proxy.httpdaili.com/apinew.asp?ddbh=1483645335587534893')
            for ip in ips.text.split('\r\n'):
                ipPool.append('http://' + ip)
                print("代理ip：", ip)
        # 每次访问,计数器+1
        count['count'] += 1

        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
