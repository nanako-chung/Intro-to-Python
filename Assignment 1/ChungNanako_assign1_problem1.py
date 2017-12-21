# Nanako Chung
# September 15th, 2016
# M/W Intro to Comp Sci
# Problem #1: Variables & Print Statements

# First, we must name the class by storing data into a variable.
class_name = "Introduction to Computer Programming"
# In this case, our variable name is class_name and the data being stored is "Introduction to Computer Programming".
# Since it is in quotes (""), the data is called a string.

# Secondly, create three variables that store the test average data.
# This is the same idea, except we do not need to put quotes around numbers to store them on the computer as numbers.
test1avg = 95
test2avg = 76
test3avg = 87

# Thirdly, we must format it in accordance to the output given in the problem.
# We must be careful with quoting and spacing. This is the reason we used " ", '"', the sep function, and the end function.
print("Average Test Scores For", " ", '"', class_name, '"', sep='', end=":")
print()

# Lastly, we display the data stored on to the screen using the print function.
print(" - Test #1:", test1avg)
print(" - Test #2:", test2avg)
print(" - Test #3:", test3avg)
