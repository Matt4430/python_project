#!/usr/bin/env python
# -*- coding:utf-8 -*-
import scrapy


class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['5atxt.com']
    start_urls = ['https://www.5atxt.com/69_69867/54512697.html']

    def parse(self, response):
        print('爬虫开始....................')
        title = response.xpath('//*[@id="main"]/div/div/div[2]/h1//text()').extract_first()
        content = response.xpath('//*[@id="content"]//text()').extract()
        print(title)
        content = ''.join(content).replace('\xa0', '').replace('\n                    ', '').replace(
            '天才一秒记住本站地址：[笔趣阁]    https://www.5atxt.com最快更新！无广告！', '').replace('　　', '\n').replace(
            '章节错误,点此报送(免注册),    报送后维护人员会在两分钟内校正章节内容,请耐心等待。', '')
        # print(content)
        next_url = response.xpath('//*[@id="main"]/div/div/div[4]/a[4]/@href').extract_first()
        yield {
            "title": title,
            "content": content
        }
        yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
