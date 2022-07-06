# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint, choice


class IamGodError(Exception):

    def __str__(self):
        return 'Я бог'


class DrunkError(Exception):

    def __str__(self):
        return 'Я напился'


class CarCrashError(Exception):

    def __str__(self):
        return 'Я попал в аварию'


class GluttonyError(Exception):

    def __str__(self):
        return 'Я нажрался'


class DepressionError(Exception):

    def __str__(self):
        return 'Я в депрессии'


class SuicideError(Exception):

    def __str__(self):
        return 'Я суициднулся'


def one_day():
    list_of_errors = [SuicideError, DepressionError, DrunkError, CarCrashError, GluttonyError, IamGodError]
    dice = randint(1, 13)
    if dice == 13:
        raise choice(list_of_errors)
    return randint(1, 7)


ENLIGHTENMENT_CARMA_LEVEL = 777
my_carma = 0
day = 0
while True:
    day += 1
    try:
        my_carma += one_day()
    except Exception as exc:
        with open('log.txt', mode='a', encoding='utf8') as file:
            file.write(f'В {day} день ' + str(exc) + '\n')
    if my_carma >= ENLIGHTENMENT_CARMA_LEVEL:
        break
print('Я преодолел день сурка')

# https://goo.gl/JnsDqu
