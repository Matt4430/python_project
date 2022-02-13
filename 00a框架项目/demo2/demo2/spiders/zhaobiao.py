#!/usr/bin/python
# -*- coding: UTF-8 -*-

import scrapy
import requests


class ZhaobiaoSpider(scrapy.Spider):
    name = 'zhaobiao'
    allowed_domains = ['ccgp.gov.cn']
    start_urls = ['http://www.ccgp.gov.cn/cggg/zygg/gkzb/index.htm']

    def parse(self, response):
        biaoti_url = response.xpath('//*[@id="detail"]/div[2]/div/div[1]/div/div[2]/div[1]/ul/li/a/@href').extract()
        # print(biaoti_url)
        self.get_ip()

        for i in biaoti_url:
            url = response.urljoin(i)
            # print(url)
            yield scrapy.Request(response.urljoin(i), callback=self.parse1)
        for j in range(1, 25):
            next_url = 'http://www.ccgp.gov.cn/cggg/zygg/gkzb/index_{}.htm'.format(j)
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

        self.get_ip()

    def get_ip(self):
        url = 'http://icanhazip.com/'
        req = requests.get(url)
        print('当前爬虫的ip是：', req.text)

    def parse1(self, response):
        大标题 = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[1]/h2//text()').extract_first()
        采购项目名称 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[2]/td[2]//text()').extract_first()
        品目 = response.xpath('//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[3]/td[2]//text()').extract_first()
        采购单位 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[4]/td[2]//text()').extract_first()
        行政区域 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[2]//text()').extract_first()
        公告时间 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[5]/td[4]//text()').extract_first()
        获取招标文件时间 = str(response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[6]/td[2]//text()').extract()).replace('[',
                                                                                                           '').replace(
            ']', '').replace("'", '').replace(r"\xa0", ' ')
        招标文件售价 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[7]/td[2]//text()').extract_first()
        获取招标文件的地点 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[8]/td[2]//text()').extract_first()
        开标时间 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[9]/td[2]//text()').extract_first()
        开标地点 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[10]/td[2]//text()').extract_first()
        预算金额 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[11]/td[2]//text()').extract_first()
        项目联系人 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[13]/td[2]//text()').extract_first()
        项目联系电话 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[14]/td[2]//text()').extract_first()
        采购单位地址 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[16]/td[2]//text()').extract_first()
        采购单位联系方式 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[17]/td[2]//text()').extract_first()
        代理机构名称 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[18]/td[2]//text()').extract_first()
        代理机构地址 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[19]/td[2]//text()').extract_first()
        代理机构联系方式 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[20]/td[2]//text()').extract_first()
        a1_url = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[23]/td[2]/a/@href').extract_first()
        fujian_url_1 = response.urljoin(a1_url)
        fu_name_1 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[22]/td[2]//text()').extract_first()
        附件1 = str(fu_name_1) + '-' + str(fujian_url_1)

        a2_url = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[23]/td[2]/a/@href').extract_first()
        fujian_url_2 = response.urljoin(a2_url)
        fu_name_2 = response.xpath(
            '//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tr[23]/td[2]//text()').extract_first()
        附件2 = str(fu_name_2) + '-' + str(fujian_url_2)
        yield {
            "大标题": 大标题,
            "采购项目名称": 采购项目名称,
            "品目": 品目,
            "采购单位": 采购单位,
            "行政区域": 行政区域,
            "公告时间": 公告时间,
            "获取招标文件时间": 获取招标文件时间,
            "招标文件售价": 招标文件售价,
            "获取招标文件的地点": 获取招标文件的地点,
            "开标时间": 开标时间,
            "开标地点": 开标地点,
            "预算金额": 预算金额,
            "项目联系人": 项目联系人,
            "项目联系电话": 项目联系电话,
            "采购单位地址": 采购单位地址,
            "采购单位联系方式": 采购单位联系方式,
            "代理机构名称": 代理机构名称,
            "代理机构地址": 代理机构地址,
            "代理机构联系方式": 代理机构联系方式,
            "附件1": 附件1,
            "附件2": 附件2
        }
