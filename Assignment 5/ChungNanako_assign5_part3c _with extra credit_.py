#Nanako Chung
#Intro to Computer Programming M/W
#October 24th, 2016
#Problem #3c: Find all Prime Numbers between 1 and 1000 (with extra credit!!)

#create a while loop to reprompt bad user
while True:
    startnum=int(input("Start number: "))
    endnum=int(input("End number: "))
    if startnum<=0 or endnum<=0:
        print("Start and end must be positive")
        print()
    elif startnum>endnum:
        print("End number must be greater than start number")
        print()
    elif startnum==endnum:
        print("Start number cannot equal end number")
        print()
    else:
        break
print()
#set an accumulator variable to count how many numbers are being listed in the outcome
count=0
#create a for loop to go through all the numbers within the range, looking for a prime number
for a in range(startnum, endnum+1):
    #again, a special case (see previous program comments about 2)
    if a==2:
        print(format(a, ">4d"), end="")
        #this counts as one outcome!
        count+=1
    else:
        #set up another for loop to create a variable to test if a is divisible by other numbers besides 1 and itself
        for i in range(2, a):
            #if a is divisible by a number in i, it is not prime so do not list it
            if a%i==0:
                break
            else:
                #see other programs for explanations of this
                if a/(i+1)==1:
                    #format the outputs: right align, with a total of four spaces; do not go on to the next line (that is what end function is there for)
                    print(format(a, ">4d"), end="")
                    #counter for how many outputs there are
                    count+=1
                    #if the counter goes up to 10, start printing the outputs on a new line
                    if count==10:
                        #restart counter to 0
                        count=0
                        print()
                        #exit loop
                        break
