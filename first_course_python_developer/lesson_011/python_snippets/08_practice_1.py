# -*- coding: utf-8 -*-

# Погружаемся в функциональный стиль - За-заикальщик
# Написать функцию которая повторяет два первых символа у строки

animal = 'мишка'


def stutter(text):
    return f'{text[:2]}-{text}'

# Написать функцию которая возвращет функцию повторения двух первых символов n раз


def stutter_factory(n):

    def stutter(text):
        return (text[0:2] + '-') * n + text

    return stutter


stutter_2 = stutter_factory(2)
text = stutter_2('зайка')
print(text)


# Применим все функции поочередно к массиву аргументов
animals = ['зайка', 'мишка', 'бегемотик']
stutters = [stutter_factory(n) for n in range(1, 4)]
result = [func(animal) for func in stutters for animal in animals]
print(result)
