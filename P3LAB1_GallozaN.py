#CTI 110
#P3LAB1
#Natasha Galloza
#10/22/2024

def main():
    print("Choose Your Own Adventure")
    go_home()

def go_home():
    print("You decide to go home.")
    print("But should you get some food?")
    print("1. Order pizza 🍕")
    print("2. Order tacos 🌮")
    print("3. Order wings 🍗")
    choice = int(input())
    if choice == 1:
        get_pizza()
    if choice == 2:
        get_tacos()
    if choice == 3:
        get_wings()
#After food!
    at_home()
#Inside the house
    inside_home()

def get_pizza():
    print("The cashier guy befriends you 🤝")
def get_tacos():
    print("The tacos are too spicy 🥵")   
def get_wings():
    print("The food is delicious! 🥳") 

def at_home():
    print("You get home, which door do you go through?")
    print("1. Front Door")
    print("2. Backdoor")
    print("3. Window")
    choice = int(input())
    if choice == 1:
        go_front()
    if choice == 2:
        go_back()
    if choice == 3:
        go_window()

def go_front():
    print("The door is unlocked")   
def go_back():
    print("The door is locked, you go to the front door 🚪")
def go_window():
    print("The window does not open, you go to the front door 🚪")

def inside_home():
    print("You get inside and lock the door behind you.")
    print("Someone knocks on your door.")
    print("1. Look through peephole")
    print("2. Ask who is it?")
    print("3. Ignore and go eat your food")
    choice = int(input())
    if choice == 1:
        look_peephole()
    if choice == 2:
        ask_who()
    if choice == 3:
        ignore_eatfood()  

def look_peephole():
    print("You see a person with a mask 👹")
    print("The masked person finds a way inside the house")
    print("He hurts you and takes your food 🤕")
def ask_who():
    print("Nobody answers 😨")
    print("The masked person gets inside your house.")
    print("You are dead 💀")
def ignore_eatfood():
    print("You ignore the knock and enjoy your food.")
    print("You live happy ever after 🥳")

#Start the program
main()    
