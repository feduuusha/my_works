# -*- coding: utf-8 -*-
import turtle

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


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


n_agon_color(100, 100, 5, angle=30, length=100)
