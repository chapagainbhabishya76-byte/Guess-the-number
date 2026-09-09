print("")
print("==============GUESS THE NUMBER==============")
print("---> 1 to 100")
import random
num = random.randint(1,100)
while True:
    guess = input("Guess the number or [Q] to Quit :")
    if(guess == "Q"):
        break
    else:
        guess = int(guess)

    if(guess>num):
        if((num - 3)<guess and (num + 3)>guess):
            print("You are close, try guessing little less then this..\n ")
        else:
            print("You are so wrong dude!,try guessing less then this..\n ")

    elif(guess<num):
            if((num - 3)<guess and (num + 3)>guess):
                print("You are close, try guessing little high then this..\n ")
            else:
                print("You are so wrong dude!,try guessing high then this..\n ")

    elif(guess == num):
        print("Congratulations, you guessed the right number! ")
        break
print("")
print("---------Game completed sucessfully----------")
    