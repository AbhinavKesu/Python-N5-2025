students= int(input("how many students are there?"))
Pizza = round(students/8) + 1
print("The total number of pizzas needed is: " + str(Pizza))
PizzaPrice = 12
Total = Pizza * PizzaPrice
print("The total cost of the pizzas is: £" + str(Total))