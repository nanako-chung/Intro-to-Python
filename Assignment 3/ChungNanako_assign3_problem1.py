#Nanako Chung
#September 29th, 2016
#M/W Intro to Comp Programming
#Problem #1: Valid Triangle Tester

print("Valid Triangle Tester")

#ask user for the x and y positions of points
point1_x = float(input("Enter Point #1 - x position: "))
point1_y = float(input("Enter Point #1 - y position: "))
point2_x = float(input("Enter Point #2 - x position: "))
point2_y = float(input("Enter Point #2 - y position: "))
point3_x = float(input("Enter Point #3 - x position: "))
point3_y = float(input("Enter Point #3 - y position: "))
print()

# calculate distance between points, format sides, then display to user
side1 = (((point1_x-point2_x)**2)+(point1_y-point2_y)**2)**.5
side2 = (((point2_x-point3_x)**2)+(point2_y-point3_y)**2)**.5
side3 = (((point1_x-point3_x)**2)+(point1_y-point3_y)**2)**.5

fside1 = format(side1, ".2f")
fside2 = format(side2, ".2f")
fside3 = format(side3, ".2f")
print("The length of each side of your test shape is:")
print()
print("Side 1:", fside1)
print("Side 2:", fside2)
print("Side 3:", fside3)
print()

#test to see if triangle is valid
#use formatted side values to round to nearest number and avoid Python error
if side2+side3>side1 and side1+side2>side3 and side3+side1>side2:
    print("This is a valid triangle!")
    if (fside2==fside3 and fside3==fside1) or (fside2==fside1 and fside==fside1) or (fside2==fside3 and fside2==fside1):
        print("This is an equilateral triangle")
    elif fside2==fside3 or fside3==fside1 or fside2==fside1:
        print("This is an isosceles triangle")
    else:
        print("This is a scalene triangle")
else:
    print("This is not a valid triangle")
