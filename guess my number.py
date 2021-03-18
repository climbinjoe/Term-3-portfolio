# # joseph simper
# 9/20
# guess my number 1.0

import random

#intro
print("\twelcom to 'guess my number' !")

question = input("what difficulty would you like Easy, Medium, or Hard")
if ("Ea" in question) or ("ea" in question):
    diff = 1
    maxrange = 10
    trys = 3
elif ("M" in question) or ("m" in question):
    diff = 2
    maxrange = 50
    trys = 5
else:
    diff = 3
    maxrange = 100
    trys = 10

theNumber = (random.randint(1,maxrange))
print(theNumber)

print("\nI'm thinking of a number between 1 and "+str(maxrange)+".")
print("Try to guess in in "+str (trys)+" attempt.\n")

winner = False
#guess 1
guess = int(input("pick a number between 1 and "+str(maxrange)))

if guess == theNumber:
        winner = True

elif guess < theNumber:
    print("guess higher")

else:
    print("guess lower")
#guess 2
if winner == False:
    guess = int(input("pick a number between 1 and "+str(maxrange)))

    if guess == theNumber:
        winner = True

    elif guess < theNumber:
        print("guess higher")

    else:
        print("guess lower")
#guess 3
if winner == False:
    if diff > 1:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 4
if winner == False:
    if diff > 1:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 5
if winner == False:
    if diff > 2:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 6
if winner == False:
    if diff > 2:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 7
if winner == False:
    if diff > 2:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 8
if winner == False:
    if diff > 2:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 9
if winner == False:
    if diff > 2:
        guess = int(input("pick a number between 1 and "+str(maxrange)))
        if guess == theNumber:
            winner = True

        elif guess < theNumber:
            print("guess higher")

        else:
            print("guess lower")
#guess 10
if winner == False:
    guess = int(input("pick a number between 1 and "+str(maxrange)))
    if guess == theNumber:
        winner = True

    elif guess < theNumber:
        pass

    else:
        pass
#end of code
if winner == True:
    print("you win")
else:
    print("you loose the number was",theNumber)
print("game over")
