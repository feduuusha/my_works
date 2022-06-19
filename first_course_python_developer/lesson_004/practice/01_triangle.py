# -*- coding: utf-8 -*-

# pip install simple_draw
# from math import cos

import turtle
import time

pen = turtle.Turtle()


# нарисовать треугольник из точки (300, 300) с длиной стороны 200
pen.up()
pen.setpos(150, 150)
pen.down()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(135)
pen.forward((200**2 + 200**2)**.5)
pen.ht()
time.sleep(3)


# определить функцию рисования треугольника из заданной точки с заданным наклоном
# инвалидная функция
# def triangle(point_x, point_y, angle=60, length=200):
#     pen = turtle.Turtle()
#     if angle == 60:
#         pen.up()
#         pen.setpos(point_x, point_y)
#         pen.left(angle)
#         pen.down()
#         pen.forward(length)
#         pen.left(180-angle)
#         pen.forward(length)
#         pen.left(180 - angle)
#         pen.forward(length)
#         pen.ht()
#     else:
#         pen.up()
#         pen.setpos(point_x, point_y)
#         # pen.left(angle)
#         pen.down()
#         pen.forward(length)
#         pen.left(180 - angle)
#         pen.forward(length)
#         pen.left(130)
#         pen.forward((length**2 + length**2 - 2 * length * length * cos(angle))**.5)
#         pen.ht()
#
#
# triangle(100, 100, 60, 500)

def triangle(point_x, point_y, angle=0, length=200):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.left(angle)
    pen.down()
    pen.forward(length)
    pen.left(180-60)
    pen.forward(length)
    pen.left(120)
    pen.forward(length)
    pen.ht()


triangle(100, 100, 60, 100)
