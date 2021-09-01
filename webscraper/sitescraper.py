import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from urllib.request import urlopen

logging.getLogger('scrapy').propagate = False
_log = logging.getLogger("sitescraper")

# return a list of urls so that we pass into the filedownloader function
class MuseScoreSpider(scrapy.Spider):
    name = 'musescorespider'

    # find a way to build the list with all pages on musescore
    def start_requests(self):
        urls = [
            'https://musescore.com/sheetmusic/public-domain?page=1'
            # 'https://musescore.com/sheetmusic/public-domain?page=2',
            # 'https://musescore.com/sheetmusic/public-domain?page=3'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parse)

    def parse(self, response):
        url = response.url
        
        print('Parsing url: ' + url)
        page = urlopen(url)
        # need to specify a byte amount in order to get everything.  find a way to get the size of bytes without ending the read stream
        html_bytes = page.read(30000)
        
        print("print url page")
        html = html_bytes.decode("utf-8")
        
        # content is in here but scrapy isn't getting it
        # <div class="js-page react-container">
        #     </div>
        print(html)
        divs = html.find("<div")

        print("finished printing url")
        
        # article_section = html.find("<article")
        # print("test article")
        # print(article_section)




#run the spider 
process = CrawlerProcess({
    'USER_AGENT': 'Chrome/92.0.4515.107'
})
process.crawl(MuseScoreSpider)
process.start()
