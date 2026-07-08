#Day 4 :- work
import pandas as pd
from matplotlib import pyplot as plt
import requests

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()

state = []
cases = []

for i in range(0,len(mydata['statewise'])):
    state.append(mydata['statewise'][i]['state'])
    cases.append(int(mydata['statewise'][i]['confirmed'])) #int bcz we only want the interger data not "3666"


plt.bar(state,cases)
plt.show()