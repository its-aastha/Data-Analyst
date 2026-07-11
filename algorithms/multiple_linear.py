import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv('order.csv')
print(df)

reg = LinearRegression()
reg.fit(df[['users','orders','age']],df.amount)

new_data = pd.DataFrame({
    'users' : [2200],
    'orders' : [5000],
    'age' : [34]
})

prediction = reg.predict(new_data)
print(prediction)



