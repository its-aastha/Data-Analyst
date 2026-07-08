#Day 3 :
import pandas as pd
import numpy as np

print("List data reprsent as the Data frame")
my_data = [15,23,56]
print(type(my_data))

#Convert mydata into dataframe

pd_data = pd.DataFrame(my_data)
print(pd_data)


print("Tuple Data reprsent in the data frame")
new_data = (15,25,40)
tup_data = pd.DataFrame(new_data)
print(tup_data)


one = ([10,20],[30,40],[50,60])
pone =  pd.DataFrame(one)
print()
print(pone)

imdata = { 
    'a': [10,20],
    'b': [30,40],
    'c' :[50,60]
}
pd_imdata = pd.DataFrame(imdata)
print(pd_imdata)

game = pd.DataFrame([
    ['ROHIT', 'BATSMAN', 50],
    ['KOHLI', 'BATSMAN', 75],
    ['BUMRAH', 'BOWLOER', 5]
], columns=['NAME', 'TYPE', 'SCORE'])
print()
print("CIRCKETER DATA")
print(game)

emp_data = np.array ([[8000,10000,2000],[15000,18000,25000]])
pd_emp_data = pd.DataFrame(emp_data,columns=[2024,2025,2026],index=['RAMESH','MAHESH'])
print()
print("EMPLOYEE DATA")
print(pd_emp_data)

#Adding new column 
pd_emp_data ['TOTAL'] = 12* (pd_emp_data[2024]+pd_emp_data[2025]+pd_emp_data[2026])
print()
print("UPDATED DATA WITH NEW COLUMN")
print(pd_emp_data)

#30% increase 
#Remaning 
pd_emp_data [2027] = pd_emp_data[2026] * 1.30
print()
print('30% INCRESED')
print(pd_emp_data) 
