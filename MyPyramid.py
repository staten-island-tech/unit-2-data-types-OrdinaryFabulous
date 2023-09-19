# << Libraries >> #
import turtle
from turtle import * 

t = Turtle()
t.speed(0)

def square(length):
    for i in range(4):
        t.forward(length)
        t.right(90)

def row(squares, length):
    for i in range(squares):
        square(length)
        t.forward(length)

def pyramid(e, length):
    for j in range(e, 0, -1):
        row(squares=j, length=length)

        if j != 1:
            t.back((j - 1) * length)
            t.left(90)
            t.forward(length)
            t.right(90)

pyramid(10, 20)

turtle.done()