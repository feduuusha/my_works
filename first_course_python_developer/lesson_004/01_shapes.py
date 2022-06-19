# -*- coding: utf-8 -*-

import turtle

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:


# - треугольника
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


# - квадрата
def square(point_x, point_y, angle=0, length=200):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.left(angle)
    pen.down()
    for i in range(0, 4):
        pen.forward(length)
        pen.left(90)


# - пятиугольника
def pentagon(point_x, point_y, angle=0, length=200):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.left(angle)
    pen.down()
    for i in range(0, 5):
        pen.forward(length)
        pen.left(72)


# - шестиугольника
def hexagon(point_x, point_y, angle=0, length=200):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.left(angle)
    pen.down()
    for i in range(0, 6):
        pen.forward(length)
        pen.left(60)


# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны

#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

def n_agon(point_x, point_y, number_of_edges, angle=0, length=200):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(point_x, point_y)
    pen.left(angle)
    pen.down()
    for i in range(0, number_of_edges):
        pen.forward(length)
        pen.left(360 / number_of_edges)
    pen.ht()


n_agon(100, 100, 8, 60, 100)
# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
