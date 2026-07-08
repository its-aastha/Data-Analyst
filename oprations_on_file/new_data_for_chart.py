import requests
import pandas as pd
from matplotlib import pyplot as plt 

url = requests.get('https://dummyjson.com/users')
data = url.json()
#print the key 
print(data.keys())

#Convert the api to the csv
new_data = pd.DataFrame(data['users'])

#new_data.to_csv("users_data.csv", index=False)

#Read csv file 
read = pd.read_csv('users_data.csv')

#scatter plot chart
plt.bar(new_data['height'],new_data['weight'])
plt.title("height vs weight")
plt.xlabel('Hight in cm')
plt.ylabel('weight in kg')
plt.show()
