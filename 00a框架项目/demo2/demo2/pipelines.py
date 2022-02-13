#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 将字段写入文件
class Demo2Pipeline:

    def __init__(self):
        self.file = open('./data.csv', 'w', newline='', encoding='utf-8')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['大标题', '采购项目名称', '品目', '采购单位', '行政区域', '公告时间', '获取招标文件时间', '招标文件售价', '获取招标文件的地点'
                                    , '开标时间', '开标地点', '预算金额', '项目联系人', '项目联系电话', '采购单位地址'
                                    , '采购单位联系方式', '代理机构名称', '代理机构地址', '代理机构联系方式', '附件1', '附件2'])

    def process_item(self, item, spider):
        self.csvwriter.writerow(
            [item["大标题"], item["采购项目名称"], item["品目"], item["采购单位"], item["行政区域"], item["公告时间"], item["获取招标文件时间"],
             item["招标文件售价"]
                , item["获取招标文件的地点"], item["开标时间"], item["开标地点"], item["预算金额"], item["项目联系人"], item["项目联系电话"],
             item["采购单位地址"]
                , item["采购单位联系方式"], item["代理机构名称"], item["代理机构地址"], item["代理机构联系方式"], item["附件1"], item["附件2"]])
        return item

    def close_spider(self, spider):
        self.file.close()
