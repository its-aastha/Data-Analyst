#day 6 
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('price.csv')

X = data[['area']] #Independent variable
Y = data['price'] #dependent variable

#create and Traing model 
model = LinearRegression()
model.fit(X,Y) #Parameters of the linear regression

predict = model.predict(X) #Prediction of model

print('slop :- ', model.coef_[0]) #It store the slop

new_area = pd.DataFrame([[200]],columns = ['area'])
price = model.predict(new_area)
print('predicted price:-',price[0])
plt.scatter(X,Y,label = 'actual data')
plt.plot(X, predict, label = "regression line")
plt.title('Linear regression')
plt.xlabel('area')
plt.ylabel('price')
plt.legend()
plt.show()