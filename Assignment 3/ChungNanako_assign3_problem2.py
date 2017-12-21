#Nanako Chung
#September 29th, 2016
#M/W Intro to Comp Programming
#Problem #2: Guess the Number Game

#let program select random integer
import random
secretnum = random.randint(1, 10)

#prompt user to guess a number between 1 and 10
print("I'm thinking of a number between 1 and 10!")
guess=int(input("What is your guess? "))
if guess == secretnum:
    print("You got it!")
    print("The secret number was", " ", secretnum, ".", sep="")
    print("It took you 1 try to guess this number.")
elif guess<1 or guess>10:
    print("This number is not in the range.")
else:
    #determine if number is too high or too low
    if guess<secretnum:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
    #run program another time
    guess=int(input("What is your guess? "))
    if guess == secretnum:
        print("You got it!")
        print("The secret number was", " ", secretnum, ".", sep="")
        print("It took you 2 tries to guess this number.")
    elif guess<1 or guess>10:
        print("This number is not in the range.")
    else:
        #determine if number is too high or too low
        if guess<secretnum:
            print("Too low, try again.")
        else:
            print("Too high, try again.")
        #run program another time
        guess=int(input("What is your guess? "))
        if guess == secretnum:
            print("You got it!")
            print("The secret number was", " ", secretnum, ".", sep="")
            print("It took you 3 tries to guess this number.")
        elif guess<1 or guess>10:
            print("This number is not in the range.")
        else:
            print("The secret number was", " ", secretnum, ".", sep="")
            print("You didn't guess the number.")
