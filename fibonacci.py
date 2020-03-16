def fib(target):
    a= [0,1]
    n1 = 0
    n2 = 1
    while True: #- use this for max series number
    #if i in range(0,n-2): use this for total number of fib numbers user wants to see
        n = n1+n2
        n1=n2
        n2=n
        if n<target:
            a.append(n)
        else:
            break
    print(a)

n = int(input("please enter total number of fib number you want to see: "))  
fib(n)