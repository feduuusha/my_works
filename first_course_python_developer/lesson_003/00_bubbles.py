# -*- coding: utf-8 -*-

# Import turtle package
import turtle
import time
import random

pen = turtle.Turtle()
# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

pen.circle(100)
pen.up()
pen.setpos(0, 20)
pen.down()
pen.circle(80)
pen.up()
pen.setpos(0, 40)
pen.down()
pen.circle(60)
pen.up()
pen.setpos(0, 60)
pen.down()
pen.circle(40)
time.sleep(3)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг


def draw_bubble(drawing_point_x, drawing_point_y, step, radius):
    pen = turtle.Turtle()
    pen.up()
    pen.setpos(drawing_point_x, drawing_point_y)
    pen.down()
    pen.circle(radius)
    pen.up()
    pen.setpos(drawing_point_x, drawing_point_y + step)
    pen.down()
    pen.circle(radius - step)
    pen.up()
    pen.setpos(drawing_point_x, drawing_point_y + 2 * step)
    pen.down()
    pen.circle(radius - 2 * step)
    pen.up()
    pen.setpos(drawing_point_x, drawing_point_y + 3 * step)
    pen.down()
    pen.circle(radius - 3 * step)
    pen.up()
    time.sleep(1)


# Нарисовать 10 пузырьков в ряд
for i in range(-500, 501, 100):
    draw_bubble(i, 0, 40, 50)


# Нарисовать три ряда по 10 пузырьков
for i in range(-500, 501, 100):
    draw_bubble(i, -100, 40, 50)
for i in range(-500, 501, 100):
    draw_bubble(i, 0, 40, 50)
for i in range(-500, 501, 100):
    draw_bubble(i, 100, 40, 50)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
k = 0
while k < 100:
    draw_bubble(random.randint(-1000, 1000), random.randint(-1000, 1000), 40, 50)
    k += 1
