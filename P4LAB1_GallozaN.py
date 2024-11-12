#CTI 110
#P4LAB1
#Natasha Galloza
#11/12/2024

import turtle 
t = turtle.Turtle()

t.pensize(3)
t.pencolor("black")
t.shape("turtle")

# speedup
t.speed(9)
#triangle
for i in range(3):
    t.forward(100)
    t.right(120)

# trippy triangle
t.pencolor("red")
for i in range(15):
    t.forward(100)
    t.right(110)
    

t.pencolor("blue")
for i in range(15):
    t.forward(100)
    t.right(110)


t.pencolor("green")
for i in range(15):
    t.forward(100)
    t.right(110)

t.penup()
t.goto (230,230)
t.pendown()

# regular speed
t.speed(9)

# first version
"""
t.pencolor("black")
#Square
for side in range(4):
    t.forward(100)
    t.left(90)
    
t.pencolor("red")
for side in range(4):
    t.forward(120)
    t.left(90)
    
t.pencolor("blue")    
for side in range(4):
    t.forward(140)
    t.left(90)

t.pencolor("green")
for side in range(4):
    t.forward(160)
    t.left(90)
"""
# version 2 - rotate each time
for times in range(9):
    for color in ["black", "red", "blue", "green"]:
        t.pencolor(color)
        #draw the square
        for side in range(4):
            t.forward(120)
            t.left(90)
        # turn a little extra
        t.left(10)    


t.penup()
t.goto (-130,-100)
t.pendown()

#Snowflake
t.pencolor("light blue")
for flake in range(30):
    for color in ["aquamarine", "darkslategray1", "DarkTurquoise"]:
        t.pencolor(color) 
        #draw flake
        t.forward(120)
        t.back(120)
        t.left(29)
