import scrapy

class Ref_Goodies(scrapy.Item):    
    link = scrapy.Field()

class DmozSpider(scrapy.Spider):
    name = "arph"
    allowed_domains = ["apps.webofknowledge.com"]
    start_urls = [
        "https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=56&SID=1FPLgaM74RsbI75AHNJ&page=1&doc=1",
    ]

    def parse(self, response):
        sel = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "l-block", " " ))]//p[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]')
        item = Ref_Goodies()
        item['link'] = sel.xpath('a/@href').extract()
        next_url = response.url
        print next_url
        next_next_url = next_url.split("&doc=")
        print len(next_next_url)
        next_next_next_url = next_next_url[0] + '&doc=' + str(int(next_next_url[1])+1)
        #next_url = "https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=56&SID=1FPLgaM74RsbI75AHNJ&page=1&doc=2"
        return scrapy.Request(next_next_next_url,callback=self.parse), item

