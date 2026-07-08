#Day 4

import pandas as pd
import numpy as np

data = pd.read_csv('mydata.csv')
print(data)
print(data['KOHLI'])
print("DHONI AND COLUMN 4:- ",data['DHONI'][4])

print(np.max(data['KOHLI']))