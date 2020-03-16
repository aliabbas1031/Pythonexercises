
def check():

    number = input("please enter a number: ")

    list = []

    try:
        number1 = int(number)
    except:
        print("wrong number")
        check()
    number2 = int(number)
    print(number2**.5)
    for i in range(1,int(number2**.5)):
        if number2%i == 0:
            list.append(i)
            list.append(number2//i)
    print(list)

check()

#ethod 2

def divisor(x):
     divisors =[]
     #print(int(x**.5))
     for i in range(1,int(x**.5)):
        if x % i == 0:
            divisors.append(i)
            divisors.append(x//i)
            #divisors.sort()
     print(divisors)
divisor(6457382)