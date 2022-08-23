import csv
from email.errors import MultipartInvariantViolationDefect
from itertools import count
from operator import index
from typing import Counter

from matplotlib import pyplot as plt

data = open('kpop_data.csv','r') #read (juste en lecture)

dataCsv = csv.reader(data)

femaleCounter = 0
maleCounter = 0
transCounter = 0


for row in dataCsv:
    for element in row:
        if(element=="Female"):
            femaleCounter = femaleCounter + 1
        if(element=="Transgender"):
            transCounter = transCounter + 1
        if(element=="Male"):
            maleCounter = maleCounter + 1
    
    

print(f"Female: {femaleCounter}, Male: {maleCounter}, Trans: {transCounter}")
# time = range(0, 25)
# hours = []
# firstTime = 0
# indexHours = []
# number = []
# age = {}
# indexAge = []

# for row in dataCsv:
#     indexHours.append(row[0])
#     indexAge.append(row[1])

# indexHours.pop(0)
# indexAge.pop(0)

# hoursCounter = Counter(indexHours)
# print(hoursCounter)
 
# sort_keys = hoursCounter.items()
# new_items = sorted(sort_keys)
# print(new_items)

# ageCounter = Counter(indexAge)


# # x = newIndexHours.keys()
# # y = newIndexHours.values()
# # print(x);

# # plt.plot(x,y)
# # plt.show()

        

# #print(f"hellow Hours : {newIndexHours}")

        
# data.close()