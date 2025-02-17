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


def draw_red_square(x, y,c):
    tom.pu()
    tom.goto(x, y)
    tom.pendown()
    tom.begin_fill()
    tom.color('grey')
    tom.fillcolor(c)  # Red color
    for _ in range(4):
        tom.forward(25)
        tom.right(90)
    tom.end_fill()
    tom.penup()

red_pixels = [(-100, 200), (-75, 175),(-100,175),
              (-75,200),(-100,150),(-125,175),(-125,150),
              (-150,150),(-150,125),(-125,125),(-75,75),
              (-50,75),(-50,50),(-75,50),(-75,25),(-50,25),
              (-75,0),(-50,0),(0,-150),(25,-175),]

tom.pu()
tom.goto(-175,100)
tom.pd()
tom.begin_fill()
for i in range(5):
    tom.color('grey',('#ff0000'))
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
    tom.color('grey',('#ed1c24'))
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
    tom.color('grey',('#ed1c24'))
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
    tom.color('grey',('#ed1c24'))
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
    tom.color('grey',('#ed1c24'))
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
    tom.color('grey',('#ed1c24'))
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
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-175,-75)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-225,-125)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-225,-100)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-250,-150)
tom.pd()

tom.begin_fill()
for i in range(1):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-275,-150)
tom.pd()

for x, y in red_pixels:
    draw_red_square(x, y, "#ff0000")

tom.pu()
tom.goto(-25,-0)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-50,-25)
tom.pd()

tom.begin_fill()
for i in range(5):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-50,-50)
tom.pd()

tom.begin_fill()
for i in range(6):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-75,-75)
tom.pd()

tom.begin_fill()
for i in range(4):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-25,-100)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-50,-200)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

def draw_black_square(x, y):
    tom.pu()
    tom.goto(x, y)
    tom.pendown()
    tom.begin_fill()
    tom.color('grey')
    tom.fillcolor('#000000')  
    for _ in range(4):
        tom.forward(25)
        tom.right(90)
    tom.end_fill()
    tom.penup()


def draw_grey_square(x, y):
    tom.pu()
    tom.goto(x, y)
    tom.pendown()
    tom.begin_fill()
    tom.fillcolor('#c7b299')  
    for _ in range(4):
        tom.forward(25)
        tom.right(90)
    tom.end_fill()
    tom.penup()

grey_pixels = [(-75,-100),(-50,-100),(-75,-125),(-50,-150),
               (-50,-125),(-25,-125),(-50,-175),]

for x, y in grey_pixels:
    draw_grey_square(x, y)

tom.pu()
tom.goto(-175,-100)
tom.pd()

tom.begin_fill()
for i in range(4):
    tom.color('grey',('#000000'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-125,-75)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#000000'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

black_pixels = [(-75,-25),(-75,-50),(-25,-150),(-25,-175),
                (0,-125),(25,-100),(25,-75),(-75,-175),
                (-75,-150),(-125,25),(-150,0),(-100,50),(-125,0),
                (-100,-125),(-175,-125),(25,-250),(125,-250),(100,-225)]

for x, y in black_pixels:
    draw_black_square(x, y)


tom.pu()
tom.goto(0,-200)
tom.pd()

tom.begin_fill()
for i in range(2):
    tom.color('grey',('#000000'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(-100,-225)
tom.pd()

tom.begin_fill()
for i in range(7):
    tom.color('grey',('#000000'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(50,-275)
tom.pd()

tom.begin_fill()
for i in range(3):
    tom.color('grey',('#000000'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(75,-250)
tom.pd()

tom.left(90)
tom.backward(25)
tom.begin_fill()
for i in range(8):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()

tom.pu()
tom.goto(50,-225)
tom.pd()

tom.begin_fill()
for i in range(8):
    tom.color('grey',('#ed1c24'))
    for i in range(4):
        tom.fd(25)
        tom.rt(90)
    tom.fd(25)
tom.end_fill()




tom.hideturtle
window.tracer(True)
turtle.exitonclick()