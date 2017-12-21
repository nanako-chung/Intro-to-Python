#Nanako Chung
#Professor Kapp
#Intro to Computer Programming M/W
#7 November 2016
#Assignment 7

#PART 2a
name=input("Name: ")
sumcleanup=0
counter=0
lowername=name.lower()
if name.isalnum()==True:
    print("Your 'cleaned up' name is:", lowername)
    print("Your 'cleaned up' name reduces to:")
    for c in lowername:
        addcleanup=ord(c)-96
        sumcleanup+=addcleanup
        print(addcleanup, end=" ")
        counter+=1
        if counter==len(lowername):
            break
        else:
            print("+", end=" ")
    print("=", sumcleanup)
else:
    if (" " in lowername) or ("!" in lowername) or ("#" in lowername) or ("$" in lowername) or ("%" in lowername) or ("&" in lowername):
        lowername=lowername.replace("!", "")
        lowername=lowername.replace("#", "")
        lowername=lowername.replace("$", "")
        lowername=lowername.replace("%", "")
        lowername=lowername.replace("&", "")
        lowername=lowername.replace(" ", "")
        print("Your 'cleaned up' name is:", lowername)
        print("Your 'cleaned up' name reduces to:")
        for c in lowername:
            addcleanup=ord(c)-96
            sumcleanup+=addcleanup
            print(addcleanup, end=" ")
            counter+=1
            if counter==len(lowername):
                break
            else:
                print("+", end=" ")
        print("=", sumcleanup)
