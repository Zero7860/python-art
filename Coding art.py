import turtle
from turtle import *
window = turtle.Screen()
window.tracer(False)
hideturtle()
turtle.Screen().bgcolor("white")
tom = Turtle()
tom.shape('turtle')
tom.width(1)
tom.penup()
tom.goto(-100, 200)
tom.pendown()

def darredsquare():
    tom.begin_fill()
    tom.color("#ed1c24")
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.end_fill()

def yellowsquare():
    tom.begin_fill()
    tom.color("#f7941d")
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.end_fill()


def draw_red_square(x, y):
    tom.goto(x, y)
    tom.pendown()
    tom.begin_fill()
    tom.fillcolor("#ff0000")  # Red color
    for _ in range(4):
        tom.forward(25)
        tom.right(90)
    tom.end_fill()
    tom.penup()
red_pixels = [(-100, 200), (-75, 175),(-100,175),(-75,200),(-100,150),(-125,175),(-125,150),(-150,150),(-150,125),(-125,125)]

for x, y in red_pixels:
    draw_red_square(x, y)

tom.goto(-175,100)
tom.pd()
tom.begin_fill()
for i in range(5):
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)

tom.end_fill()
tom.pu()
tom.goto(-200,75)
tom.pd()

tom.begin_fill()
for i in range(5):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-200,50)
tom.pd()

tom.begin_fill()
for i in range(4):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-225,25)
tom.pd()

tom.begin_fill()
for i in range(4):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-250,0)
tom.pd()

tom.begin_fill()
for i in range(4):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-250,-25)
tom.pd()

tom.begin_fill()
for i in range(7):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-225,-50)
tom.pd()

tom.begin_fill()
for i in range(6):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-200,-75)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('black',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()



tom.hideturtle
window.tracer(True)
turtle.exitonclick()