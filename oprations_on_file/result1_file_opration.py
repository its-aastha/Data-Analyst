#Day 4

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('RESULT1.csv')
print(data)
print("Number of rows and colums are:- ",data.shape) #used to identify the how much rows and columns are there
print("Number of rows are:- ",data.shape[0]) #Number of rows
print("Number of columns  are:- ",data.shape[1]) #Number of columns
print("Name of column names are :- ",data.columns) #Columns name are 

#Null values
print("Null values are :")
print(data.isnull().sum())

#2 columns
print(data[['BRANCH','NAME','TOTAL']])

#bar graph X= NAME Y = TOTAL
plt.bar(data['NAME'],data['TOTAL'])
plt.show()

plt.pie(data['TOTAL'],labels=data['NAME'],autopct = '%0.1f%%')

plt.show()