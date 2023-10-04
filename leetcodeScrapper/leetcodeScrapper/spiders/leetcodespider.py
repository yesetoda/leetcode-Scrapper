import scrapy
from .post import add_record_if_not_exists

class LeetcodespiderSpider(scrapy.Spider):
    name = "leetcodespider"
    allowed_domains = ["leetcode.com"]
    username = input("enter the username oof the profile : ")
    start_urls = [f"https://leetcode.com/{username}/"]

    def parse(self, response):
        
        rank = "".join( response.css(".ttext-label-1::text").extract())
        total = "".join(response.css(".text-\[24px\]::text").extract())
        nickname = "".join( response.css(".break-all::text").extract())
        fullname = "".join( response.css(".lc-lg\:w-\[300px\] > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)::text").extract())
        hard = response.css("div.space-y-2:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)::text").extract()[0] + "".join(response.css('div.space-y-2:nth-child(3) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)::text').extract())
        medium = response.css("div.space-y-2:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)::text").extract()[0] + "".join(response.css('div.space-y-2:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)::text').extract())
        easy = response.css(".lc-xl\:max-w-\[228px\] > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)::text").extract()[0] + "".join(response.css('.lc-xl\:max-w-\[228px\] > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)::text').extract())
        languages = ",".join(response.css(".notranslate::text").extract())

        # Write the data to a text file
        with open('output.txt', 'a') as file:
            file.write(f"\nFull Name: {fullname}\n")
            file.write(f"Nickname: {nickname}\n")
            file.write(f"Rank: {rank}\n")
            file.write(f"Total: {total}\n")
            file.write(f"Easy: {easy}\n")
            file.write(f"Medium: {medium}\n")
            file.write(f"Hard: {hard}\n")
            file.write(f"Languages: {languages}\n")
        add_record_if_not_exists(fullname, nickname, rank, easy, medium, hard, languages,total)
        