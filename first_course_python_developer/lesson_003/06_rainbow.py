# -*- coding: utf-8 -*-

# (цикл for)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


import turtle
import time


turtle.bgcolor('blue')
pen = turtle.Turtle()
pen.up()
pen.setpos(-300, -250)
pen.down()
pen.left(40)


def rainbow(color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.forward(900)
    pen.right(90)
    pen.forward(30)
    pen.right(90)
    pen.forward(900)
    pen.right(90)
    pen.forward(30)
    pen.end_fill()
    pen.right(180)
    pen.forward(30)
    pen.left(90)


rainbow_colors = ('red', 'orange', 'yellow', 'green', 'cyan', 'purple')
for i in rainbow_colors:
    rainbow(i)


time.sleep(3)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


pen = turtle.Turtle()

color_list_1 = ['red', 'orange', 'yellow', 'green', 'blue']


def rainbow_curve(set_pose_x, set_pose_y, color_list, bgcolor):
    turtle.bgcolor(bgcolor)
    pen.pensize(57)
    pen.up()
    pen.setpos(set_pose_x, set_pose_y)
    pen.down()
    pen.left(90)
    pen.color(color_list[0])
    for k in range(180):
        pen.forward(4)
        pen.right(1)
    pen.right(90)
    pen.forward(57)
    pen.color(color_list[1])
    pen.right(90)
    pen.forward(5)
    for c in range(180):
        pen.forward(3)
        pen.left(1)
    pen.forward(6)
    pen.left(90)
    pen.forward(57)
    pen.left(90)
    pen.color(color_list[2])
    pen.forward(5)
    for b in range(180):
        pen.forward(2)
        pen.right(1)
    pen.right(90)
    pen.forward(57)
    pen.right(90)
    pen.color(color_list[3])
    pen.forward(5)
    for d in range(180):
        pen.forward(1)
        pen.left(1)
    pen.forward(5)
    pen.left(90)
    pen.forward(57)
    pen.pensize(65)
    pen.color(color_list[4])
    pen.forward(6)
    pen.right(90)
    pen.forward(10)
    pen.right(90)
    pen.color(bgcolor)
    pen.forward(500)
    pen.left(180)
    pen.forward(1000)


rainbow_curve(-300, 0, color_list_1, 'blue')

time.sleep(3)


def rainbow_curve_simple(point_x, point_y, color_list, bg_color):
    pen = turtle.Turtle()
    turtle.bgcolor(bg_color)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.color(color_list[0])
    pen.pensize(13)
    pen.down()
    pen.left(90)
    pen.circle(70, 180)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.right(90)
    pen.forward(10)
    pen.right(90)
    pen.color(color_list[1])
    pen.down()
    pen.circle(60, 180)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.right(90)
    pen.forward(20)
    pen.right(90)
    pen.color(color_list[2])
    pen.down()
    pen.circle(50, 180)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.right(90)
    pen.forward(30)
    pen.right(90)
    pen.color(color_list[3])
    pen.down()
    pen.circle(40, 180)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.right(90)
    pen.forward(40)
    pen.right(90)
    pen.color(color_list[4])
    pen.down()
    pen.circle(30, 180)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
    pen.color(color_list[5])
    pen.down()
    pen.circle(20, 180)
    pen.up()
    pen.setpos(point_x, point_y)
    pen.right(90)
    pen.forward(60)
    pen.right(90)
    pen.color(color_list[6])
    pen.down()
    pen.circle(10, 180)
    time.sleep(3)


list_of_colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'pink', 'purple']
rainbow_curve_simple(100, 100, list_of_colors, 'blue')
