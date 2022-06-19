

def snowflake(point_x, point_y, length, k=0):
    import turtle
    pen = turtle.Turtle()
    if k > 7:
        pen.ht()
        return True
    pen.up()
    pen.setpos(point_x, point_y)
    pen.down()
    pen.forward(length)
    pen.right(180)
    pen.forward(length - .5 * length)
    pen.right(180)
    pen.right(45)
    pen.forward(length - .5 * length)
    pen.right(180)
    pen.forward(length - .5 * length)
    pen.left(270)
    pen.forward(length - .5 * length)
    pen.right(180)
    pen.forward(length - .5 * length)
    pen.right(45)
    pen.forward(length - .5 * length)
    pen.right(135)
    snowflake(point_x, point_y, length, k + 1)
