import turtle as t
import random

t.shape("turtle")
t.speed(0)
t.colormode(255)

#параметры
while True:
    x = random.randint(-300, 300)
    y = random.randint(-100, 100)
    cout_circle = random.randint(3, 5)
    radius = random.randint(20, 50)
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    t.fillcolor(red, green, blue)
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range (cout_circle):
        t.begin_fill()
        t.circle(radius)
        t.left(90)
        t.penup()
        t.forward(radius * 2)
        t.right(90)
        if radius < 2:
            break
        radius = radius / 2
        t.pendown()
        t.end_fill()
    t.penup()
    t.goto(0,0)
    t.pendown()

t.done()


