#Nanako Chung
#Intro to Computer Programming M/W
#October 24th, 2016
#Problem #1: Pizza Party

#create counter for slices needed to get total amount of slices needed for order
slices_needed=0

#ask user for budget, cost of each slice, cost of each pie, and num of people
budget=float(input("Enter budget for your party: "))
cost_slice=float(input("Cost per slice of pizza: "))
cost_pie=float(input("Cost per whole pizza place: "))
people=int(input("How many people will be attending your party? "))

#create a for loop to count up the number of people
for i in range(1, people+1):
    slices_per_person=int(input("Enter number of slices for person "+"#"+str(i)+": "))
    #create while loop to ask user for number of slices per person
    while True:
        if slices_per_person<0:
            print("Not a valid entry, try again!")
            print()
            slices_per_person=int(input("Enter number of slices for person "+"#"+str(i)+": "))
        else:
            break
    #get total number of slices needed
    slices_needed+=slices_per_person

#calculate total cost of slices and format it
total=(((slices_needed//8)*cost_pie)+((slices_needed%8)*cost_slice))
ftotal=format(total, ".2f")

#calculate leftover cost
leftover=budget-total
fleftover=format(leftover, ".2f")

#create if statements to produce output
if leftover==0:
    print("You should purchase", slices_needed//8, "pies and", slices_needed%8, "slices")
    print("Your total cost will be:", ftotal)
    print("You will have no money left after your order.")
elif leftover<0:
    print("Your order cannot be completed.")
    print("You would need to purchase", slices_needed//8, "pies and", slices_needed%8, "slices")
    print("This would put you over the budget by", format(total-budget, ".2f"))
else:
    print("You should purchase", slices_needed//8, "pies and", slices_needed%8, "slices")
    print("Your total cost will be:", ftotal)
    print("You still have", fleftover, "after your order.")
