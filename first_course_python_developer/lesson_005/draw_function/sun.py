def sun(point_x, point_y):
    import turtle
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.color('yellow')
    pen.pensize(5)
    pen.left(90)
    pen.down()
    for i in range(60, 361, 60):
        pen.circle(30, 60)
        pen.right(90)
        pen.forward(20)
        pen.right(180)
        pen.forward(20)
        pen.right(90)
