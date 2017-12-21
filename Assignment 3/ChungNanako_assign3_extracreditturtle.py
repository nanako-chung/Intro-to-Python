#Nanako Chung
#September 29th, 2016
#M/W Intro to Comp Programming
#Problem #1 with extra credit

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
#display on turtle
if side2+side3>side1 and side1+side2>side3 and side3+side1>side2:
    print("This is a valid triangle!")
    if (fside2==fside3 and fside3==fside1) or (fside2==fside1 and fside==fside1) or (fside2==fside3 and fside2==fside1):
        print("This is an equilateral triangle")
        import turtle
        turtle.setup(500,500,point1_x,point1_y)
        turtle.pensize(5.0)
        turtle.fillcolor("Blue")
        turtle.begin_fill()
        turtle.forward(side1)
        turtle.right(240)
        turtle.forward(side2)
        turtle.right(240)
        turtle.forward(side3)
        turtle.end_fill()
        turtle.bye
    elif fside2==fside3 or fside3==fside1 or fside2==fside1:
        print("This is an isosceles triangle")
        import turtle
        turtle.setup(500,500,0,0)
        turtle.pensize(5.0)
        turtle.fillcolor("Yellow")
        turtle.begin_fill()
        turtle.forward(side1)
        turtle.left(135)
        turtle.forward(side2)
        turtle.left(135)
        turtle.forward(side3)
        turtle.end_fill()
        turtle.bye
    else:
        print("This is a scalene triangle")
        import turtle
        turtle.setup(500,500,0,0)
        turtle.pensize(5.0)
        turtle.fillcolor("Green")
        turtle.begin_fill()
        turtle.left(18)
        turtle.forward(side1)
        turtle.left(57)
        turtle.forward(side2)
        turtle.left(150)
        turtle.forward(side3)
        turtle.end_fill()
        turtle.bye
else:
    print("This is not a valid triangle")
    import turtle
    turtle.setup(500,500,0,0)
    turtle.forward(side1)
    import random
    turtle.right(random.randint(1,180))
    turtle.forward(side2)
    turtle.right(random.randint(1,180))
    turtle.forward(side3)
    turtle.right(random.randint(1,180))
    turtle.bye
