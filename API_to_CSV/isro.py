#Day 1 : 
import requests

url = requests.get('https://isro.vercel.app/api/spacecrafts')
data = url.json()

print(data.keys())
print("Total number of spacecrafts:- " , len(data.keys()))

print(data['spacecrafts'][0]['name'])

print("Total number of spacecrafts:" , len(data["spacecrafts"]))

