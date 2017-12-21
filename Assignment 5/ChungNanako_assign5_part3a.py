#Nanako Chung
#Intro to Computer Programming M/W
#October 24th, 2016
#Problem #3a: Prime Number Finder

#create a while loop to remprompt bad user
while True:
    posnum=int(input("Enter a positive number to test: "))
    if posnum<=0:
        print("I said a POSITIVE number!")
    else:
        #leave while loop
        break
#create an if loop to specify conditions about prime number
#e.g. if number is 1, the number is not prime. if number is 2, number is prime, but this is a special case because there are no numbers to test except 1.
if posnum>2:
    #create a for loop with variable i as a counter to divide into posnum
    for i in range(2, posnum):
        #if the number is divided by i without remainders, that means that posnum has a divisor in addition to 1 and itself; thus, posnum is not prime
        if posnum%i==0:
            print(i, "is a divisor of", posnum, "...", "stopping")
            print()
            print(posnum, "is not a prime number.")
            break
        #continue checking to see if posnum is prime
        else:
            print(i, "is NOT a divisor of", posnum, "...", "continuing")
            #create a further condition stating that if the next number above i (i+1) is divisible by posnum AND posnum has no other divisors in the range, posnum is prime
            if posnum/(i+1)==1:
                print()
                print(posnum, "is a prime number!")
                break
elif posnum==1:
    print(posnum, "is not a prime number.")
elif posnum==2:
    print(posnum, "is a prime number.")
