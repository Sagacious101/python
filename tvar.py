import turtle as t
import math

t.shape("turtle")
t.speed(5)



"""
walls_width = int(input("Введите ширину стен "))
walls_height = int(input("Введите высоту стен "))
roof_height = int(input("Введите сторону "))
roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
roof_angle =  math.degrees(math.atan(roof_height / (walls_width/2)))
walls_color = input("стены цвет ")
roof_color = input('крыша цвет ')
door_height = int(input('дверь высота '))
door_width = int(input("дверь ширина "))
door_color = input("цвет двери ")
"""


"""
x - левый нижний угол стены
y - левый нижний угол стены
walls_height - высота стен
walls_wight - ширина стен
door_x - левый нижний угол стены
door_y - левый нижний угол стены
door_width - ширина двери
door_height - высота
"""

def draw_walls(walls_x, walls_y, walls_height, walls_width, walls_color):
    t.penup()
    t.goto(walls_x,walls_y)
    t.pendown()
    t.fillcolor(walls_color)
    t.begin_fill()
    for i in range (2):
        t.forward(walls_width)
        t.left(90)
        t.forward(walls_height)
        t.left(90)
    t.end_fill()


def draw_roof(roof_height,walls_width,roof_color,walls_height,roof_side, roof_angle,walls_x,roof_y):
    print("Нарисовали крышу")
    t.penup()
    t.goto(walls_x, roof_y)
    t.pendown()
    t.fillcolor(roof_color)
    t.begin_fill()
    t.setheading(roof_angle)
    t.forward(roof_side)
    t.setheading(-roof_angle)
    t.forward(roof_side)
    t.setheading(180)
    t.forward(walls_width)
    t.end_fill()


def draw_doors(door_x,door_width,door_height,door_color,walls_y,walls_width,walls_height):
    print("Нарисовали двери")
    t.penup()
    t.goto(door_x,walls_y)
    t.pendown()
    t.setheading(180)
    t.fillcolor(door_color)
    t.begin_fill()
    t.right(90)
    t.forward(door_height)
    t.right(90)
    t.forward(door_width)
    t.right(90)
    t.forward(door_height)
    t.right(90)
    t.forward(door_width)
    t.end_fill()



def draw_house(walls_x,
walls_y,
walls_width,
walls_height,
walls_color,
door_width,
door_height,
door_color,
roof_height,
roof_color
):
    roof_y = walls_y + walls_height
    door_x = (walls_x + (walls_width/2 - door_width/2))
    roof_side = math.sqrt(roof_height ** 2 + (walls_width / 2) ** 2)
    roof_angle = math.degrees(math.atan(roof_height / (walls_width/2)))
    draw_walls(walls_x, walls_y, walls_height, walls_width, walls_color)
    draw_roof(roof_height,walls_width,roof_color,walls_height,roof_side, roof_angle,walls_x,roof_y)
    draw_doors(door_x, door_width, door_height, door_color, walls_y, walls_width, walls_height)


draw_house(0, 0, 200, 100,"purple", 60, 80, "blue", 90, "red")
draw_house(200,200,100,100,"blue",40,60,"red",40,"purple")
t.done()
