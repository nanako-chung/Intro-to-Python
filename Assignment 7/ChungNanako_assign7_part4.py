#Nanako Chung
#Professor Kapp
#Intro to Computer Programming M/W
#7 November 2016
#Assignment 7

# function:   string_length
# input:      a word (String)
# processing: computes the length of the supplied String (without using the len() function)
# output:     returns the length of the string (integer)
def string_length(string):
    counter=0
    for c in string:
        counter+=1
    return counter
# sample code:
print ( string_length("apple") )	# 5
print ( string_length("pear")  )	# 4
print ( string_length("")      )	# 0
print()

# function:   string_isalpha
# input:      a word (String)
# processing: determines if the supplied String contains all alphabetic characters (A-Z,a-z)
#             DO NOT USE THE "isalpha()" METHOD!
# output:     returns True or False (boolean)
def string_isalpha(string):
    alphacount=0
    string_length(string)
    for c in string:
        if 65<=ord(c)<=90 or 97<=ord(c)<=122:
            alphacount+=1
    if string=="":
        return False
    elif alphacount==string_length(string):
        return True
    else:
        return False
# sample code:
print ( string_isalpha("apple")     )	# True
print ( string_isalpha("pear!")     )	# False
print ( string_isalpha("123")       )	# False
print ( string_isalpha("123 AbC")   )	# False
print ( string_isalpha("abc1")      )	# False
print ( string_isalpha("")          )	# False
print()

# function:   string_isupper
# input:      a word (String)
# processing: determines if the supplied String contains all uppercase characters (A-Z)
#             DO NOT USE THE "isupper()" METHOD!
# output:     returns True or False (boolean)
def string_isupper(string):
    upper=0
    string_length(string)
    for c in string:
        if 65<=ord(c)<=90:
            upper+=1
    if string=="":
        return False
    elif upper==string_length(string):
        return True
    else:
        return False
# sample code:
print ( string_isupper("apple")     )	# False
print ( string_isupper("PEAR")      )	# True
print ( string_isupper("123")       )	# False
print ( string_isupper("123 AbC")   )	# False
print ( string_isupper("ApPLE")     )	# False
print ( string_isupper("")          )	# False
print()

# function:   string_isdigit
# input:      a word (String)
# processing: determines if the supplied String contains all numeric characters (0-9)
#             DO NOT USE THE "isdigit()" METHOD!
# output:     returns True or False (boolean)
def string_isdigit(string):
    num=0
    string_length(string)
    for c in string:
        if 48<=ord(c)<=57:
            num+=1
    if string=="":
        return False
    elif num==string_length(string):
        return True
    else:
        return False
# sample code:    
print ( string_isdigit("apple")     )	# False
print ( string_isdigit("PEAR")      )	# False
print ( string_isdigit("123")       )	# True
print ( string_isdigit("123 AbC")   )	# False
print ( string_isdigit("ApPLE")     )	# False
print ( string_isdigit("")          )	# False
print()

# function:   string_swapcase
# input:      a word (String)
# processing: swaps uppercase characters with lowercase characters & vice-versa
#             DO NOT USE THE "swapcase()" METHOD!
# output:     returns a new copy of the String
def string_swapcase(string):
    string_isalpha(string)
    string_isupper(string)
    string_isdigit(string)
    counter=""
    for c in string:
        if string_isupper(c)==True:
            string.replace(c, c.lower())
            counter+=c
        elif c.lower()==True:
            string.replace(c, string_isupper(c))
            counter+=c
        else:
            counter+=c
    return counter
# sample code:
print ( string_swapcase("apple")     )	# APPLE
print ( string_swapcase("PEAR")      )	# pear
print ( string_swapcase("123")       )	# 123
print ( string_swapcase("123 AbC")   )	# 123 aBc
print ( string_swapcase("ApPLE")     )	# aPple
print ( string_swapcase("")          )	# (nothing prints)
print()

# function:   string_lower
# input:      a word (String)
# processing: converts all characters in a String to their lowecase equivalents
#             DO NOT USE THE "lower()" METHOD OR "str.lower()"!
# output:     returns a new copy of the String
def string_lower(string):
    count=0
    string_length(string)
    for c in string:
        if 97<=ord(c)<=122:
            count+=c
    return count
# sample code:
print ( string_lower("apple")     )	# apple
print ( string_lower("PEAR")      )	# pear
print ( string_lower("123")       )	# 123
print ( string_lower("123 AbC")   )	# 123 abc
print ( string_lower("ApPLE")     )	# apple
print ( string_lower("")          )	# (nothing prints)
print()
