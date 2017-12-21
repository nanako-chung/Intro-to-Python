#PART 2f

import myfunctions
#check to see if functions are properly called
answer = myfunctions.check_answer(1,1,2,"+")
print(answer)

#PART 2g (with drill mode and statistics for extra credit)
while True:
    probs=int(input("How many problems would you like to attempt? "))
    if probs<=0:
        print("Invalid number, try again")
        print()
    else:
        break
while True:
    width=int(input("How wide do you want your digits to be? 5-10: " ))
    if width<5 or width>10:
        print("Invalid width, try again")
        print()
    else:
        break
while True:
    drill=input("Would you like to activate 'drill' mode? yes or no: ")
    if drill=="yes" or drill=="no":
        break
    else:
        print("Invalid answer, try again")
        print()

import random
#set up a counter to see how many problems the user gets right
correct=0
addition=0
addition_correct=0
subtraction=0
subtraction_correct=0
addition_attempts=0
subtraction_attempts=0
if drill=="no":
    print()
    print("Here we go!")
    #create a for loop to keep asking user problems
    for i in range(probs):
        print()
        print("What is .....")
        print()
        #set up two random integers
        num1=random.randint(0,9)
        num2=random.randint(0,9)
        #display first number to user
        print(myfunctions.print_number(num1, width))
        #have python pick an operator randomly and display it to the user
        choice_of_sign=["+", "-"]
        sign=random.choice(choice_of_sign)
        if sign=="+":
            print(myfunctions.plus(width))
            addition+=1
        else:
            print(myfunctions.minus(width))
            subtraction+=1
            print()
            print()
        #display the second number to the user
        print(myfunctions.print_number(num2, width))
        #ask the user for the answer
        ansr=int(input("= "))
        #use check_answer to see if the user was right, then display result to user
        if myfunctions.check_answer(num1, num2, ansr, sign)==True:
            print("Correct!")
            #count how many questions the user gets right
            correct+=1
            if sign=="+":
                addition_correct+=1
            else:
                subtraction_correct+=1
        else:
            print("Sorry, that's not correct.")
    print()
    print("You got", correct, "out of", probs, "correct!")
    print()
    print("Total addition problems presented:", addition)
    print("Correct addition problems:", addition_correct, "("+format((addition_correct/addition*100), ".1f")+"%"+")")
    print()
    print("Total subtraction problems presented:", subtraction)
    print("Correct subtraction problems:", subtraction_correct, "("+format((subtraction_correct/subtraction*100), ".1f")+"%"+")")
    
#activate drill mode
else:
    #create a for loop to keep asking user problems
    for i in range(probs):
        print()
        print("What is .....")
        print()
        #set up two random integers
        num1=random.randint(0,9)
        num2=random.randint(0,9)
        #display first number to user
        print(myfunctions.print_number(num1, width))
        #have python pick an operator randomly and display it to the user
        choice_of_sign=["+", "-"]
        sign=random.choice(choice_of_sign)
        if sign=="+":
            print(myfunctions.plus(width))
            addition+=1
        else:
            print(myfunctions.minus(width))
            subtraction+=1
            print()
            print()
        #display the second number to the user
        print(myfunctions.print_number(num2, width))
        while True:
            #ask the user for the answer
            ansr=int(input("= "))
            #use check_answer to see if the user was right, then display result to user
            if myfunctions.check_answer(num1, num2, ansr, sign)==True:
                print("Correct!")
                if sign=="+":
                    addition_correct+=1
                else:
                    subtraction_correct+=1
                break
            else:
                print("Sorry, that's not correct.")
                if sign=="+":
                    addition_attempts+=1
                else:
                    subtraction_attempts+=1
    print()
    print("Thanks for playing!")
    print()
    print("Total addition problems presented:", addition)
    print("# of extra attempts needed:", addition_attempts, end=" ")
    if addition!=0 and addition_attempts==0:
        print("(perfect!)")
    print()
    print("Total subtraction problems presented:", subtraction)
    print("# of extra attempts needed:", subtraction_attempts, end=" ")
    if subtraction!=0 and subtraction_attempts==0:
        print("(perfect!)")
