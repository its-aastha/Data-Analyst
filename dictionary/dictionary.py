#Day 1 : 

#DATA INSIDE THE CURLY { } BRACKET
#DATA KEY(left) AND VALUE(right) PAIR
#TO ACCESS VALUE , KEY IS REQUIRED

data = {
    'ahmedabad': 200,
    'surat' : [300, 350, 1],
    'rajkot' : 500
}
print(type(data))
print(data['ahmedabad'])

#print 350
print(data['surat'][1])

data = {
    'ahmedabad' : [{'date' : '1 july 2026' , 'cases' : 50},
                   {'date' : '2 july 2026' , 'cases' : 60},
                   {'date' : '3 july 2026' , 'cases' : 70}],
    'surat' : [300, 350, 1],
    'rajkot' : 400
}
print(data['ahmedabad'][2]['date'])
print(data['ahmedabad'][1]['cases'])
