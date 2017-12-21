#Nanako Chung
#October 8th, 2016
#M/W Intro to Comp Programming
#Problem #2: Pick Up Sticks

#part 1
#ask user for a number of sticks to be used in the game
num=int(input("How many sticks (10-100)? "))

#display whether the number inputted is too much, too little, or just right
while True:
    if num>100:
        print("Sorry, that's too many sticks. Try again.")
        num=int(input("How many sticks (10-100)? "))
    elif num<10:
        print("Sorry, that's too few sticks. Try again.")
        num=int(input("How many sticks (10-100)? "))
    else:
        print("Great Let's play ...")
        break

#present number of sticks on the table
while True:
    print()
    print("There are", num, "sticks on the table.")
    #ask user how many sticks they want to take from table
    take=int(input("How many sticks do you want to take (1, 2 or 3)? "))
    if take==1 or take==2 or take==3:
        #new number of sticks on table is the old amount minus the number of sticks taken
        num=num-take
        #no more sticks left
        if num==0:
            print()
            print("There are no sticks left on the table. Game over.")
            break
        #new number cannot be negative, since there is no such thing as having a negative amount of sticks
        if num<0:
            print("Sorry, that's an invalid amount of sticks to take.")
            num=num+take
    else:
        print("Sorry, that's not a valid number.")
