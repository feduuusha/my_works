

def smile(point_x, point_y, color):
    import turtle
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.color(color)
    pen.down()
    pen.circle(30)
    pen.up()
    pen.setpos(point_x - 20, point_y + 35)
    pen.down()
    pen.circle(5)
    pen.up()
    pen.setpos(point_x + 20, point_y + 35)
    pen.down()
    pen.circle(5)
    pen.up()
    pen.setpos(point_x - 25, point_y + 30)
    pen.down()
    pen.right(90)
    pen.circle(25, 180)
    pen.ht()
