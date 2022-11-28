import scrapy

class AirqualityontarioSpider(scrapy.Spider):
    name = 'o3'
    allowed_domains = ['www.airqualityontario.com']
    # CO, PM2.5, NO2, 03, SO2
    start_urls = ["http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=122&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML"]
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=9&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML"]

    def parse(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_url,
                                 dont_filter=True)

    def parse_url(self, response):
        rows = response.xpath("//table/tbody/tr")
        # pollution = response.xpath("//h1/text()").get()
        for row in rows:
            date = row.xpath(".//td[2]/text()").get()
            h01 = row.xpath(".//td[3]/text()").get()
            h02 = row.xpath(".//td[4]/text()").get()
            h03 = row.xpath(".//td[5]/text()").get()
            h04 = row.xpath(".//td[6]/text()").get()
            h05 = row.xpath(".//td[7]/text()").get()
            h06 = row.xpath(".//td[8]/text()").get()
            h07 = row.xpath(".//td[9]/text()").get()
            h08 = row.xpath(".//td[10]/text()").get()
            h09 = row.xpath(".//td[11]/text()").get()
            h10 = row.xpath(".//td[12]/text()").get()
            h11 = row.xpath(".//td[13]/text()").get()
            h12 = row.xpath(".//td[14]/text()").get()
            h13 = row.xpath(".//td[15]/text()").get()
            h14 = row.xpath(".//td[16]/text()").get()
            h15 = row.xpath(".//td[17]/text()").get()
            h16 = row.xpath(".//td[18]/text()").get()
            h17 = row.xpath(".//td[19]/text()").get()
            h18 = row.xpath(".//td[20]/text()").get()
            h19 = row.xpath(".//td[21]/text()").get()
            h20 = row.xpath(".//td[22]/text()").get()
            h21 = row.xpath(".//td[23]/text()").get()
            h22 = row.xpath(".//td[24]/text()").get()
            h23 = row.xpath(".//td[25]/text()").get()
            h24 = row.xpath(".//td[26]/text()").get()
            yield {
                # "pollution": pollution,
                "date": date,
                "h01": h01,
                "h02": h02,
                "h03": h03,
                "h04": h04,
                "h05": h05,
                "h06": h06,
                "h07": h07,
                "h08": h08,
                "h09": h09,
                "h10": h10,
                "h11": h11,
                "h12": h12,
                "h13": h13,
                "h14": h14,
                "h15": h15,
                "h16": h16,
                "h17": h17,
                "h18": h18,
                "h19": h19,
                "h20": h20,
                "h21": h21,
                "h22": h22,
                "h23": h23,
                "h24": h24,
            }
       
