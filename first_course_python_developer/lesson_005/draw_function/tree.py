

def branch(angle, length=100.0, point_x=0.0, point_y=-50.0):
    import turtle
    if length < 10:
        return 10
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.down()
    pen.left(angle)
    pen.forward(length)
    pen.ht()
    (k, y) = pen.pos()
    branch(angle * 0.65, length * 0.65, point_x=k, point_y=y)


def left_branch(angle, length=100.0, point_x=0.0, point_y=-50.0):
    import turtle
    if length < 10:
        return 10
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.down()
    pen.left(180)
    pen.right(angle)
    pen.forward(length)
    pen.ht()
    (k, y) = pen.pos()
    left_branch(angle * 0.65, length * 0.65, point_x=k, point_y=y)


def tree(point_x):
    for z in range(0, 101, 20):
        branch(90, 100, point_x, z)
        left_branch(90, 100, point_x, z)
