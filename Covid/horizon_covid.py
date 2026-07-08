#Day 3 task : horizontally data repsent 

from matplotlib import pyplot as plt
import pandas as pd

data = pd.read_csv('Covid_csv_dynamic.csv')

data['confirmed'] = pd.to_numeric(data['confirmed'])
plt.figure(figsize=(5,5)) 

plt.barh(data['state'],data['confirmed'])
plt.xlabel('STATE')
plt.ylabel('DAILY CASES')
plt.title('TOTAL NUMBER OF CASES')
plt.show()
