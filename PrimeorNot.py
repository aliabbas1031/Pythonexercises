def isprime(num):

    divisors =list(range(2,num))
    a = []
    for i in divisors:
        if num%i == 0:
            a.append(i)
    if len(a) == 0:
        print("Given number is prime")
    else:
        print("Given number is not prime and divisors are "+ str(a))


while True:
    num = int(input("please enter a number to check if it is prime: "))
    if num > 1:
        isprime(num)
    else:
        print("number should be greater than 1")
