from turtle import *
t = Turtle()

x = int(input())
n = int(input())

for i in range(n):
    t.forward(x)
    t.left(360 / n)
