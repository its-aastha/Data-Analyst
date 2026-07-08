#Day 2 : 

# DA / ML / AI
# LESS  <> LOGICAL
import requests

url = requests.get("https://data.covid19india.org/data.json")
covid_data = url.json()

#print(covid_data)
#Hudge data 

#Tasks have to print 
#Prine totl number of days as follow
#day 1  date
#day 2 date ....
for i in range (0,len(covid_data['cases_time_series'])):
    print('day :- ', i+1 , ', ' , 'date :- ', covid_data['cases_time_series'][i]['date'])


#how much main keys are there
print(covid_data.keys())
print("Total number of main keys:", len(covid_data.keys()))

# print statewise data using for loop


for i in range(1,len(covid_data['statewise'])):
    print("Total cases is in ", covid_data ['statewise'][i]['state'],'are :- ',
          covid_data['statewise'][i]['confirmed'])

print(" ")
#total cases in gujarat are 
for i in range (1,len(covid_data['statewise'])):
    if covid_data['statewise'][i]['state'] == 'Gujarat':
        print("Total number of cases in gujarat is :- ",covid_data['statewise'][i]['confirmed'])
        break
else :
    print('not found')
