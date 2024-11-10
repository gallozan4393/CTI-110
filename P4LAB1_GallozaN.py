#CTI 110
#P4LAB1
#Natasha Galloza
#11/10/2024

import turtle            
t = turtle.Turtle()    
t.pensize(3)
t.pencolor("green")     


#TRIANGLE
t.left(120)
t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)

t.pencolor("blue")

#SQUARE
for x in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.done()             

