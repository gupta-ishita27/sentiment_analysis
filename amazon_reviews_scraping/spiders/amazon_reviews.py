import scrapy

class AmazonReviewsSpider(scrapy.Spider):
 
    # Spider name
    name = 'amazon_reviews'
 
    # Domain names to scrape
    allowed_domains = ['amazon.in']
 
    # Base URL for the MacBook air reviews
    myBaseUrl = "https://www.amazon.in/SKUDGEAR-Multi-Purpose-Reading-Foldable-Non-Slip/product-reviews/B0822999TS/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    start_urls=[]
 
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,121):
        start_urls.append(myBaseUrl+str(i))
 
    # Defining a Scrapy parser
    def parse(self, response):
          #  data = response.css('#cm_cr-review_list')
 
            # Collecting product star ratings
          #  star_rating = data.css('.review-rating')

        stars=response.xpath('//span[@class="a-icon-alt"]/text()').extract()

        comment=response.xpath('//span[@class="a-size-base review-text review-text-content"]/span/text()').extract()

 
        count = 0

        for item in zip(stars, comment):

       # create a dictionary to store the scraped info

            scraped_data = {

           'Stars': item[0],

           'Comment': item[1].replace("\n", ""),

            }

       # yield or give the scraped info to scrapy
            yield scraped_data


        next_page = response.css('.a-last a ::attr(href)').extract_first()

        if next_page:

            yield scrapy.Request(

                response.urljoin(next_page),

                callback=self.parse

            )
            











            