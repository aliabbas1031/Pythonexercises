a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def intersect(a,b):
    new = []
    for i in a and b:
        if i in a and b:
            new.append(i)
    print(new)

intersect(a,b)

print(list(set(a) & set(b)))


result = [i for i in a if i in b]

print(result)