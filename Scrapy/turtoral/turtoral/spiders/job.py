import scrapy
import re
class jobSpider(scrapy.Spider):
    name="job"
    
    def __init__(self):
        scrapy.Spider.__init__(self)
        self.headerInit=False
        self.table=[]

    def start_requests(self):
        urls=["http://www.bankhr.com/so/kj%E8%9E%8D%E8%B5%84.html"]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)


    def parse(self,response):
        for links in response.css(".td_sp1 a::attr(href)").extract():
            nextPage=response.urljoin(links)
            yield scrapy.Request(nextPage,callback=self.parseBody)

    def parseBody(self,response):
        print("print table")
        for item in self.table:            
            print(item)
        record=list()
        header=list()
        if(self.headerInit == False):
            header.append("职位")
            header.append("公司")
        position=response.css(".wrap_title h1::text").extract_first()
        record.append(position)
        company=response.css(".info_lf").css("h3 a::text").extract_first()
        record.append(company)
        for jobinfo in response.css(".job_info li"):
            if(self.headerInit==False):
                header.append(jobinfo.css("span::text").extract_first())
            record.append(jobinfo.css("li::text").extract_first())
            if(self.headerInit==False):
                self.table.append(header)
            self.table.append(record)
        self.headerInit=True
            
