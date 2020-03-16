import random

print("rules are rock wins against scissors, scissorswins against paper and paper wins against rock")

print('''Please pick one:   1 for rock 
                            2 for paper
                            3 for scissors 
                            ''') 
while True:

    wins = 0
    loss = 0
    tie = 0

    user1 = str(input("please print your name: "))
    user2 = str(input("please print your name: "))
    a = int(input("please enter your entry for game which is either rock(1)/paper(2)/scissors(3): "))
    b = int(input("please enter your entry for game which is either rock(1)/paper(2)/scissors(3): "))

    while a  > 3 or a  <1 or b  > 3 or b  <1:
        a = input("please enter valid command")
        b = input("please enter valid command")

    if a  == 1:
        a == 'rock'
    if a  == 2:
        a == "paper"
    else: 
        a =="scissors"

    if b  == 1:
        b == 'rock'
    if b  == 2:
        b=="paper"
    else: 
        b=="scissors"

    print(user1 +  ' choice is ' + str(a) )
    print(user2 +  ' choice is ' + str(b) )

    if a==b:
        print("its a tie")
        tie+=1
    if((a==1 and b==3) or (a == 3 and b == 1)):
        print("rock wins =>",end = "")
        result = "rock"
    elif((a==2 and b==3) or (a == 3 and b == 2)):
        print("scissors wins =>",end = "")
        result = "scissors"
    else:
        print("paper wins =>",end = "")
        result = "paper"

    if result == "a":
        print("<==user1 wins==>")
        #wins+=1
    if result == 'b':
        print("<=user2 wins=>")
        #loss+=1

    print("Do you want to continue, y/n")

    user = input()

    if user.lower == 'n':
        break

print("wins are ",wins)
print("losses are ",loss)
print("tie is ",tie)
print("\nThanks for playing") 

