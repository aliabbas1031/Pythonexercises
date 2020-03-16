
def removeduplicates(a):
    n = []
    for i in a:
        if i not in n:
            n.append(i)
    print(n)

a = [1,1,1,2,2,3,4,5,3,2,4,5,7]

removeduplicates(a)


b = list(set(a))
print(b)
