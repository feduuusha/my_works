

def brick(point_x, point_y):
    import turtle
    pen = turtle.Turtle()
    pen.screen.screensize(800, 800)
    turtle.bgcolor('blue')
    pen.pensize(5)
    pen.color('yellow')
    pen.up()
    pen.setpos(point_x, point_y)
    pen.down()
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.up()
    pen.setpos(point_x + 100, point_y)
    pen.down()
    pen.left(90)
    pen.ht()


def wall(height, length):
    for k in range(-height, height, 100):
        for z in range(-length, length, 100):
            brick(z, k)
        for i in range(-length - 50, length + 50, 100):
            brick(i, k + 50)


def house(height, length):
    import turtle
    pen = turtle.Turtle()
    pen.ht()
    wall(height, length)
    pen.pensize(5)
    pen.color('yellow')
    pen.up()
    pen.setpos(0, height)
    pen.down()
    pen.forward(length + 50)
    pen.right(180)
    pen.forward((length + 50) * 2)
    pen.left(90)
    pen.forward(height * 2)
    pen.left(90)
    pen.forward((length + 50) * 2)
    pen.left(90)
    pen.forward(height * 2)
    pen.left(45)
    pen.forward(((length + 50) ** 2 + (length + 50) ** 2) ** .5)
    pen.left(90)
    pen.forward(((length + 50) ** 2 + (length + 50) ** 2) ** .5)
    pen.up()
    pen.setpos(0, height)
    pen.right(135)
    pen.forward(length / 2)
    pen.right(90)
    pen.down()
    pen.circle(50)
