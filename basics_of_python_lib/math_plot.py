#Day 3 :-
from matplotlib import pyplot as plt
cites = ['RAJKOT','AHMEDABAD','SURAT']
cases = [150,20,30]

plt.bar(cites,cases)
plt.xlabel('GUJARAT CITIES')
plt.ylabel('COVID CASES')
plt.title('GUJARAT STATE CASES')
plt.show()

