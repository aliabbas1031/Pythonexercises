import random
import sys
def guessgame():

    user = int(input("please enter one number between 1 to 9 for guess game: "))
    computer = random.randint(1,9)

    if user == computer:
        print("you guessed right")
    else:
        print("your guess was wrong, right number was ",computer)


while True:

    print("Do you want to play guess game,y/n")

    firsttime = input()
    play=0
    continueplay = 0
    if firsttime == 'n':
        print("Thank you, See you later")
        sys.exit
        break
    else:
        guessgame()
        play+=1
        print("you played "+str(play)+" times")
        while True:
            print("Do you want to continue,y/n")
            playagain = input()
        
            if playagain == 'n':
                print("Thank you, See you later")
                sys.exit
                break
            else:
                guessgame()
                continueplay+=1
                finalplay = play+continueplay
                print("you played "+str(finalplay)+" times")





