import turtle as t



def draw_house(x, y, walls_width, walls_height):
    '''

    x - лувфй нижний угол стены
    y - лувый нижний угол стены
    walls_width - ширина стен
    walls_height -высота стен


    '''
    draw_walls(x, y, walls_width, walls_height)
    draw_roof()
    draw_door()


def draw_walls(x, y, walls_width, walls_height):
    print(f"нарисовал стену из {x}, {y}")
    print(f"ширина стен {walls_width}")
    print(f"высота стен {walls_height}")

def draw_roof():
    print("нарисовал крышу")


def draw_door():
    print("нарисовал дверь")



draw_house(-100, -200)
walls_width(200)
walls_height(100)

