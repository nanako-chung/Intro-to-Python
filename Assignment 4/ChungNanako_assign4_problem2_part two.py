#Nanako Chung (with help from Anusha)
#October 8th, 2016
#M/W Intro to Comp Programming
#Problem #2: Pick Up Sticks

#part2

#ask user for a number of sticks to be used in the game
num=int(input("How many sticks (10-100)? "))

#create a loop to indicate whether the number inputted is too big, too small, or just right
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
    
#create an accumulator variable
turn=1

#create a loop to keep the program running for both player 1 and 2
while True:
    #use mod to check who's turn it is
    #even is player 2 and odd is player 1
    if turn%2==0:
        player="Player 2"
    else:
        player="Player 1"
    print()
    print("Turn:", player)
    #present to user how many sticks there are
    print("There are", num, "sticks on the table.")
    #ask user how many sticks he or she wants to take
    take=int(input("How many sticks do you want to take (1, 2 or 3)? "))
    if take==1 or take==2 or take==3:
        #the new number of sticks will become the old number of sticks subtracted by the taken sticks
        num=num-take
        if num==0:
            print()
            print("There are no sticks left on the table. Game over.")
            #add turn to declare winner (since person who picks up the last stick loses)
            turn=turn+1
            #use mod to check who's turn it is
            if turn%2==0:
                player="Player 2"
            else:
                player="Player 1"
            print(player, "wins!")
            break
        elif num<0:
            print("Sorry, that's an invalid amount of sticks to take.")
            num=num+take
        else:
            turn+=1
    else:
        print("Sorry, that's not a valid number.")
