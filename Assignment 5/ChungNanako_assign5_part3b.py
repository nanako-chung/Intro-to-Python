#Nanako Chung
#Intro to Computer Programming M/W
#October 24th, 2016
#Problem #3b: Find all Prime Numbers between 1 and 1000

#create a for loop to list numbers between 1 to 1000
for a in range(1, 1001):
    if a>1:
        #again, 2 is a special case because there are no other factors we can use lower than 2 to prove it is prime (not divisible by other numbers)
        if a==2:
            print(a, "is a prime number!")
        else:
            #create a nested for loop with upper range a (do not include a because we already know a%a==0)
            for i in range(2, a):
                #if a is divisible by a without a remainder, do not list it as a prime number
                if a%i==0:
                    break
                else:
                    #if a is divisible by the next number to i and the quotient is 1, then a is prime because it is not divisible by other numbers in the range
                    if a/(i+1)==1:
                        print(a, "is a prime number!")
                        break
    #if a is 1, then a is technically not prime; display this to user
    else:
        print(a, "is technically not a prime number.")
