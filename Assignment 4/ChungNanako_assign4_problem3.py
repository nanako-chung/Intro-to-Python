#Nanako Chung
#October 5th, 2016
#M/W Intro to Comp Programming
#Problem #3: Arrows (with extra credit)

#get a positive number
num=int(input("How many columns? "))

#if number is less than 1, display an invalid entry and ask again
while num<1:
    print("Invalid entry, try again")
    num=int(input("How many columns? "))

#ask for direction
direction=input("Direction? (l)eft or (r)ight: ")

while True:
    if direction=="r":
        #set up counter
        star=0
        #start with 1 star
        while star<(num-1):
            print((" "*star)+"*")
            star+=1
        while (num+1)>1:
            #use string repetition
            print((" "*(num-1))+"*")
            #decrease num of stars
            num-=1
        break
    elif direction=="l":
        secondhalf=0
        while num>0:
            #use string repetition
            print((" "*(num-1))+"*")
            #decrease num of stars
            num-=1
            secondhalf+=1
        #set up counter
        star=1
        #use string repetition
        while star<secondhalf:
            print((" "*star)+"*")
            star+=1
        break
    else:
        print("Invalid direction.")
        direction=input("Direction? (l)eft or (r)ight: ")
