#def listlessthannumber(a):
import time
targetnumber = int(input("please enter target number for list: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n =[]
for i in a:
    if i<=targetnumber:
        n.append(a.index(i))
print(n)

#output(for)-->item(in)-->list(if)-->filter

#one line method
print([aa for aa in a if aa < targetnumber])