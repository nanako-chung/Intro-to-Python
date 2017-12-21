# Nanako Chung
# September 16th, 2016
# M/W Intro to Comp Sci
# Problem #2: Using the print function

# First, we must name the class by asking the user to store data into a variable. We use the input function to do this.
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

# Secondly, we create spaces on lines and print the data accordingly.
print()
print("Here are your names in every possible order:")
print("--------------------------------------------")
print()

# The next three lines determine how the names are represented in #1.
# The end function is used to prevent the comma used from the sep=", " of interfearing with the "1.", but to keep all the data on the same line separated by commas.
print("1.", end=" ")
print(name1, name2, name3, sep=", ")
print()

# This is the same as the previous three lines, except the variables are presented in a different order.
print("2.", end=" ")
print(name1, name3, name2, sep=", ")
print()

# This is the same as the previous three lines, except the variables are presented in a different order.
print("3.", end=" ")
print(name2, name1, name3, sep=", ")
print()

# There is a "\n" because we are indicating to Python that we would like this printed on the next line. 
print("4.", name2, "\n", name3, "\n", name1, sep="")
print()

# This is the same as the previous two lines, except the variables are presented in a different order.
print("5.", name3, "\n", name2, "\n", name1, sep="")
print()

# This is the same as the previous two lines, except the variables are presented in a different order.
print("6.", name3, "\n", name1, "\n", name2, sep="")
