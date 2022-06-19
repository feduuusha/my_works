# -*- coding: utf-8 -*-

import turtle

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def n_agon_color(point_x, point_y, number_of_edges, angle=0, length=200):
    colors = {1: 'red', 2: 'orange', 3: 'yellow', 4: 'green',
              5: 'cyan', 6: 'blue', 7: 'purple'}
    print('Выберете цвет из предложенных -', colors)
    user_input = int(input())
    pen = turtle.Turtle()
    pen.pencolor(colors[user_input])
    pen.up()
    pen.setpos(point_x, point_y)
    pen.left(angle)
    pen.down()
    for i in range(0, number_of_edges):
        pen.forward(length)
        pen.left(360 / number_of_edges)
    pen.ht()


def shape_select(point_x, point_y, angle=0, length=200):
    list_of_shapes = {3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon'}
    print('Список доступных фигур -', list_of_shapes)
    user_input = int(input())
    number_of_edges = user_input
    n_agon_color(point_x=point_x, point_y=point_y, number_of_edges=number_of_edges, angle=angle, length=length)


shape_select(100, 100, 60, 200)
