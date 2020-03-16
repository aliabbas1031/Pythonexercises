number = int(input("Please enter a number"))
check = int(input("please enter number to divide"))

#method 1
i = number%2

if i > 0:
    print("number is odd")
else:
    print("number is even")

#method 2

if(number%check==0):
    print("first number is divisible by second number")
else:
    print("first number is not divisible by second number")

if(number%4 == 0):
    print("given number is multiple of 4")
elif(number%2 == 0):
    print("number is even")
else:
    print("number is odd")





