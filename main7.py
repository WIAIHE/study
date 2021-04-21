from turtle import *
from random import *

t = Turtle()
t.speed(7)
t.color("black", "yellow")
for k in range(5):
    x = randint(-200, 200)
    y = randint(-200, 200)
    c = randint(10, 150)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(c)
        t.right(144)

t.end_fill()
