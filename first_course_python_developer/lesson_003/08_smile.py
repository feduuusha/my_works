# -*- coding: utf-8 -*-

# (определение функций)


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

import turtle
import random


def smile(point_x, point_y, color):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.color(color)
    pen.down()
    pen.circle(50)
    pen.up()
    pen.setpos(point_x - 20, point_y + 60)
    pen.down()
    pen.circle(5)
    pen.up()
    pen.setpos(point_x + 20, point_y + 60)
    pen.down()
    pen.circle(5)
    pen.up()
    pen.setpos(point_x - 25, point_y + 50)
    pen.down()
    pen.right(90)
    pen.circle(25, 180)
    pen.ht()


for _ in range(10):
    turtle.bgcolor('blue')
    smile(random.randint(-300, 300), random.randint(-300, 300), 'green')
