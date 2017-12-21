#Nanako Chung
#Intro to Computer Programming
#October 31st, 2016
#Assignment 6

#PART 2a

# function:   horizontal_line
# input:      a width value (integer)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width):
    pattern = width * "*" + "\n"
    return pattern

# function:   vertical_line
# input:      a shift value and a height value (both integers)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift, height):
    final_pattern = ""
    for i in range(height):
        row = shift * " " + "*" + "\n"
        final_pattern+=row
    return final_pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width, height):
    final_pattern = ""
    for i in range(height):
        row = "*" + (width-2)*" " + "*" + "\n"
        final_pattern+=row
    return final_pattern

#PART 2b

# function:   number_0
# input:      a width value (integer)
# processing: generates the number 0 as it would appear on a digital display
#             using the supplied width value and a given height of 5
# output:     returns the generated pattern (string)
def number_0(width):
    return horizontal_line(width)+two_vertical_lines(width, 3)+horizontal_line(width)
    
# function:   number_1
# input:      a width value (integer)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_1(width):
    pattern = vertical_line(width-1, 5)
    return pattern

# function:   number_2
# input:      a width value (integer)
# processing: generates the number 2 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_2(width):
    return horizontal_line(width)+vertical_line((width-1), 1)+horizontal_line(width)+vertical_line(0,1)+horizontal_line(width)

# function:   number_3
# input:      a width value (integer)
# processing: generates the number 3 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_3(width):
    return horizontal_line(width)+vertical_line((width-1), 1)+horizontal_line(width)+vertical_line((width-1),1)+horizontal_line(width)

# function:   number_4
# input:      a width value (integer)
# processing: generates the number 4 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_4(width):
    return two_vertical_lines(width, 2)+horizontal_line(width)+vertical_line((width-1), 2)

# function:   number_5
# input:      a width value (integer)
# processing: generates the number 5 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_5(width):
    return horizontal_line(width)+vertical_line(0,1)+horizontal_line(width)+vertical_line((width-1), 1)+horizontal_line(width)

# function:   number_6
# input:      a width value (integer)
# processing: generates the number 6 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_6(width):
    return horizontal_line(width)+vertical_line(0,1)+horizontal_line(width)+two_vertical_lines(width, 1)+horizontal_line(width)

# function:   number_7
# input:      a width value (integer)
# processing: generates the number 7 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_7(width):
    return horizontal_line(width)+vertical_line((width-1), 4)

# function:   number_8
# input:      a width value (integer)
# processing: generates the number 8 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_8(width):
    return horizontal_line(width)+two_vertical_lines(width, 1)+horizontal_line(width)+two_vertical_lines(width, 1)+horizontal_line(width)

# function:   number_9
# input:      a width value (integer)
# processing: generates the number 9 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_9(width):
    return horizontal_line(width)+two_vertical_lines(width, 1)+horizontal_line(width)+vertical_line((width-1), 2)

#PART 2c

# function:   print_number
# input:      a number to print (integer) and a width value (integer)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything
def print_number(num, width):
    if num==0:
        return number_0(width)
    elif num==1:
        return number_1(width)
    elif num==2:
        return number_2(width)
    elif num==3:
        return number_3(width)
    elif num==4:
        return number_4(width)
    elif num==5:
        return number_5(width)
    elif num==6:
        return number_6(width)
    elif num==7:
        return number_7(width)
    elif num==8:
        return number_8(width)
    else:
        return number_9(width)

#PART 2d

# function:   plus
# input:      a width value
# processing: prints the desired number of stars as a horizontal line with a vertical line down the middle to look like an addition sign 
# output:     does not return anything
def plus(width):
    if width%2==0:
        return (" "*((width//2)-1))+horizontal_line(2)+(" "*((width//2)-1))+horizontal_line(2)+horizontal_line(width)+(" "*((width//2)-1))+horizontal_line(2)+(" "*((width//2)-1))+horizontal_line(2)
    else:
        return vertical_line(width//2, 2)+horizontal_line(width)+vertical_line(width//2, 2)                                          

# function:   minus
# input:      a width value
# processing: prints the desired number of stars as a horizontal line to look like a minus sign
# output:     does not return anything
def minus(width):
    return ("\n"*2)+horizontal_line(width)

#PART 2e

# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct
def check_answer(number1, number2, answer, operation):
    if operation=="+":
        if number1+number2==answer:
            return True
        else:
            return False
    else:
        if number1-number2==answer:
            return True
        else:
            return False
