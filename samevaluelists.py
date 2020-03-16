import random

a = range(1,random.randint(1,10))
b = range(4,random.randint(1,20))

newlist = []

for i in a and b:
    if i in a and b:
        newlist.append(i)
print(newlist)
print(list(set(a) & set(b)))