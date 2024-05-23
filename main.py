import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use('seaborn')


temp = pd.read_csv("temp.csv", parse_dates=["datetime"],index_col='datetime' )


pd.to_datetime(temp.datetime[0])
# print(temp.info())

# downtiming series
temp.resample('d')
print(temp)









# env\Scripts\activate