
def main ():
    x, y = 300, 400
    width, height = 200, 300

    draw_house(x, y, width, height)

def draw_house(x, y, width, height):
    """
    Function is drawing house all width and height from reference point (x, y),
    which is in the middle lower point of fundamental
    :param x: It is the middle of the house
    :param y: It is the lower of the house fundamental
    :param width: It is all width the house include fundamental and roof
    :param height: It is all height the house include fundamental and roof
    :return: None
    """
    print('Типа рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_height - walls_height

    draw_house_foundation(x, y, width, foundation_height)
    draw_house_walls(x, y - foundation_height, walls_width, walls_height)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)



def draw_house_foundation(x, y, width, height):
    print('Типа рисую фундамент...', x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):
    print('Типа рисую стены...', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    print('Типа рисую крышу...', x, y, width, height)
    pass


main()