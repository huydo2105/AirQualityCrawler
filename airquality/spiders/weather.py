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
    name = 'weather_ottawa'
    allowed_domains = ['www.wunderground.com']
    # CO, PM2.5, NO2, 03, SO2
    base_url ="https://www.wunderground.com/history/daily/ca/ottawa/CYOW/date/2021-"
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
            start_urls.append(base_url + str(i) + "-" + str(j))
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
        #//table[@class="mat-table cdk-table mat-sort ng-star-inserted"]/tbody/tr/td[1]/lib-display-unit/span/span/text()
        text = response.xpath('//script[@id="app-root-state"]/text()').get()
        parsedJson = json.loads(unescapeHTML(text))
        api_key = parsedJson["process.env"]["SUN_PWS_HISTORY_API_KEY"]

        rows = response.xpath('//table[@class="mat-table cdk-table mat-sort ng-star-inserted"]/tbody/tr')
        # # pollution = response.xpath("//h1/lib-display-unit/span/span/text()").get()
        parts = response.request.url.split("-")
        month = parts[1]
        day = parts[2]
        if int(month)<10:
            month = '0'+month
        if int(day)<10:
            day = '0'+day
        query_date = "2021"+month+day
        table_url = "https://api.weather.com/v1/location/CYOW:9:CA/observations/historical.json?units=e&startDate="+ query_date + "&endDate=" + query_date + "&apiKey=" + api_key


        # f = open("../csv/request_url.txt", "a")
        # f.write(response.request.url+"\n")
        # f.close()
        # f = open("../csv/demofile3.txt", "a")
        # f.write(table_url+"\n")
        # f.close()
        response = requests.get(table_url).json()
        hour_counter =0
        date_mark = dict()
        for res in response["observations"]:
            # print(res)
            timestamp = res["valid_time_gmt"]
            date = datetime.fromtimestamp(timestamp-12*3600) #convert VN timezone to Ottawa
            hour = date.hour 
            minute = date.minute
            month = date.month
            day = date.day
            date_key = str(hour)+str(day)+str(month)
            if date_key in date_mark:
                continue
            date_mark[date_key]=1
            hour_counter +=1
            print("--------------------------------------------")
            temp = res["temp"]
            humidity = res["rh"]
            pressure = res["pressure"]
            wind_speed = res["wspd"]
            precip = res["precip_hrly"]
            if precip is None:
                precip = 0.0
            # print("hour = {}:{}, temp = {}, humidity = {}, pressure = {}, wind speed = {}, precip = {}".format(hour, minute, temp, humidity, pressure, wind_speed, precip))
            yield {
                "hour": hour,
                "day": day,
                "month": month,
                # "time": time_dict[time],
                "temp": temp,
                "humidity": humidity,
                "wind": wind_speed,
                "pressure": pressure,
                "precip": precip
            }

        # for row in rows:
        #     time = row.xpath(".//td[1]/span/text()").get()
        #     time_dict = {
        #         "1:00 AM": 1,
        #         "2:00 AM": 2,
        #         "3:00 AM": 3,
        #         "4:00 AM": 4,
        #         "5:00 AM": 5,
        #         "6:00 AM": 6,
        #         "7:00 AM": 7,
        #         "8:00 AM": 8,
        #         "9:00 AM": 9,
        #         "10:00 AM": 10,
        #         "11:00 AM": 11,
        #         "12:00 AM": 12,
        #         "1:00 PM": 13,
        #         "2:00 PM": 14,
        #         "3:00 PM": 15,
        #         "4:00 PM": 16,
        #         "5:00 PM": 17,
        #         "6:00 PM": 18,
        #         "7:00 PM": 19,
        #         "8:00 PM": 20,
        #         "9:00 PM": 21,
        #         "10:00 PM": 22,
        #         "11:00 PM": 23,
        #         "12:00 PM": 24,
        #     }
        #     # if time not in time_dict:
        #     #     continue #todo
            
        #     date = response.request.url
        #     temp = row.xpath(".//td[2]/lib-display-unit/span/span/text()").get()
        #     print(temp)
        #     humidity = row.xpath(".//td[4]/lib-display-unit/span/span/text()").get()
        #     # h03 = row.xpath(".//td[5]/lib-display-unit/span/span/text()").get()
        #     wind = row.xpath(".//td[6]/lib-display-unit/span/span/text()").get()
        #     # h05 = row.xpath(".//td[7]/lib-display-unit/span/span/text()").get()
        #     pressure = row.xpath(".//td[8]/lib-display-unit/span/span/text()").get()
        #     precip = row.xpath(".//td[9]/lib-display-unit/span/span/text()").get()
        #     yield {
        #         # "pollution": pollution,
        #         "date": date,
        #         # "time": time_dict[time],
        #         "temp": temp,
        #         "humidity": humidity,
        #         "wind": wind,
        #         "pressure": pressure,
        #         "precip": precip
        #     }
       
