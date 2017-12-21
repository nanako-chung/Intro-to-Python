#Nanako Chung
#Professor Kapp
#Intro to Computer Programming M/W
#7 November 2016
#Assignment 7

#PART 1a
while True:
    #Ask the user for a username
    username=input("Enter a username: ")
    #calculate the length of the username
    print("* Length of username:", len(username))
    #see if all characters are alpha-numeric using an if statement
    print("* All characters are alpha-numeric:", end="")
    if username.isalnum()==True:
        print(" True")
    else:
        print(" False")
    #determine if the first and last characters that are not digits using if statements
    print("* First & last characters are not digits:", end="")
    if username[0].isdigit() == True or username[-1].isdigit() == True:
        print(" False")
    else:
        print(" True")
    #set up accumulator variables to count uppercase, lowercase, and digits
    lower=0
    upper=0
    digit=0
    for c in username:
        if c.islower()==True:
            lower+=1
        if c.isupper()==True:
            upper+=1
        if c.isnumeric()==True:
            digit+=1
    #display results to the user
    print("* # of uppercase characters in the username:", upper)
    print("* # of lowercase characters in the username:", lower)
    print("* # of digits in the username:", digit)
    #set up an if statement to display to the user whether the username is valid or not
    if 8<=len(username)<=15 and username.isalnum()==True and (username[0].isdigit() == True or username[-1].isdigit() == True)==False and upper>=1 and lower>=1 and digit>=1:
        print("Username is valid!")
        print()
        #PART 1b
        while True:
            #ask user for a password
            password=input("Enter a password: ")
            #calculate the length of the password using len
            print("* Length of password:", len(password))
            #see if username is in password and display to user
            print("* Username is part of password:", end="")
            if username in password:
                print(" True")
            else:
                print(" False")
            #set up accumulator variables to count uppercase, lowercase, and digits
            upper=0
            lower=0
            digit=0
            for c in password:
                if c.islower()==True:
                    lower+=1
                if c.isupper()==True:
                    upper+=1
                if c.isnumeric()==True:
                    digit+=1
            #display results to the user
            print("* # of uppercase characters in password:", upper)
            print("* # of lowercase characters in password:", lower)
            print("* # of digits in password:", digit)
            special=0
            if ("#" in password) or ("$" in password) or ("%" in password) or ("&" in password):
                special+=1
            print("* # of special characters in the password:", special)
            #set up an if statement to display to the user whether the password is valid or not
            if len(password)>=8 and digit>=1 and (username not in password) and upper>=1 and lower>=1 and digit>=1 and special>=1:
                print("Password is valid!")
                break
            else:
                print("Password is invalid, please try again.")
                print()
        break
    else:
        print("Username is invalid, please try again")
        print()
