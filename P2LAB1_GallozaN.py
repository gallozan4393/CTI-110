#CTI 110
#P2LAB1
#Galloza, N.
#10/10/2024

#What are they buying?
ice_cream = input("What flavor of ice cream are you buying? ")

#How many they want?
amount = int(input("How many do you want?"))

#Price per item
price_ice_cream = float(input("How much is it? $"))
total = price_ice_cream * amount

# format (total, ".2f")
print ("The price for", amount, ice_cream, "ice cream is: $", format(total, ".2f"))




