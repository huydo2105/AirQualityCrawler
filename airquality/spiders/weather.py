import scrapy

class WeatherOttawaSpider(scrapy.Spider):
    name = 'weather_ottawa'
    allowed_domains = ['www.wunderground.com']
    # CO, PM2.5, NO2, 03, SO2
    base_url ="https://www.wunderground.com/history/daily/ca/ottawa/CYOW/date/2021-"
    # start_urls = ['http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=46&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML',]
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=124&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML",
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=36&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML",
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=122&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML",
                #   "http://www.airqualityontario.com/history/searchResults.php?page=_search&s_categoryId=Academic&s_stationId=51002,51001&s_pollutantId=9&s_startDate=01/01/2021&s_endDate=12/31/2021&s_reportType=HTML"]
    days = {
        1: [ i for i in range (1,32)],
        2: [i for i in range (1,29)],
        3: [i for i in range (1,32)],
        4: [i for i in range (1,31)],
        5: [i for i in range (1,32)],
        6: [i for i in range (1,31)],
        7: [i for i in range (1,32)],
        8: [i for i in range (1,32)],
        9: [i for i in range (1,31)],
        10: [i for i in range (1,32)],
        11: [i for i in range (1,31)],
        12: [i for i in range (1,32)],
    }

    start_urls =[]
    for i in range(1,2):
        for j in days[i]:
            start_urls.append(base_url + str(i) + "-" + str(j))
    url = ""
    # for i in start_urls:
    #     print(i)
    def parse(self, response):
        for url in self.start_urls:
            self.url= url
            yield scrapy.Request(url, callback=self.parse_url,
                                 dont_filter=True)

    def parse_url(self, response):
        # print(response.request.url)
        #//table[@class="mat-table cdk-table mat-sort ng-star-inserted"]/tbody/tr/td[1]/lib-display-unit/span/span/text()
        rows = response.xpath('//table[@class="mat-table cdk-table mat-sort ng-star-inserted"]/tbody/tr')
        # # pollution = response.xpath("//h1/lib-display-unit/span/span/text()").get()
        for row in rows:
            time = row.xpath(".//td[1]/span/text()").get()
            time_dict = {
                "1:00 AM": 1,
                "2:00 AM": 2,
                "3:00 AM": 3,
                "4:00 AM": 4,
                "5:00 AM": 5,
                "6:00 AM": 6,
                "7:00 AM": 7,
                "8:00 AM": 8,
                "9:00 AM": 9,
                "10:00 AM": 10,
                "11:00 AM": 11,
                "12:00 AM": 12,
                "1:00 PM": 13,
                "2:00 PM": 14,
                "3:00 PM": 15,
                "4:00 PM": 16,
                "5:00 PM": 17,
                "6:00 PM": 18,
                "7:00 PM": 19,
                "8:00 PM": 20,
                "9:00 PM": 21,
                "10:00 PM": 22,
                "11:00 PM": 23,
                "12:00 PM": 24,
            }
            # if time not in time_dict:
            #     continue #todo
            
            date = response.request.url
            temp = row.xpath(".//td[2]/lib-display-unit/span/span/text()").get()
            print(temp)
            humidity = row.xpath(".//td[4]/lib-display-unit/span/span/text()").get()
            # h03 = row.xpath(".//td[5]/lib-display-unit/span/span/text()").get()
            wind = row.xpath(".//td[6]/lib-display-unit/span/span/text()").get()
            # h05 = row.xpath(".//td[7]/lib-display-unit/span/span/text()").get()
            pressure = row.xpath(".//td[8]/lib-display-unit/span/span/text()").get()
            precip = row.xpath(".//td[9]/lib-display-unit/span/span/text()").get()
            yield {
                # "pollution": pollution,
                "date": date,
                # "time": time_dict[time],
                "temp": temp,
                "humidity": humidity,
                "wind": wind,
                "pressure": pressure,
                "precip": precip
            }
       
