from html import unescape
import html,requests
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
url="{&q;process.env&q;:{&q;WU_LEGACY_API_HOST&q;:&q;https://api-ak.wunderground.com/api&q;,&q;DSX_API_HOST&q;:&q;https://dsx.weather.com&q;,&q;UPS_API_HOST&q;:&q;https://profile.wunderground.com&q;,&q;SUN_API_HOST&q;:&q;https://api.weather.com&q;,&q;SUN_DEVICE_API_HOST&q;:&q;https://station-management.wunderground.com&q;,&q;SUN_PWS_HISTORY_API_HOST&q;:&q;https://api.weather.com/v2/pws/history&q;,&q;SUN_PWS_IDENTITY_API_HOST&q;:&q;https://api.weather.com&q;,&q;MEMBER_KEY_GEN_API_HOST&q;:&q;https://www.wunderground.com/key-gen&q;,&q;WX_API_HOST&q;:&q;https://weather.com/api&q;,&q;WU_LEGACY_API_KEY&q;:&q;d8585d80376a429e&q;,&q;DSX_API_KEY&q;:&q;7bb1c920-7027-4289-9c96-ae5e263980bc&q;,&q;UPS_API_KEY&q;:&q;3254cfcb-90e3-4af5-819f-d79ea7e2382f&q;,&q;SUN_API_KEY&q;:&q;e1f10a1e78da46f5b10a1e78da96f525&q;,&q;SUN_DEVICE_API_KEY&q;:&q;&q;,&q;SUN_PWS_HISTORY_API_KEY&q;:&q;e1f10a1e78da46f5b10a1e78da96f525&q;,&q;SUN_PWS_IDENTITY_API_KEY&q;:&q;e1f10a1e78da46f5b10a1e78da96f525&q;,&q;WX_API_KEY&q;:&q;5c241d89f91274015a577e3e17d43370&q;,&q;DSR_SERVICE_HOST&q;:&q;https://www.wunderground.com/&q;,&q;NETATMO_CLIENT_ID&q;:&q;5d41ba256df87f001255caed&q;,&q;NETATMO_API_HOST&q;:&q;https://api.netatmo.com&q;,&q;NETATMO_REDIRECT_URL&q;:&q;https://www.wunderground.com/member/devices/link&q;,&q;PRIVACY_SETTINGS_HOST&q;:&q;https://www.wunderground.com&q;,&q;STATIC_HOST&q;:&q;www.wunderground.com&q;,&q;BASE_HOSTNAME&q;:&q;https://www.wunderground.com&q;,&q;DPR_SDK_HOST&q;:&q;https://www.wunderground.com/&q;,&q;DSR_FORM_HOST&q;:&q;https://weather.com&q;,&q;DATA_DEFINITIONS_HOST&q;:&q;https://www.wunderground.com&q;,&q;WEBCAKES_ENV&q;:&q;PROD&q;,&q;METRICS_API_AMPLITUDE_KEY&q;:&q;65e1857125d8c35761d19ddb9c32f145&q;},&q;wu-next-state-key&q;:{&q;c75b10d26a5ac7196178ad5be3553104&q;:{&q;value&q;:{&q;location&q;:{&q;latitude&q;:45.32,&q;longitude&q;:-75.67,&q;city&q;:&q;Ottawa&q;,&q;locale&q;:{&q;locale1&q;:null,&q;locale2&q;:&q;Ottawa&q;,&q;locale3&q;:null,&q;locale4&q;:&q;Hunt Club - Ottawa Airport&q;},&q;neighborhood&q;:&q;Hunt Club - Ottawa Airport&q;,&q;adminDistrict&q;:&q;Ontario&q;,&q;adminDistrictCode&q;:null,&q;postalCode&q;:&q;K1V 9B4&q;,&q;postalKey&q;:&q;K1V:CA&q;,&q;country&q;:&q;Canada&q;,&q;countryCode&q;:&q;CA&q;,&q;ianaTimeZone&q;:&q;America/Toronto&q;,&q;displayName&q;:&q;Ottawa&q;,&q;dstEnd&q;:&q;2022-11-06T01:00:00-0500&q;,&q;dstStart&q;:&q;2023-03-12T03:00:00-0400&q;,&q;dmaCd&q;:null,&q;placeId&q;:&q;7aac6077eae85b6451f7bdf98dc1c838f1e17db33accabf79dd774c0426a2b7c&q;,&q;disputedArea&q;:false,&q;disputedCountries&q;:null,&q;disputedCountryCodes&q;:null,&q;disputedCustomers&q;:null,&q;disputedShowCountry&q;:[false],&q;canonicalCityId&q;:&q;bd8262010e6e424d45c878890271a2cec79560cd9c75a3d8fdefaa459f973a2e&q;,&q;countyId&q;:null,&q;locId&q;:&q;CAON0010:1:CA&q;,&q;locationCategory&q;:null,&q;pollenId&q;:&q;BTV&q;,&q;pwsId&q;:&q;IONTARIO265&q;,&q;regionalSatellite&q;:&q;ne&q;,&q;tideId&q;:null,&q;type&q;:&q;neighborhood&q;,&q;zoneId&q;:&q;045400&q;,&q;airportName&q;:&q;Ottawa Macdonald-Cartier Intl Airport&q;,&q;icaoCode&q;:&q;CYOW&q;}},&q;expiresAt&q;:&q;2022-11-30T19:12:18.479Z&q;,&q;url&q;:&q;https://api.weather.com/v3/location/point?apiKey=e1f10a1e78da46f5b10a1e78da96f525&a;language=en-US&a;icaoCode=CYOW&a;format=json&q;},&q;3f96714e5931a4e157c3b69277016e99&q;:{&q;value&q;:{&q;location&q;:{&q;stationName&q;:[&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;,&q;Ottawa&q;],&q;stationId&q;:[&q;IONTARIO265&q;,&q;IOTTAW235&q;,&q;IONTARIO579&q;,&q;IOTTAW193&q;,&q;IOTTAWA98&q;,&q;IONTARIO1210&q;,&q;IOTTAW145&q;,&q;IOTTAW205&q;,&q;IOTTAW25&q;,&q;IONTARIO591&q;],&q;qcStatus&q;:[0,1,1,0,1,-1,1,1,1,1],&q;updateTimeUtc&q;:[1655082092,1669580280,1650561405,1669631174,1669558800,1595400360,1669559511,1669631015,1669583700,1565113834],&q;partnerId&q;:[&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;,&q;wu&q;],&q;latitude&q;:[45.32246,45.322,45.29837,45.318,45.28045,45.28991,45.365,45.273,45.358,45.35758],&q;longitude&q;:[-75.68967,-75.69,-75.69964,-75.719,-75.69585,-75.71541,-75.671,-75.691,-75.716,-75.71684],&q;distanceKm&q;:[1.56,1.58,3.34,3.84,4.84,4.88,5,5.48,5.55,5.56],&q;distanceMi&q;:[0.97,0.98,2.08,2.38,3.01,3.03,3.11,3.4,3.45,3.45]}},&q;expiresAt&q;:&q;2022-12-01T00:27:59.506Z&q;,&q;url&q;:&q;https://api.weather.com/v3/location/near?apiKey=e1f10a1e78da46f5b10a1e78da96f525&a;geocode=45.32%2C-75.67&a;product=pws&a;format=json&q;},&q;a8dbad82c164ce115cc94e53650e6aa8&q;:{&q;value&q;:{&q;observations&q;:[{&q;stationID&q;:&q;IOTTAW235&q;,&q;obsTimeUtc&q;:&q;2022-11-30T16:41:48Z&q;,&q;obsTimeLocal&q;:&q;2022-11-30 11:41:48&q;,&q;neighborhood&q;:&q;Hunt Club Woods - Quintarra - Revelstoke&q;,&q;softwareType&q;:null,&q;country&q;:&q;CA&q;,&q;solarRadiation&q;:25,&q;lon&q;:-75.69,&q;realtimeFrequency&q;:null,&q;epoch&q;:1669826508,&q;lat&q;:45.322,&q;uv&q;:0.1,&q;winddir&q;:88,&q;humidity&q;:91,&q;qcStatus&q;:1,&q;imperial&q;:{&q;temp&q;:36,&q;heatIndex&q;:36,&q;dewpt&q;:33,&q;windChill&q;:31,&q;windSpeed&q;:5,&q;windGust&q;:8,&q;pressure&q;:29.51,&q;precipRate&q;:0.2,&q;precipTotal&q;:0.36,&q;elev&q;:348}}]},&q;expiresAt&q;:&q;2022-11-30T16:42:29.608Z&q;,&q;url&q;:&q;https://api.weather.com/v2/pws/observations/current?apiKey=e1f10a1e78da46f5b10a1e78da96f525&a;units=e&a;stationId=IOTTAW235&a;format=json&q;},&q;85c860846ba4de0abebbd911ce822c2b&q;:{&q;value&q;:{&q;cloudCeiling&q;:1600,&q;cloudCoverPhrase&q;:&q;Cloudy&q;,&q;dayOfWeek&q;:&q;Wednesday&q;,&q;dayOrNight&q;:&q;D&q;,&q;expirationTimeUtc&q;:1669827103,&q;iconCode&q;:12,&q;iconCodeExtend&q;:1200,&q;obsQualifierCode&q;:&q;OQ1189&q;,&q;obsQualifierSeverity&q;:2,&q;precip1Hour&q;:0.15,&q;precip6Hour&q;:0.47,&q;precip24Hour&q;:0.47,&q;pressureAltimeter&q;:29.53,&q;pressureChange&q;:-0.2,&q;pressureMeanSeaLevel&q;:999.2,&q;pressureTendencyCode&q;:4,&q;pressureTendencyTrend&q;:&q;Falling Rapidly&q;,&q;relativeHumidity&q;:100,&q;snow1Hour&q;:0,&q;snow6Hour&q;:0,&q;snow24Hour&q;:0,&q;sunriseTimeLocal&q;:&q;2022-11-30T07:20:25-0500&q;,&q;sunriseTimeUtc&q;:1669810825,&q;sunsetTimeLocal&q;:&q;2022-11-30T16:22:05-0500&q;,&q;sunsetTimeUtc&q;:1669843325,&q;temperature&q;:36,&q;temperatureChange24Hour&q;:4,&q;temperatureDewPoint&q;:36,&q;temperatureFeelsLike&q;:29,&q;temperatureHeatIndex&q;:36,&q;temperatureMax24Hour&q;:36,&q;temperatureMaxSince7Am&q;:36,&q;temperatureMin24Hour&q;:29,&q;temperatureWindChill&q;:29,&q;uvDescription&q;:&q;Low&q;,&q;uvIndex&q;:1,&q;validTimeLocal&q;:&q;2022-11-30T11:41:43-0500&q;,&q;validTimeUtc&q;:1669826503,&q;visibility&q;:3,&q;windDirection&q;:90,&q;windDirectionCardinal&q;:&q;E&q;,&q;windGust&q;:null,&q;windSpeed&q;:10,&q;wxPhraseLong&q;:&q;Rain&q;,&q;wxPhraseMedium&q;:&q;Rain&q;,&q;wxPhraseShort&q;:&q;Rain&q;},&q;expiresAt&q;:&q;2022-11-30T16:51:42.706Z&q;,&q;url&q;:&q;https://api.weather.com/v3/wx/observations/current?apiKey=e1f10a1e78da46f5b10a1e78da96f525&a;language=en-US&a;units=e&a;format=json&a;icaoCode=CYOW&q;},&q;d192862c1407ae627637028de5949ea7&q;:{&q;value&q;:{&q;cloudCeiling&q;:1600,&q;cloudCoverPhrase&q;:&q;Cloudy&q;,&q;dayOfWeek&q;:&q;Wednesday&q;,&q;dayOrNight&q;:&q;D&q;,&q;expirationTimeUtc&q;:1669827103,&q;iconCode&q;:12,&q;iconCodeExtend&q;:1200,&q;obsQualifierCode&q;:&q;OQ1189&q;,&q;obsQualifierSeverity&q;:2,&q;precip1Hour&q;:0.15,&q;precip6Hour&q;:0.47,&q;precip24Hour&q;:0.47,&q;pressureAltimeter&q;:29.53,&q;pressureChange&q;:-0.2,&q;pressureMeanSeaLevel&q;:999.2,&q;pressureTendencyCode&q;:4,&q;pressureTendencyTrend&q;:&q;Falling Rapidly&q;,&q;relativeHumidity&q;:100,&q;snow1Hour&q;:0,&q;snow6Hour&q;:0,&q;snow24Hour&q;:0,&q;sunriseTimeLocal&q;:&q;2022-11-30T07:20:25-0500&q;,&q;sunriseTimeUtc&q;:1669810825,&q;sunsetTimeLocal&q;:&q;2022-11-30T16:22:05-0500&q;,&q;sunsetTimeUtc&q;:1669843325,&q;temperature&q;:36,&q;temperatureChange24Hour&q;:4,&q;temperatureDewPoint&q;:36,&q;temperatureFeelsLike&q;:29,&q;temperatureHeatIndex&q;:36,&q;temperatureMax24Hour&q;:36,&q;temperatureMaxSince7Am&q;:36,&q;temperatureMin24Hour&q;:29,&q;temperatureWindChill&q;:29,&q;uvDescription&q;:&q;Low&q;,&q;uvIndex&q;:1,&q;validTimeLocal&q;:&q;2022-11-30T11:41:43-0500&q;,&q;validTimeUtc&q;:1669826503,&q;visibility&q;:3,&q;windDirection&q;:90,&q;windDirectionCardinal&q;:&q;E&q;,&q;windGust&q;:null,&q;windSpeed&q;:10,&q;wxPhraseLong&q;:&q;Rain&q;,&q;wxPhraseMedium&q;:&q;Rain&q;,&q;wxPhraseShort&q;:&q;Rain&q;},&q;expiresAt&q;:&q;2022-11-30T16:50:45.067Z&q;,&q;url&q;:&q;https://api.weather.com/v3/wx/observations/current?apiKey=e1f10a1e78da46f5b10a1e78da96f525&a;geocode=45.32%2C-75.67&a;units=e&a;language=en-US&a;format=json&q;}}}"
# print(unescapeHTML(url))

url = "https://api.weather.com/v1/location/CYOW:9:CA/observations/historical.json?units=e&startDate=20210113&endDate=20210113&apiKey=e1f10a1e78da46f5b10a1e78da96f525"
response = requests.get(url).json()
for res in response["observations"]:
    # print(res)
    print("--------------------------------------------")
    temp = res["temp"]
    humidity = res["rh"]
    pressure = res["pressure"]
    wind_speed = res["wspd"]
    precip = res["precip_hrly"]
    if precip is None:
        precip = 0.0
    timestamp = res["valid_time_gmt"]
    date = datetime.fromtimestamp(timestamp-12*3600) #convert VN timezone to Ottawa
    hour = date.hour 
    minute = date.minute
    print("hour = {}:{}, temp = {}, humidity = {}, pressure = {}, wind speed = {}, precip = {}".format(hour, minute, temp, humidity, pressure, wind_speed, precip))

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
for i in range(1,2):
    for j in days[i]:
        start_urls.append(base_url + str(i) + "-" + str(j))
url = ""
for i in start_urls:
    print(i)
parts = start_urls[20].split("-")
month = parts[1]
day = parts[2]
if int(month)<10:
    month = '0'+month
if int(day)<10:
    day = '0'+day
query_date = "2021"+month+day
print(query_date)