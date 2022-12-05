import scrapy
from datetime import datetime
class AirqualityontarioSpider(scrapy.Spider):
    name = 'pm2_5'
    allowed_domains = ['www.airqualityontario.com']
    # CO, PM2.5, NO2, 03, SO2
    start_urls = ["http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=124&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML"]
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=36&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML",
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=122&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML",
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=9&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML"]

    def parse(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_url,
                                 dont_filter=True)

    def parse_url(self, response):
        rows = response.xpath("//table/tbody/tr")
        # pollution = response.xpath("//h1/text()").get()
        for row in rows:
            timestamp = row.xpath(".//td[2]/text()").get()
            date = datetime.strptime(timestamp, "%Y-%m-%d") #convert VN timezone to Ottawa
            month = date.month
            day = date.day
            td_list = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
            for i in td_list:
                pm2_5 = row.xpath(".//td[" + str(i) + "]/text()").get()
                hour = response.xpath("//table/thead/tr/th[" + str(i) + "]/text()").get()
                if int(hour[1:]) < 10:
                    hour = int(hour[-1]) - 1
                else:
                    hour = int(hour[1:]) - 1 
                yield {
                    "hour": hour,
                    "day": day,
                    "month": month,
                    "pm2.5": pm2_5,
                }
       
