import scrapy

class QuoteSpider(scrapy.Spider):
    name= 'quotes'
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75.html']

    def parse(self, response):
        websites = response.xpath('//div[@class="p_box_wrapper"]/div')
        for website in websites:
            true_price = website.xpath('.//div[@class="p_box_price cf"]/span[1]/text()').extract()
            if true_price:
                title1 = website.xpath('.//a[@class="p_box_title"]/text()').extract()
                price1 = website.xpath('.//div[@class="p_box_price cf"]/span[1]/text()').extract()
                yield {
                    'title': title1[1],
                    'price': price1
                }

            else:
                title1 = website.xpath('.//a[@class="p_box_title"]/text()').extract()
                price1 = website.xpath('.//div[@class="p_box_price cf"]/text()').extract()
                yield {
                    'title': title1[1],
                    'price': price1
                }
        next_page = response.xpath('//a[@class="nextPage"]/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)