#CTI 110
#P1HW2
#Natasha Galloza
#10/8/2024


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

print ("Location: ", destination)
print ("Initial Budget: $", budget)
print ("Fuel: $", gas)
print ("Accommodation: $", accommodation)
print ("Food: $", food)
print ("Remaining Balance: $", left)
