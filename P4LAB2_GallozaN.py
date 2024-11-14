#CTI 110
#P4LAB2
#Natasha Galloza
#11/14/2024


def times_table():
    num = int(input("Enter a integer: "))
    while (num < 0):
        print("No negative numbers please.")
        num = int(input("Enter a integer: "))
    print("You entered: ", num)

#Times Table
    for num2 in range(1,13):
        answer = num * num2
        print(num, "*", num2, "=", answer)
    
def main():
    times_table()
    again = input("Do you want to run again? ")
    while (again == "yes"):
        times_table()
        again = input("Do you want to run again? ")
    print("Goodbye!")

#Start the program
main()
   

    







"""
print("test program")
count = 1
while count <= 5:
    print ("count is", count)
    count += 1
print("done")


for number in range (1,6):
    print(number)
print("done")


#input validation
num = int(input("Type number between 1 to 3:"))
while num < 1 or num > 3:
    print("Please try again")
    num = int(input("Type number between 1 to 3:"))
print("You entered:", num)
"""
