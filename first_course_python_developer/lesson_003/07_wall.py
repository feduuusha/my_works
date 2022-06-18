# -*- coding: utf-8 -*-

# (цикл for)
import turtle

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

pen = turtle.Turtle()
turtle.bgcolor('blue')
pen.screen.screensize(800, 800)


def brick(point_x, point_y):
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


for k in range(-400, 400, 100):
    for z in range(-400, 400, 100):
        brick(z, k)
    for i in range(-450, 450, 100):
        brick(i, k + 50)
