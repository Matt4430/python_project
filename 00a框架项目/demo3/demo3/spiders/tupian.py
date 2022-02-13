#!/usr/bin/env python
# -*- coding:utf-8 -*-

import scrapy


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['588ku.com']
    start_urls = ['https://588ku.com/figures/36.html']

    def parse(self, response):
        # print('11111111111111111111111111111111111111111111111111111111111')
        x_img_url = response.xpath('/html/body/div[2]/div[2]/div/div/div[1]/div/a/@href').extract()
        for i in x_img_url:
            # print('第1层图片URL：',str(response.urljoin(i)))
            yield scrapy.Request(response.urljoin(i), callback=self.parse1)

    def parse1(self, response):
        # print('22222222222222222222222222222222222222222222222222222222222')
        d_img_url = response.xpath('//div[@class="item-ctn"]/a/@href').extract()
        for i in d_img_url:
            # print('第二层图片URL：    ',str(response.urljoin(i)))
            yield scrapy.Request(response.urljoin(i), callback=self.parse2)

    def parse2(self, response):
        no_list = []
        # print('6666666666666666666666666666666666666666666666666666666666')
        z_img_url = response.xpath('/html/body/div[4]/div/div[3]/div[1]/div[1]/div[2]/img/@src').extract_first()
        z_img_url = response.urljoin(z_img_url)
        no_list.append(z_img_url)

        name = response.xpath('/html/body/div[4]/div/div[2]/span/span/a/text()').extract_first()
        yield {
            "image_urls": no_list,
            "name": name
        }
