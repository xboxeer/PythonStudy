import scrapy
class QuoteSpider(scrapy.Spider):
    name="quotes"

    def start_requests(self):
        urls=["http://pythonwhy.net/"]
        for url in urls:
            yield scrapy.Request(url,callback=self.parse)
    
    def parse(self,response):
        for post in response.css(".entry-header"):
            yield {
                "Title":post.css(".entry-title a::text").extract_first(),
                "Posted Time":post.css(".entry-date").css(".published").css(".updated::attr(datetime)").extract_first()
                }
        '''
        postsUrl=response.css(".entry-title a::attr(href)").extract()        
        for url in postsUrl:
            nextpage=response.urljoin(url)
            print("visiting page %s"%url)
            yield scrapy.Request(nextpage,callback=self.parse)
        '''
