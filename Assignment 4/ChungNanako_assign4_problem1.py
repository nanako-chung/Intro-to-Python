#Nanako Chung
#October 3rd, 2016
#M/W Intro to Comp Programming
#Problem #1: Roll the Dice

#create a loop (consider if the value user put in is not a valid input
while True:
    #prompt user to enter amount of sides on dice
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, or 20)? "))
    if sides==4 or sides==6 or sides==8 or sides==10 or sides==12 or sides==20:
        print()
        print("Thanks! Here we go...")
        print()
        break
    #display to the user that the input is not a valid size
    else:
        print("Sorry, that's not a valid size.")
        sides = int(input("How many sides on your dice (4, 6, 8, 10, 12, or 20)? "))

#enter random numbers produced by the dice
import random

#trial count
trialnum = 0

#doubles count
doubles = 0

#sumcount
sumdie1=0
sumdie2=0

#create a loop to keep the die going
while True:
    trialnum +=1
    die1 = random.randint(1, sides)
    die2 = random.randint(1, sides)
    sumdie1=sumdie1+die1
    sumdie2=sumdie2+die2
    #if the rolls produce a snake eye
    if (die1==1) and (die2==1):
        doubles+=1
        print(trialnum, ".", " ", "die number 1 is", " ", die1," ", "and die number 2 is", " ", die2, sep="")
        print()
        print("You got snake eyes! Finally! On try number", " ", trialnum, "!", sep="")
        # calculate percent of doubles
        percent = (doubles/trialnum)*100
        spercent = format(percent, ".2f")
        print("Along the way you rolled doubles", doubles, "time(s)", "("+spercent+"%", "of all rolls were doubles"+")")
        break
    #count the snake eyes as part of the double rolls count
    else:
        if die1==die2:
            doubles+=1
        print(trialnum, ".", " ", "die number 1 is", " ", die1," ", "and die number 2 is", " ", die2, sep="")

#find average roll for each die with format
avg1=sumdie1/trialnum
favg1=format(avg1, ".2f")
print("The average roll for die #1 was", favg1)
avg2=sumdie2/trialnum
favg2=format(avg2, ".2f")
print("The average roll for die #2 was", favg2)
