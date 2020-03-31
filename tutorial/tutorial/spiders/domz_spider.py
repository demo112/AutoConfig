import scrapy

class DomzSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://www.baidu.com/"
    ]

    def parse(self, response):
        filename = response.url.split(".")[-2]
        print(filename)
        with open(filename, "wb") as f:
            f.write(response.body)

