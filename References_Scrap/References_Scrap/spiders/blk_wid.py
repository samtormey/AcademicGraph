import scrapy

class Ref_Goodies(scrapy.Item):    
    field_num1 = scrapy.Field()    
    field_num2 = scrapy.Field()
    field_num2 = scrapy.Field()
    field_num3 = scrapy.Field()
    field_num4 = scrapy.Field()
    field_num5 = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "bkwd"
    allowed_domains = ["apps.webofknowledge.com"]
    start_urls = [
        "https://apps.webofknowledge.com/CitingArticles.do?product=WOS&REFID=370688&SID=1FPLgaM74RsbI75AHNJ&search_mode=CitingArticles&parentProduct=UA&parentQid=56&parentDoc=13&excludeEventConfig=ExcludeIfFromNonInterProduct",
    ]

    def parse(self, response):
        thing = response.css('.refine-subitem-title')        
        item = Ref_Goodies()
        item['field_num1'] = thing[0].css('label::text').extract()
        item['field_num2'] = thing[1].css('label::text').extract()
        item['field_num3'] = thing[2].css('label::text').extract()
        item['field_num4'] = thing[3].css('label::text').extract()
        item['field_num5'] = thing[4].css('label::text').extract()
        return item


