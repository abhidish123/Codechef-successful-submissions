print("Hello World")

a = [1,2,3]
b = [4,5,6]
# c = [5,7,9]

c = []
for i in range(0,3):
    c.append(a[i]+b[i])

print(c)
c.reverse()
print(c)

to sort in descending order, where default sort is in ascending order
c.sort(reverse=True)
print(c)

print(c)
print(c[::-1])

l = [1,2,3,7,8,3,4,3,7,1]
print(l.count(3))

t = set(l)
t = {x for x in l}
t = list(t)
from asyncore import loop
from collections import defaultdict as dd
freq = dd(int)
for i in range(0,len(l)):
    freq[l[i]] += 1

print(t)
for i in range(0,len(t)):
    print("t[i] = ",t[i])
    print(freq[t[i]])

    if(freq[t[i]] == 1):
        print(*{t[i]}, "occured 1 time")
    elif(freq[t[i]] == 2):
        print(*{t[i]}, "occured 2 times")
    else:
        print(*{t[i]}, "occured 3 times")
    
3 types of loops
    for loop
    while loop
    do while loop

countries = {}
countries['India'] = 'New Delhi' 
countries['Russia'] = 'Moscow' 
countries['USA'] = 'Washington DC'

print(countries)
print(*countries)

print(*countries.keys())
print(*countries.values())
