# Nanako Chung
# September 19th, 2016
# M/W 2-3:15 Intro to Comp Sci
# Problem #3: Grade Calculator

# ask user for their name
name = input("What is your name? ")

# ask user for name of class using variable
class_name = input("What class are you in? ")
print()
test_worth = float(input("How much are tests worth in this class (i.e. 0.40 for 40%): "))

# ask the user for 3 test scores
test1 = float(input("Enter test score #1: "))
test2 = float(input("Enter test score #2: "))
test3 = float(input("Enter test score #3: "))
print()

# calculate test average and display to user
test_avg = float((test1+test2+test3) / 3)
ftest_avg = format(test_avg, ".2f")
print("Your test average is:", ftest_avg)
print()

# ask the user for the weight of hw assignments in their class
hw_worth = float(input("How much are the homework assignments worth in this class (i.e. 0.60 for 60%): "))

# ask the user for 3 hw assignment scores
hw1 = float(input("Enter homework score #1: "))
hw2 = float(input("Enter homework score #2: "))
hw3 = float(input("Enter homework score #3: "))
print()

# calculate the student's hw average and display to user
hw_avg = float((hw1+hw2+hw3) / 3)
fhw_avg = format(hw_avg, ".2f")
print("Your homework average is: ", fhw_avg)
print()

# calculate the student's final grade and display it to the user
final_score = format(((hw_avg * hw_worth) + (test_avg * test_worth)), ".2f")
print("Thanks, Craig. Your final score in", class_name, "is", final_score)
