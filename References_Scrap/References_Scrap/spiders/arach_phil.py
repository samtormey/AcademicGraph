#import scrapy
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors import LinkExtractor

#class Ref_Goodies(scrapy.Item):
    ## define the fields for your item here like:
    #link = scrapy.Field()
    #num = scrapy.Field()
    #cur_url = scrapy.Field()

#class DmozSpider(CrawlSpider):
    #name = "arph"
    #allowed_domains = ["apps.webofknowledge.com"]
    #start_urls = [
        #"https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=56&SID=1FPLgaM74RsbI75AHNJ&page=1&doc=1",
        #"https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=58&SID=1FPLgaM74RsbI75AHNJ&page=1&doc=2"
    #]

    #rule = Rule(LinkExtractor(restrict_xpaths=('//*[contains(concat( " ", @class, " " ), concat( " ", "l-block", " " ))]//p[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]')), callback='parse_spd', follow=True)

    #def parse(self, response):
        #sel = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "l-block", " " ))]//p[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]')
        #item = Ref_Goodies()
        #item['link'] = sel.xpath('a/@href').extract()
        #url = sel.xpath('a/@href').extract()
        #item['cur_url'] = response.url
        #item['num'] = sel.xpath('a/text()').extract()
        #item['cur_url']
        #yield item
        ##yield scrapy.Request(test_url, callback=self.parse)


    #def parse_spd(self, response):
        #sel = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "l-block", " " ))]//p[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]')
        #item = Ref_Goodies()
        #item['link'] = sel.xpath('a/@href').extract()
        #url = sel.xpath('a/@href').extract()
        #item['cur_url'] = response.url
        #item['num'] = sel.xpath('a/text()').extract()
        #item['cur_url']
        #yield item


