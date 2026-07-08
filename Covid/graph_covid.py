#Day 3 task
from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('Covid_csv_dynamic.csv')
data['confirmed'] = pd.to_numeric(data['confirmed'])
data['deltaconfirmed'] = pd.to_numeric(data['deltaconfirmed'])

plt.scatter(data['confirmed'],data['deltaconfirmed'])
plt.xlabel('CASES')
plt.ylabel('DAILY CASES')
plt.title('TOTAL NUMBER OF CASES')
plt.show()
