# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
class TurtoralPipeline(object):
    def process_item(self, item, spider):
        return item
#Item Pipeline在Item_Processor之后
class jobInfoPipline(object):
    def process_item(self,item,spider):
        if(item['Salary']):
            print("pipeline hit!")
            print(item['Salary'])
            matches=[re.match('(\d+)-[^.]*',salary).groups()[0] for salary in item['Salary'] if re.match('(\d+)-[^.]*',salary)!=None]
            print(matches)
        return item
