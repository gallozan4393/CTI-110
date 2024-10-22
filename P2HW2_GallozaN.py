#CTI 110
#P2HW2 - Lists
#Natasha Galloza
#10/17/2024

print("Please enter grade for each Module (enter after each)")
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))


#Results

print ("-" * 10, "Results", "-" * 10)

module = [mod1, mod2, mod3, mod4, mod5, mod6]

#print("You entered these grade:", module)
#print("There are", len(module), "grades.")

print("Lowest Grade: ",min(module))
print("Largest Grade: ", max(module))
print("Sum of Grades: ", sum(module))

average = sum(module) / len(module)

print("Average: ", format(average, ".2f"))

                            
#AVERAGE FIXED!!
#print format(average, ".2f")

print ("-" * 30)
