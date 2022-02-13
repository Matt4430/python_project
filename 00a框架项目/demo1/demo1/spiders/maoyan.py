import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://www.maoyan.com/films?showType=1']

    def parse(self, response):
        print('爬虫程序开始运行.................')
        name = response.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[2]/a/text()').extract()
        socer = response.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[3]')
        ss = []
        for i in socer:
            a = i.xpath('string(.)').extract_first()
            print('a:::::::::::',a)
        print(name)
        print(socer)

        print(type(name))
