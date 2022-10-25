import turtle as t
import math

t.shape("turtle")
t.speed(0)



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


def draw_roof(roof_height,walls_width,roof_color):
    print("Нарисовали крышу")
    t.fillcolor(roof_color)
    roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
    roof_angle =  math.degrees(math.atan(roof_height / (walls_width/2)))
    t.right(roof_side)
    t.forward(100)


def draw_doors(door_width,door_height,door_color,walls_x,walls_y,walls_width,walls_height):
    print("Нарисовали двери")
    door_x = (walls_x + (walls_width/2 - door_width/2))
    door_y = walls_y
    t.penup()
    t.goto(door_x,walls_y)
    t.pendown()
    t.fillcolor(door_color)
    t.begin_fill()
    t.left(90)
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
    draw_walls(walls_x, walls_y, walls_height, walls_width, walls_color)
    draw_roof(roof_height,roof_color)
    draw_doors(door_width,door_height,door_color,walls_x,walls_y,walls_width,walls_height)


draw_house(0, 0, 200, 100,"purple", 50, 70, "blue", 50, "purple")

t.done()

