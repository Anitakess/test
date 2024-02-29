from collections import Counter
c = Counter()
cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
for car in cars:
    c[car] +=1
#print(c['black'])
