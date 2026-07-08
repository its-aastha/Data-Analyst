#Day 3 : 
import pandas as pd
import numpy as np 
file_data  = pd.read_csv('Covid_csv_dynamic.csv')
print(file_data)
print(type(file_data))

print(np.max(file_data['deltaconfirmed']))
