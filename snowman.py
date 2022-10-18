import turtle as t

t.shape("turtle")
t.speed(0)

#параметры

radius = int(input("Введите радиус первого круга: "))
cout_circle = int(input("Введите количество шаров: "))
x = int(input("Введите ось x: "))
y = int(input("Введите ось y: "))
color = input("Введите цвет снеговика(hex): ")
t.penup()
t.goto(x,y)
t.pendown()

t.color(color)
t.begin_fill()
for i in range (cout_circle):
    t.circle(radius)
    t.left(90)
    t.penup()
    t.forward(radius * 2)
    t.pendown()
    t.right(90)
    radius = radius / 2
t.end_fill()

t.done()


