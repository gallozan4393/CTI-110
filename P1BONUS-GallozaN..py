#CTI 110
#P1BONUS
#Natasha Galloza
#10/3/2024

import turtle
t = turtle.Turtle()
t.pensize(3)

#"N" Initial
t.penup()
t.goto(0,0)
t.pendown()

t.left(90)
t.fd(100)

t.rt(150)
t.fd(115)

t.lt(150)
t.fd(100)

#Circle
t.penup()
t.goto(110,55)
t.pendown()

t.circle(80)

#Top Star
t.penup()
t.goto(-80,100)
t.pendown()

t.lt(75)
t.fd(100)
t.rt(150)
t.fd(100)
t.rt(140)
t.fd(100)
t.rt(140)
t.fd(100)
t.rt(140)
t.fd(100)

#Bottom Star
t.penup()
t.goto(-100,-70)
t.pendown()

t.lt(75)
t.fd(100)
t.rt(150)
t.fd(100)
t.rt(140)
t.fd(100)
t.rt(140)
t.fd(100)
t.rt(140)
t.fd(100)

#Right Star
t.penup()
t.goto(210,160)
t.pendown()

t.lt(75)
t.fd(100)
t.rt(150)
t.fd(100)
t.rt(140)
t.fd(100)
t.rt(140)
t.fd(100)
t.rt(140)
t.fd(100)

