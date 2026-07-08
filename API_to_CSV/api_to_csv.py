#Day 2 
import requests
import pandas as pd
url = requests.get ('https://data.covid19india.org/data.json')
my_data = url.json()
new_data = pd.DataFrame(my_data['statewise'])

new_data.to_csv("Covid_csv_dynamic.csv")
