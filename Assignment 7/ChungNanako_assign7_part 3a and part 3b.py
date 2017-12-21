#Nanako Chung
#M/W Intro to Comp Programming
#November 14th, 2016
#Assignment 7: Part 3a and Part 3b

# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter 
#             in the supplied word. for example, if word="cat" and num=1 
#             we could generate any of the following:
#             cZaQtR
#             cwaRts
#             cEaett
# 
#             if word="cat" and num=2 we could generate any of the following:
#             cRtaHFtui
#             cnnaNYtjn
#             czAaAitym
#
# output:     returns the newly generated word
def add_letters(original, num):
    import random
    randletters=""
    word=""
    #create a for loop to go through each character in the word
    for c in original:
        for i in range(num):
            pickcase=random.randint(0,2)
            if pickcase==0:
                #choose uppercase letter
                index=random.randint(97, 122)
            elif pickcase==1:
                #choose lowercase letter
                index=random.randint(65, 90)
            else:
                #choose exclamation point
                index=33
            #convert ascii indexes to character value using chr()
            case=chr(index)
            #string the random letters together
            randletters+=case
        #string the word together with each character plus the random characters
        newword=c+randletters
        word+=newword
        randletters=""
    return word

# function:   remove_letters
# input:      a word to unscramble (String) and the number of characters to remove (integer)
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#                  character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word
def remove_letters(word, num):
    newword=""
    #only add the strings (characters) that matter to form the new word
    a=word[::num+1]
    newword+=a
    return newword

# function:   shift_characters
# input:      a word (String) and a number of characters to shift (integer)
# processing: shifts each character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the supplied integer.  for example,
#             if word = "apple" and num=1 the newly generated word would be:
#
#             bqqmf
#
#             because we added +1 to each character. if we were to call the function with
#             word = "bqqmf" and num=-1 the newly generated word would be:
#           
#             apple
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
# output:     returns the newly generated word
def shift_characters(word, num):
    newword=""
    #create for loop to iterate through each character in word
    for c in word:
        #have the index increase by the number of desired digits and then convert it back to a character value
        a=chr(ord(c)+num)
        #put the characters together
        newword+=a
    return newword

#create a while loop
while True:
    #ask if the user wants to encode, decode, or quit
    option=input("(e)ncode, (d)ecode or (q)uit: ")
    if option=="e":
        #reprompt if number is not between 1 and 5
        while True:
            num=int(input("Enter a number between 1 and 5: "))
            if num<1 or num>5:
                print("Invalid input, try again.")
            else:
                break
        phrase=input("Enter a phrase to encode: ")
        #call functions from part 3a and encode
        nw=shift_characters(phrase, num)
        print("Your encoded word is:", add_letters(nw, num))
        print()
    elif option=="d":
        #reprompt if number is not between 1 and 5
        while True:
            num=int(input("Enter a number between 1 and 5: "))
            if num<1 or num>5:
                print("Invalid input, try again.")
            else:
                break
        phrase=input("Enter a phrase to decode: ")
        #call functions from 3a and decode
        nw=remove_letters(phrase, num)
        print("Your decoded word is:", shift_characters(nw, -num))
        print()
    #if q then quit
    elif option=="q":
        break
    #reprompt
    else:
        print("Invalid input, try again.")
