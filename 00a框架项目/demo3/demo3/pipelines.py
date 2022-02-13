# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class Demo3Pipeline:
    def process_item(self, item, spider):
        return item

class ImagePipelines(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'image_name':item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name = request.meta['image_name']
        return '/full/{}.jpg'.format(file_name)
