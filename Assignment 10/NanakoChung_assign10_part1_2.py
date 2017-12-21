#Nanako Chung
#Intro to Computer Programming M/W
#Professor Kapp
#December 12, 2016

#PART 1

#get a word from the user
word=input("Enter a word to test: ")

#get all of the movie reviews
myfile=open("movie_reviews.txt", "r")

#grab all the data in the file
alldata=myfile.read()
alldata=alldata.lower()

#close the file
myfile.close()

#split the alldata variable on the \n character
allreviews=alldata.split("\n")

total=0
num=0

#examine all of the reviews one at a time
for review in allreviews:
        #split apart the review based on the spaces
        split_review=review.split(" ")

        #grab the value of the review
        value=int(split_review[0])

        #see if the rest of the review contains our word
        if word in split_review[1:]:

                #add to an accumulator variable
                total+=value
                num+=1
#display to the user that the word appears 0 times
if num==0:
        print("'"+word+"'", "appears 0 times")
        print("There is no average score for reviews containing the word", "'"+word+"'")
        print("Cannot determine if this word is positive or negative")
#display to the user how many times the word appears and the average score for that word
else:
        print("'"+word+"'", "appears", num, "times")
        print("The average score for reviews containing the word", "'"+word+"'", "is", total/num)

        #determine if this is a positive or negative word
        if total/num>2:
                print("This is a positive word")
        else:
                print("This is a negative word")


#PART 2

#get all of the movie reviews
myfile=open("movie_reviews.txt", "r")

#grab all the data in the file
alldata=myfile.read()
alldata=alldata.lower()

#close the file
myfile.close()

#split the alldata variable on the \n character
allreviews=alldata.split("\n")

#set up an empty dictionary to hold our words
sentiment={}

#examine all reviews
for review in allreviews:

        #split up the review
        split_review=review.split(" ")

        #extract the value of this review
        value=int(split_review[0])

        #examine all of the words in this review
        for i in range(1, len(split_review)):

                #see if this word is a new one
                if split_review[i] not in sentiment:

                        #add it to our dictionary
                        sentiment[split_review[i]]=[value,1]

                else:
                    
                        #the word is already here! just add to it
                        sentiment[split_review[i]][0]+=value
                        sentiment[split_review[i]][1]+=1

#input a phrase
print()
phrase=input("Enter a phrase: ")

#split the phrase to get just the words
split_phrase=phrase.split(" ")

#accumulator for scores
totalscore=0

#accumulator for words not in sentiment
unusable=0

#iterate over each word in the phrase and test to see if it is in dictionary
for words in split_phrase:

        #if word is not in dictionary, add one to the accumulator variable
        if words not in sentiment:
                print("'"+words+"'", "does not appear in any movie reviews")
                unusable+=1

        #if word is in the dictionary, add score to the totalscore variable
        else:
                score=sentiment[words][0]/sentiment[words][1]
                print("'"+words+"'", "appears", sentiment[words][1], "times with an average score of", score)
                totalscore+=score

#calculate and display average, taking into consideration the unusable amount of words 
avg=totalscore/(len(split_phrase)-unusable)
print("Average score for this phrase is:", avg)

#determine if this is a positive or negative phrase
if avg>2:
        print("This is a positive phrase")
else:
        print("This is a negative phrase")

