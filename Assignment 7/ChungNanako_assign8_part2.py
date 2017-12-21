#Nanako Chung
#Intro to Comp Programming M/W
#November 12th, 2016
#Assignment 8 Part 2

product_names = ["hamburger", "cheeseburger", "small fries"]
product_costs = [0.99, 1.29, 1.49]
quantity = [10, 5, 20]
#create a while loop to reprompt user if they do not select the correct letters
while True:
    request=input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port, or (q)uit: ")
    #if the user selects search, ask for a product name and then report how much of it there is and how much it costs
    if request=="s":
        name=input("Enter product name: ")
        if name in product_names:
            index=product_names.index(name)
            print("We sell", '"'+name+'"', "at", product_costs[index], "per unit")
            print("We currently have", quantity[index], "in stock")
        else:
            print("Sorry, we don't sell", '"'+name+'"')
        print()
    #if the user selects a list present, in formatted order, the cost of every product as well as the quantity of each product
    elif request=="l":
        print(format("Product", "26s"), end="")
        print(format("Price", "8s"), end="")
        print("Quantity")
        for i in range(len(product_names)):
            print(format(product_names[i], "26s"), end="")
            fcost=format(product_costs[i], ".2f")
            print(format(fcost, "8s"), end="")
            print(str(quantity[i]))
        print()
    #if the user selects add a product, use indexes to manipulate the list
    elif request=="a":
        #create while loop to reprompt user until they select a correct product name
        while True:
            newname=input("Enter a new product name: ")
            if newname in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                product_names.append(newname)
                #create a while loop to reprompt the user for a correct cost for the product
                while True:
                    newcost=float(input("Enter a product cost: "))
                    if newcost==0:
                        print("Invalid cost. Try again.")
                    else:
                        product_costs.append(newcost)
                        #create another while loop to reprompt and ask for the quantity of products
                        while True:
                            newquantity=int(input("How many of these products do we have? "))
                            if newquantity<=0:
                                print("Invalid quantity. Try again.")
                            else:
                                #if the quantity is correct, add the product using the append() function
                                quantity.append(newquantity)
                                print("Product added!")
                                print()
                                break
                        break
                break
    #if the user requests a remove function, use the remove() function to take out the name and the cost and the quantity of a product from all lists
    elif request=="r":
        name=input("Enter a product name: ")
        if name in product_names:
            index=product_names.index(name)
            product_names.remove(name)
            del product_costs[index]
            del quantity[index]
            print("Product removed!")
            print()
        else:
            print("Product doesn't exist. Can't remove.")
            print()
    #if user asks to update the product list...
    elif request=="u":
        #ask the user for a product name; if it doesn't exist reprompt them
        name=input("Enter a product name: ")
        #create an if statement to determine whether the product is existing
        if name in product_names:
            index=product_names.index(name)
            print("What would you like to update?")
            #ask the user what they would like to update about the product
            update=input("(n)ame, (c)ost, (q)uantity: ")
            #update the name using index manipulation
            if update=="n":
                while True:
                    newname=input("Enter a new name: ")
                    if newname in product_names:
                        print("Duplicate name!")
                    else:
                        product_names[index]=newname
                        print("Product name has been updated.")
                        print()
                        break
            #update the cost also using index manipulation
            elif update=="c":
                while True:
                    newcost=float(input("Enter a new cost: "))
                    if newcost>0:
                        product_costs[index]=newcost
                        print("Product cost has been updated.")
                        print()
                        break
                    else:
                        print("Invalid cost!")
            #update the quantity also using index manipulation
            elif update=="q":
                while True:
                    newquantity=int(input("Enter a new quantity: "))
                    if newquantity>0:
                        quantity[index]=newquantity
                        print("Product quantity has been updated.")
                        print()
                        break
                    else:
                        print("Invalid quantity!")
            else:
                print("Invalid option")
                print()
        else:
            print("Product doesn't exist. Can't update.")
            print()
    #if the user requests a report, display the largest and smallest costs and what products they correspond with 
    elif request=="e":
        #finding the most expensvie and cheapest products
        biggest=product_names[product_costs.index(max(product_costs))]
        smallest=product_names[product_costs.index(min(product_costs))]
        total=0
        for i in range(len(product_costs)):
            allproductcost=product_costs[i]*quantity[i]
            total+=allproductcost
        #display them to user
        print(format("Most expensive product:", "28s"), max(product_costs), "("+biggest+")")
        print(format("Least expensive product:", "28s"), min(product_costs), "("+smallest+")")
        print(format("Total value of all products:", "28s"), format(total, ".2f"))
        print()
    #break if the user requests to quit
    elif request=="q":
        print("See you soon!")
        break
    else:
        print("Invalid option. Try again.")
        print()
