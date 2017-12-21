#Nanako Chung
#Intro to Comp Programming M/W
#November 12th, 2016
#Assignment 8 Part 1

#ask the user for a number
num=int(input("Enter a number greater than or equal to 10: "))

#build a list that will hold all of our working values
values = ["P"]*num

#set 0 and 1 to be not prime
values[0] = "N"
values[1] = "N"

#set accumulator variable
prime=[]
count=0

#look at all elements starting at 2 going to the end and see if that element is holding a P
for i in range(2, len(values)):
    #is this element holding a P?
    if values[i] == "P":
        #found a prime one! need to set all multiples of this number equal to not prime!
        for a in range(i*2, len(values), i):
            values[a]="N"
for i in range(2, len(values)):
    #is this element holding a P?
    if values[i] == "P":
        prime+=[str(i)]
#create a for loop to iterate over the prime list
for i in range(len(prime)):
    print(format(prime[i], "4s"), end="")
    #format to make it break every 10 numbers
    count+=1
    if count==10:
        count=0
        print()

