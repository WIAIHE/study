from turtle import *
t = Turtle()
t.pencolor("red")

for i in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.forward(50)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
