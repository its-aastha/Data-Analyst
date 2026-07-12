import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

data = pd.read_csv('price.csv')

X = data[['area']]
Y = data['price']

# Linear --> Polynomial
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Train Model
model = LinearRegression()
model.fit(X_poly, Y)

# New data
new_data = pd.DataFrame({
    'area': [220]
})

# Convert new data into polynomial
new_data_poly = poly.transform(new_data)

# Prediction
prediction = model.predict(new_data_poly)
print("Predicted Price:", prediction[0])