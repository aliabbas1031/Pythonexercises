a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b =[]

for i in a:
    if i%2==0:
        b.append(i)
print(b)

print([b for b in a if b%2 == 0])
        
