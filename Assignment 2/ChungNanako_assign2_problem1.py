# Nanako Chung
# September 19th, 2016
# M/W 2-3:15 Intro to Comp Sci
# Problem #1: Dynamic Tip Calculator

# display the words as shown in the output
print("Hello! I'm here to help you calculate your tip.")

# ask the user the bill and tip splitting the bill using the input function and also convert these numbers to floats
bill = float(input("How much was your bill? (Enter a numeric value without commas or dollar signs): "))
tip_percent = float(input("How much tip would you like to leave? (Enter an integer value): "))

# make the tip into a percent, then multiply it with the bill to get the tip amount
tip = float(tip_percent / 100.00 * bill)

# ask the user for number of individuals splitting the bill
individuals = float(input("How many individuals are splitting the bill? (Enter an integer value): "))

# calculate the total by adding the bill and the tip
total = bill + tip

# calculate how much it would be if the group split the bill
splitting_bill = total / individuals

# format the floating numbers from the previous data so that it displays 2 decimal points only
ftip1 = format(tip, ".2f")
ftotal = format(total, ".2f")
fsplitting_bill = format(splitting_bill, ".2f")

# insert line breaks and display data as shown in the output (including dollar signs and periods)
print()
print("Thanks! Calculating your bill & tip...")
print()
print("You need to leave", "$" + ftip1, "as a tip.")
print("Your total bill will be", "$" + ftotal + ".")
print("Each individual should pay", "$" + fsplitting_bill + ".")
