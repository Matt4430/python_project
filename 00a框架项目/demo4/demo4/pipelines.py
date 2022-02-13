#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Demo4Pipeline:
    def __init__(self):
        self.file = open('./我真不是盖世高人.txt', 'w',  encoding='utf-8')


    def process_item(self, item, spider):
        self.file.write(item['title'])
        self.file.write(item['content'])

        return item

    def close_spider(self):
        self.file.close()



