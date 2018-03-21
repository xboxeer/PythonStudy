import scrapy
import re
from scrapy.loader import ItemLoader
from scrapy.loader.processors import *
from w3lib.html import remove_tags
class liepingSpider(scrapy.Spider):
    name="lieping"
    def start_requests(self):
        urls=["https://www.liepin.com/zhaopin/?industries=&dqs=&salary=&jobKind=&pubTime=&compkind=&compscale=&industryType=&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=15&flushckid=0&fromSearchBtn=1&headckid=e3bc6ad922873bea&d_headId=1796cc790db7c08896d574f034127a0b&d_ckId=1796cc790db7c08896d574f034127a0b&d_sfrom=search_fp_bar&d_curPage=0&d_pageSize=40&siTag=ftVHkPjdkRvUB2FzA5IaTg~fA9rXquZc5IkJpXC-Ycixw&key=%E8%9E%8D%E8%B5%84%E6%80%BB%E7%9B%91"]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
    def parse(self, response):
        i=ItemLoader(item=jobInfo(),response=response)
        i.context['SalaryUnit']='元'
        i.add_css("Title",".job-info h3::attr(title)")
        i.add_css("Salary",".text-warning::text")
        return i.load_item()
def salaryFilter(value):
    if(value=="面议"):
        print('Hit SalaryFilter!')
        return "穷逼"
    else:
        return value
def parseSalaryUnit(text,loader_context):
    text+=loader_context.get("SalaryUnit")
    print('Hit parseSalaryUnit!')
    return text
class jobInfo(scrapy.Item):
    Title=scrapy.Field(
        input_processor=MapCompose(remove_tags),
        #output_processor=Join()
    )
    Salary=scrapy.Field(
        input_processor=MapCompose(salaryFilter),
        output_processor=MapCompose(parseSalaryUnit)
    )
    


'''class jobInfoLoader(ItemLoader):
    
    default_output_processor=TakeFirst()
    Title_in=
'''
job=jobInfo(Title="Director",Salary="10000")
print(job["Title"])
print(job)

