# -*- coding: utf-8 -*-

import turtle


# # нарисовать ветку дерева из точки (300, 5) вертикально вверх длиной 100
# pen = turtle.Turtle()
# pen.up()
# pen.setpos(0, -200)
# pen.down()
# pen.left(90)
# pen.forward(100)
# point = pen.pos()


# сделать функцию рисования ветки из заданной точки,
# заданной длины, с заданным наклоном


# def branch(angle, length, point=(0, 0)):
#     pen.setpos(point)
#     pen.right(angle)
#     pen.forward(length)
#     point = pen.pos()
#     return point
#
#
# branch(60, 100, point)

# написать цикл рисования ветвей с постоянным уменьшением длины на 25% и отклонением на 30 градусов


# сделать функцию branch рекурсивной


def branch(angle, length=100.0, point_x=0.0, point_y=-50.0):
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


for z in range(0, 101, 20):
    branch(90, 100, 0, z)
    left_branch(90, 100, 0, z)
