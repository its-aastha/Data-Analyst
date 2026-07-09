#day 7 
#coding 3 line 
import matplotlib.pyplot as plt  #data 
import pandas as pd
from sklearn import linear_model

data = pd.read_csv('price.csv')

plt.scatter(data.area,data.price)
plt.show()



