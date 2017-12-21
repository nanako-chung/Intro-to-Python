# Nanako Chung
# September 16th, 2016
# M/W Intro to Comp Sci
# Problem #3: Math Expressions

# First, display the words "mL to US Fluid Volume Units" in accordance to given output.
print("--------------------------------------------------------------")
print("\t", "\t", "mL to US Fluid Volume Units")
print("--------------------------------------------------------------")

# Next, represent and display 250mL as a decimal or floating point number.
mL = float(250)

# Thirdly, represent and display 250 mL in tsp using the conversion given and some variables.
mL_to_tsp = .202884*mL
print("\t", "mL:", "\t", "\t", mL)
print("\t", "tsp:", "\t", "\t", mL_to_tsp)

# Then, represent and display 50.721000000000004 tsp in tbsp using the conversion given and some variables.
tsp_to_tbsp = mL_to_tsp / 3
print("\t", "tbsp:", "\t", "\t", tsp_to_tbsp)

# Represent and display 16.907 tbsp in cups using the conversion given and some variables.
tbsp_to_cups = tsp_to_tbsp / 16
print("\t", "cup(s):", "\t", tbsp_to_cups)

# Represent and display 1.0566875 cups in pints using the conversion given and some variables.
cups_to_pints = tbsp_to_cups / 2
print("\t", "pint(s):", "\t", cups_to_pints)

# Represent and display 0.52834375 pints in quarts using the conversion given and some variables.
pints_to_quarts = cups_to_pints / 2
print("\t", "quart(s):", "\t", pints_to_quarts)

# Represent and display 0.264171875 quarts in gallons using the conversion given and some variables.
quarts_to_gallons = pints_to_quarts / 4
print("\t", "gallon(s):", "\t", quarts_to_gallons)

# Represent and display 250mL in fl oz using the conversion given and some variables.
mL_to_floz = mL / 29.5735
print("\t", "fl oz:", "\t", mL_to_floz)

print("--------------------------------------------------------------")
