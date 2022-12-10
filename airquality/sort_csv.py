import pandas as pd

data = pd.read_csv("../csv/weather_106_2.csv")
  
# sorting data frame by a column
data.sort_values(["month","day","minute","hour"], axis=0,
                 ascending=[True, True, True, True], inplace=True)
  
data.to_csv("../csv/weather_106_sorted.csv", sep=',', index=False)
# display
print(data.head(100))

#https://www.wunderground.com/weather/ca/ottawa/IOTTAW175