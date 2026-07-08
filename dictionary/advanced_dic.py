#Day 2 :
mydict = {
    'a' : 'one',
    'b' : 'two',
    'c' : 'three'
}
#insert opration
mydict['d'] = 'four'
print(mydict)

#update opration
mydict.update ({'b': 'new two'})
print(mydict)

#delete opration
mydict.pop('c')
print(mydict)



#Search opration
data = {
    'gujarat' : 'ahmedabad',
    'maharastra' : 'mumbai',
    'rajasthan ': 'jaipur'
}

for i in data:
    print(i)

find_key = input("Enter which key you have to find :-  ")

for i in data:
    if i == find_key:
        print("key found ")
        break
        
else:
    print("key not found")


#Searching value 
uservalue = input("Enter value you want to search:- ")

for i in data.values():
    if i == uservalue:
        print("value found")
        break
else :
    print("Vlaue not found ")
