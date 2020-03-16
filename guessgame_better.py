import random

computer = random.randint(1,9)

count = 0
guess = 0

while guess != computer and guess!=exit:
    guess = int(input("please enter your number: "))
    if guess<computer:
        print("your number was too low")
    elif guess>computer:
        print("your number was too high")
    else:
        count+=1
        print("you guessed right after "+str(count)+" tries")