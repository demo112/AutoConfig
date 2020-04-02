import time

import scrapy
import subprocess
class DomzSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://localhost:9000/json/list?t=1585827611677"
    ]

    def parse(self, response):
        filename = "baidu.html"
        print(filename)
        with open(filename, "wb") as f:
            f.write(response.body)

if __name__ == '__main__':
    subprocess.check_call("scrapy crawl dmoz", shell=True)
    print(time.time())