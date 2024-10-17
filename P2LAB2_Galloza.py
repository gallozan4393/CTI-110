#CTI 110
#P2LAB2 - Lists
#Natasha Galloza
#10/17/24

# Using lists and loops to draw
import turtle
t = turtle.Turtle()

#remember pensize, pencolor
t.pensize(3)
t.pencolor("blue")

#simple loop
for length in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
    t.forward(length)
    t.left(60)

t.pensize(3)
t.pencolor("red")

for length in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
    t.forward(length)
    t.left(60)

t.pensize(3)
t.pencolor("green")

for length in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
    t.forward(length)
    t.left(60)
    



