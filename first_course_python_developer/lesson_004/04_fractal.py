# -*- coding: utf-8 -*-


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg


def branch(angle, length=100.0, point_x=0.0, point_y=-50.0):
    import turtle
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
    import turtle
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


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
