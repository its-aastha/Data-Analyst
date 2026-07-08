#Day 4 :- work
import pandas as pd
import requests
from matplotlib import pyplot as plt

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()

dates = []
cases = []
for i in range(0,len(mydata['cases_time_series'])):
    dates.append(mydata['cases_time_series'][i]['date'])
    cases.append(int(mydata['cases_time_series'][i]['dailyconfirmed'])) #int so then it repsent the integer data else it print the string data as well as 

plt.plot(dates,cases)
plt.show()