def sumofmultiplesof3and5(a):
    i=0
    for a in range(1,a+1):
            if a%3 == 0 or a%5==0:
                i = a+i
    return i
            
print(sumofmultiplesof3and5(10))
