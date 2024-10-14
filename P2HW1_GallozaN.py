#CTI 110
#P2HW1
#Galloza, N.
#10/10/2024

#Ask user to enter their budget
budget = float(input("What is your travel budget? $"))
#Where are they going
destination = input ("Where are you going?")
#Amount of gas
gas = input ("How much will you spend on gas? $")
#Amount on accommodation
accommodation = input ("How much will you spend on accommodation? $")
#Amount on food
food = input ("How much will you spend on food? $")

print ("-" * 10, "Travel Expenses", "-" * 10)

expenses = int(gas) + int(accommodation) + int(food)
left = int(budget) - int(expenses)

#format(total, ".2f")
#print(f"The price is: $ {price:".2f")
#print(name.rjust(10))


print ("Location: ", destination.rjust(20))

print ("Initial Budget: $", budget.rjust(10))
format(budget, ".2f")
print ("Fuel: $", gas.rjust(10))
format(gas, ".2f")
print ("Accommodation: $", accommodation.rjust(10))
format(accommodation, ".2f")
print ("Food: $", food.rjust(10))
format(food, ".2f")
print ("Remaining Balance: $", left.rjust(10))
format(left, ".2f")

print ("-" * 35)



