# -*- coding: utf-8 -*-

import turtle

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def n_agon(point_x, point_y, angle=0, length=200):
        pen = turtle.Turtle()
        pen.up()
        pen.setpos(point_x, point_y)
        pen.left(angle)
        pen.down()
        for i in range(0, n):
            pen.forward(length)
            pen.left(360 / n)
        pen.ht()
    return n_agon


draw_triangle = get_polygon(n=10)
draw_triangle(100, 100, 60, 200)
