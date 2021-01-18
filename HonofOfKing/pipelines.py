# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class HonofofkingPipeline:
    def __init__(self):
        self.fp = open("hero.csv","wb")
        self.exporter = CsvItemExporter(self.fp)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        print("导入了一条数据：",item['name'])
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.fp.close()
