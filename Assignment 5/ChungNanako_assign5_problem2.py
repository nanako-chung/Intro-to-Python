#Nanako Chung
#Intro to Computer Programming M/W
#October 24th, 2016
#Problem #2: Dynamic Gradebook

#ask the user for number of students in class
numstudents=int(input("How many students are in your class? "))

#set up accumulator variable that adds up the test scores of all the students in class
sumtotal=0

#create a while loop to reprompt bad user
while True:
    if numstudents<=0:
        print("Invalid # of students, try again.")
        print()
        numstudents=int(input("How many students are in your class? "))
    else:
        #ask user for number of tests and reprompt bad user
        numtests=int(input("How many tests in this class? "))
        if numtests<=0:
            print("Invalid # of tests, try again.")
        else:
            print()
            print("Here we go!")
            print()
            #create a for loop to display the data for each student
            for i in range(1, numstudents+1):
                print("**** Student", i, "****")
                #create an accumulator variable for sum of test scores of each individual student
                sumstudent=0
                #create another for loop to ask user for test scores on each test
                for b in range(1, numtests+1):
                    #set up a while loop to reprompt bad user (again...)
                    while True:
                        testscore=int(input("Enter score for test #"+str(b)+": "))
                        if testscore<0:
                            print("Invalid score, try again.")
                        else:
                            #add the test scores of the student to assist in calculating average for student#i
                            sumstudent+=testscore
                            break
                    #add the test scores of all the students to assist in calculating overall average of class
                    sumtotal+=testscore
                #calculate average score of student and display to the user
                avgstudent=sumstudent/numtests
                favgstudent=format(avgstudent, ".2f")
                print("Average score for student #"+str(i), "is", favgstudent)
                print()
            #calculate average score of all students and display to the user
            avgtotal=sumtotal/(numtests*numstudents)
            favgtotal=format(avgtotal, ".2f")
            print("Average score for all students is:", favgtotal)
            break
