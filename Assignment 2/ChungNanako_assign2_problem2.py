# Nanako Chung
# September 19th, 2016
# M/W 2-3:15 Intro to Comp Sci
# Problem #2: Place Value Madness

# ask the user to input two values
value1 = int(input("Enter value 1: "))
value2 = int(input("Enter value 2: "))

# compute and display the 
ones1 = int(value1 % 10)
tens1 = int((value1 % 100)/10)
hundreds1 = int((value1 % 1000)/100)
thousands1 = int((value1 % 10000)/1000)

# compute and display the 
ones2 = int(value2 % 10)
tens2 = int((value2 % 100)/10)
hundreds2 = int((value2 % 1000)/100)
thousands2 = int((value2 % 10000)/1000)

# add place value totals
print()
print("Place Value Totals:")
print()
total_ones = ones1 + ones2
total_tens = tens1 + tens2
total_hundreds = hundreds1 + hundreds2
total_thousands = thousands1 + thousands2

# display the data
print("\t", ones1, "+", ones2, "=", total_ones, "one(s)")
print("\t", tens1, "+", tens2, "=", total_tens, "ten(s)")
print("\t", hundreds1, "+", hundreds2, "=", total_hundreds, "hundred(s)")
print("\t", thousands1, "+", thousands2, "=", total_thousands, "thousands(s)")
