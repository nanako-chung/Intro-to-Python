#Nanako Chung
#Intro to Computer Programming M/W
#October 24th, 2016
#Problem #4: 3D Graphics

#filling the axes with cubes
#fill the x axis
# enter into a loop that iterates between the values of -500 to +500, skipping 50 each time
for x in range(-500, 501, 50):
	# draw a cube at this x position
	cube(x, 0, 0)
#fill the z axis
# enter into a loop that iterates between the values of -500 to +500, skipping 50 each time
for z in range(-500, 501, 50):
	# draw a cube at this z position
	cube(0, 0, z)
#fill the y axis
# enter into a loop that iterates between the values of -500 to +500, skipping 50 each time
for y in range(0 501, 50):
	# draw a cube at this y position
	cube(0, y, 0)

#half of the tree/diamond
#create a function
def pyramid():
    #set the size
    size = 100
    #create a for loop to indicate how much the sizes change by
    for y in range(0,101,10):
        cube(0, y, 0, size, 10, size)
        #decrease size by 10
        size-=10
pyramid()
