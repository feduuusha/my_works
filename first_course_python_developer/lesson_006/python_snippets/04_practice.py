# -*- coding: utf-8 -*-


# Ним — математическая игра, в которой два игрока по очереди берут предметы,
# разложенные на несколько кучек. За один ход может быть взято любое количество предметов
# (большее нуля) из одной кучки. Выигрывает игрок, взявший последний предмет.
# В классическом варианте игры число кучек равняется трём.

# Составить модуль, реализующий функциональность игры.
# Функции управления игрой
#  разложить_камни()
#  взять_из_кучи(NN, KK)
#  положение_камней() - возвращает список [XX, YY, ZZ, ...] - текущее расположение камней
#  есть_конец_игры() - возвращает True если больше ходов сделать нельзя
#
#
# В текущем модуле (lesson_006/python_snippets/04_practice.py) реализовать логику работы с пользователем:
#  начало игры,
#  вывод расположения камней
#  ввод первым игроком хода - позицию и кол-во камней
#  вывод расположения камней
#  ввод вторым игроком хода - позицию и кол-во камней
#  вывод расположения камней

from nimgame import put_stones, put_from_bunch, stones_positions, is_end_game
from termcolor import colored, cprint


put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(stones_positions(), color='green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрок {}'.format(user_number), color=user_color)
    pos = input(colored('Откуда берём?', color=user_color))
    quantity = input(colored('Сколько берем?', color=user_color))
    step_successful = put_from_bunch(position=int(pos), quantity=int(quantity))
    if is_end_game():
        break
    if step_successful:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход', color='red')


cprint('Выиграл игрок номер {}'.format(user_number), color='red')
