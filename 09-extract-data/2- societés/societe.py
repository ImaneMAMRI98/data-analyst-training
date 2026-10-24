import scrapy
from pathlib import Path
import re
import csv


class SocieteSpider(scrapy.Spider):
    name = "societe"
    allowed_domains = ["www.societe.com"]
    start_urls = ["https://www.societe.com/entreprises/isere-38"]


    def parse(self, response):
        spans = response.xpath('//li/a/span[text()="62" or text()="63"]')
        for span in spans:    

            url = span.xpath('../@href').get()
            if url:
                yield response.follow(url, callback=self.parse_category)

    def parse_category(self, response):
        liens_entreprises = response.xpath('//div[@class="ui-wrap"]/ul/li/a/@href').getall()
        for lien in liens_entreprises:
            yield response.follow(lien, callback=self.parse_entreprises)

    def parse_entreprises(self, response):
        liens = response.xpath('//div[@class="ui-wrap"]/ol/li/a/@href').getall()
        for lien in liens:
            yield response.follow(lien, callback=self.parse_entreprise)


    def parse_entreprise(self,response):

        nom = response.xpath('//h1/text()').get()
        siren = response.xpath('//html/body/main/section[2]/div/dl/div[1]/dd/text()').get().rstrip()
        adresse = response.xpath('//html/body/main/section[2]/div/dl/div[7]/dd//text()').get().rstrip()
        with open('dataa.csv' ,'a' ,newline='') as f:
            writer = csv.writer(f, delimiter='|')
            line = [nom , siren, adresse]
            writer.writerow(line)
        
        # yield {
        #     "nom": nom,
        #     "siren": siren,
        #     "adresse": adresse,
        # }

