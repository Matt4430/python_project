#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Demo2Item(scrapy.Item):
    # define the fields for your item here like:
    大标题 = scrapy.Field()
    品目 = scrapy.Field()
    采购单位 = scrapy.Field()
    行政区域 = scrapy.Field()
    公告时间 = scrapy.Field()
    获取招标文件时间 = scrapy.Field()
    招标文件售价 = scrapy.Field()
    获取招标文件的地点 = scrapy.Field()
    开标时间 = scrapy.Field()
    开标地点 = scrapy.Field()
    预算金额 = scrapy.Field()
    项目联系人 = scrapy.Field()
    项目联系电话 = scrapy.Field()
    采购单位地址 = scrapy.Field()
    采购单位联系方式 = scrapy.Field()
    代理机构名称 = scrapy.Field()
    代理机构地址 = scrapy.Field()
    代理机构联系方式 = scrapy.Field()
    附件1 = scrapy.Field()
    附件2 = scrapy.Field()
