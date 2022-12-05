import pandas as pd

data = pd.read_csv("../csv/weather.csv")
  
# sorting data frame by a column
data.sort_values(["month","day","hour"], axis=0,
                 ascending=[True, True, True], inplace=True)
  
data.to_csv("../csv/weather_sorted.csv", sep=',', index=False)
# display
print(data.head(100))
