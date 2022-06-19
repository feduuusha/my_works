# -*- coding: utf-8 -*-

import turtle
import time

pen = turtle.Turtle()
turtle.screensize(1200, 600)
# познакомится с параметрами библиотечной функции рисования снежинки sd.snowflake()


def snowflake(point_x, point_y, length, k=0):
    if k > 7:
        pen.ht()
        time.sleep(2)
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


snowflake(100, 100, 200)
