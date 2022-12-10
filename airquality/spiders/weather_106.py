import scrapy, json, requests
import html
from datetime import datetime
unescapedText = {
    '&a;': '&',
    '&q;': '"',
    '&s;': '\'',
    '&l;': '<',
    '&g;': '>',
}


def unescapeHTML(str):
    for key, value in unescapedText.items():
        str = str.replace(key, value)
    return html.unescape(str)

class WeatherOttawaSpider(scrapy.Spider):
    name = 'weather_ottawa106'
    allowed_domains = ['www.wunderground.com']
    # CO, PM2.5, NO2, 03, SO2
    base_url ="https://www.wunderground.com/dashboard/pws/IOTTAW106/table/2021-"
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
    for i in range(1,13):
        for j in days[i]:
            start_urls.append(base_url + str(i) + "-" + str(j)+"/2021-"+str(i) + "-" + str(j)+"/daily")
    url = ""
    for i in start_urls:
        print(i)
    
    def parse(self, response):
        url = response.url
        # f = open("../csv/parse_url.txt", "a")
        # f.write("------------------------------\n")
        # f.close()
        # f = open("../csv/parse_url.txt", "a")
        # f.write(url+"\n")
        # f.close()
        yield scrapy.Request(url, callback=self.parse_url,
                                dont_filter=True)

    def parse_url(self, response):
        # print(response.request.url)
        #response.xpath('//table[@class="history-table desktop-table"]/tbody/tr')[1].xpath(".//td")[1].xpath(".//lib-display-unit/span/span/text()").get()
        full_date = response.request.url.split("/")[-2]
        day = full_date.split("-")[2]
        month = full_date.split("-")[1]
        rows = response.xpath('//table[@class="history-table desktop-table"]/tbody/tr')
        for row in rows:
            timestamp = row.xpath(".//td")[0].xpath(".//strong/text()").get()
            parts = timestamp.split(":")
            hour = int(parts[0])
            inner_parts = parts[1].split(" ")
            minute = inner_parts[0]
            pmam = inner_parts[1]
            if pmam == "PM" and hour != 12:
                hour +=12
            if pmam =="AM" and hour == 12:
                hour =0
            td_list= row.xpath(".//td")
            temp = td_list[1].xpath(".//lib-display-unit/span/span/text()").get()
            humidity = td_list[3].xpath(".//lib-display-unit/span/span/text()").get()
            wind_speed = td_list[5].xpath(".//lib-display-unit/span/span/text()").get()
            pressure = td_list[7].xpath(".//lib-display-unit/span/span/text()").get()
            precip = td_list[9].xpath(".//lib-display-unit/span/span/text()").get()
            yield {
                "minute": minute,
                "hour": hour,
                "day": day,
                "month": month,
                "temp": temp,
                "humidity": humidity,
                "wind": wind_speed,
                "pressure": pressure,
                "precip": precip
            }



        