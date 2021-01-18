# -*- coding: utf-8 -*-
import scrapy
from ..items import HeroItem
import re
import inspect

class HonorSpider(scrapy.Spider):
    name = 'honor'
    allowed_domains = ['db.18183.com']
    start_urls = ['http://db.18183.com/wzry/']

    def parse(self, response):
        hero_lis = response.xpath("//ul[@class='mod-iconlist']/li")
        for hero_li in hero_lis:
            position = hero_li.xpath("./@data-category").get()
            hero_path = hero_li.xpath("./a/@href").get()
            url = response.urljoin(hero_path)
            item = HeroItem()
            item['position'] = position
            yield scrapy.Request(url,callback=self.parse_hero,meta={"item":item})

    def parse_hero(self,response):
        item = response.meta.get('item')
        name = response.xpath("//div[@class='name-box']/h1/text()").get()
        item['name'] = name

        hero_box = response.xpath("//div[@id='hero-panel-update']")
        # 提取数据的正则表达式
        for field in item.fields.keys():
            value = hero_box.xpath(f"./dl[@class='{field}']/dt[1]/text()").get()
            if value:
                try:
                    value = re.search(r"(\d+\.?\d*)", value).group(1)
                    item[field] = float(value)
                except:
                    item[field] = re.sub(r".+：","",value)
        print("抓取了一条数据：",item['name'])
        print("="*20)
        yield item