import scrapy
from pathlib import Path
from bookstore.items import BookstoreItem
import csv
import re


class BookNamesSpider(scrapy.Spider):
    name = "book_names"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.compteur = 0

    def parse(self, response):
        match = re.search(r'page-(\d+)\.html', response.url)
        page_num = int(match.group(1)) if match else 1
        # using xpath seloctors
        with open('dataaa.csv' ,'a' ,newline='') as f:
            writer = csv.writer(f, delimiter='|')
            head = "rank|page_number|book_title|price|ratings"
            for article in response.xpath('//article[@class="product_pod"]'):
                self.compteur += 1 
                title = article.xpath('.//h3/a/@title').get()
                price = article.xpath('.//p[@class="price_color"]/text()').get()
                rating_class = article.xpath('.//p[contains(@class,"star-rating")]/@class').get()
                rating_text = rating_class.split()[-1]
                mots_to_num = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
                rating = mots_to_num.get(rating_text, 0)

                line = [self.compteur, page_num, title, price, rating]
                writer.writerow(line)

        # using css selectors
        # with open('dataaa.csv' ,'w' ,newline='') as f:
        #     for article in response.css('article.product_pod'):
        #         line = []
        #         title = article.css("h3 > a::attr(title)").extract_first()
        #         price = article.css(".price_color::text").extract_first()
        #         line.append(title)
        #         line.append(price)
        #         writer = csv.writer(f, delimiter='|')
        #         writer.writerow(line)
        # find next pages
        for url in response.xpath('//li[@class="next"]/a/@href').getall():
            yield response.follow(url,callback=self.parse)
 
