#Nanako Chung
#Intro to Computer Programming M/W
#Professor Kapp
#December 5th, 2016
 
#get a filename
name=input("Enter a class file to grade (i.e. class1 for class1.txt): ")
filename=name+".txt"

try:
        #attempt to open the file for reading
        myfile=open(filename, "r")
except:
        print("Sorry, can't open this filename!")
else:
        #grab the data
        alldata=myfile.read()

        #close the file
        myfile.close()

        #announce success
        print("Successfully opened", filename)

        #we need to isolate each student
        allstudents=alldata.split("\n")

        #look at each student record one at a time and see how many problems they got correct or incorrect
        
        unusable=0
        allscores=[]
        
        #convert the answer key to a list (the 0 is there so that the indexes correctly match the answer key)
        answerkey = "0,B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
        listanswers=answerkey.split(",")
        for record in allstudents:
                correct=0
                wrong=0
                #process this record
                liststudentanswers=record.split(",")
                if len(liststudentanswers) != 26:
                        unusable+=1
                else:
                    for i in range(1, len(liststudentanswers)):
                               if liststudentanswers[i]==listanswers[i]:
                                       correct+=4
                               elif liststudentanswers[i]=="":
                                       pass
                               else:
                                       wrong+=1
                    score=correct-wrong
                    allscores+=[score]

#set up a counter variable
i=0
#open the file to write the grades in
file_object=open(name+"_grades.txt", "w")
#for loop to iterate over all the n numbers and the grades
for record in allstudents:
        liststudentanswers=record.split(",")
        file_object.write(str(liststudentanswers[0])+","+format(allscores[i], ".2f")+"\n")
        i+=1
file_object.close()

#sort all the scores so that we can easily determine the median
allscores.sort()
if len(allscores)%2!=0:
        median=allscores[len(allscores)//2-1]
else:
        median=(allscores[len(allscores)//2-1]+allscores[len(allscores)//2])/2

#determining the mode
unique=[]
frequency=[]
frequency+=[0]*len(allscores)
for i in allscores:
        if i not in unique:
                unique+=[i]
        else:
                location=unique.index(i)
                frequency[location]+=1
frequencymax=max(frequency)
modelocation=frequency.index(frequencymax)
mode=unique[modelocation]

#display output to user
print()
print("Grade summary:")
print("Total students:", len(allstudents)-unusable)
print("Unuable lines in the file:", unusable)
print("Highest score:", max(allscores))
print("Lowest score:", min(allscores))
print("Mean score:", format(sum(allscores)/len(allscores), ".2f"))
print("Median score:", format(median, ".2f"))
print("Mode:", format(mode, ".2f"))
print("Range:", format(max(allscores)-min(allscores)))
curve=input("Would you like to curve the exam? 'y' or 'n': ")


